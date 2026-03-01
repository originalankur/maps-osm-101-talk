import osmnx as ox
import matplotlib.pyplot as plt

def create_map_poster(place, output="poster.png",
                      theme="dark", figsize=(12, 16)):
    THEMES = {
        "dark":  {"bg":"#0d1117","road":"#e5e7eb",
                  "park":"#14532d","water":"#1e3a5f","text":"white"},
        "light": {"bg":"#f8f4ef","road":"#374151",
                  "park":"#bbf7d0","water":"#bfdbfe","text":"#111827"},
    }
    C = THEMES[theme]
    
    print(f"Generating poster for {place} with {theme} theme...")
    
    print("Fetching boundary...")
    boundary = ox.geocode_to_gdf(place)
    
    print("Fetching road network...")
    _, roads = ox.graph_to_gdfs(
                   ox.graph_from_place(place, network_type="all"))
    
    print("Fetching parks...")
    parks = ox.features_from_place(place,
                tags={"leisure":["park","garden"]})
    
    print("Fetching water...")
    water = ox.features_from_place(place,
                tags={"natural":"water","waterway":"river"})
    
    fig, ax = plt.subplots(figsize=figsize, facecolor=C["bg"])
    ax.set_facecolor(C["bg"])
    
    print("Rendering layers...")
    parks.plot(ax=ax, color=C["park"], alpha=0.85, linewidth=0)
    water.plot(ax=ax, color=C["water"], alpha=0.9,  linewidth=1)
    roads.plot(ax=ax, color=C["road"], linewidth=0.4, alpha=0.9)
    boundary.plot(ax=ax, color="none",
                  edgecolor=C["road"], linewidth=1.5, alpha=0.4)
    
    ax.set_title(place.split(",")[0].upper(),
                 color=C["text"], fontsize=32, fontweight="bold")
    ax.axis("off")
    
    plt.savefig(output, dpi=300,
                bbox_inches="tight", facecolor=C["bg"])
    print(f"✅ Saved → {output}")

if __name__ == "__main__":
    create_map_poster("Santa Monica, California, USA", output="santa_monica_full.png")
