import osmnx as ox
import matplotlib.pyplot as plt

place = "Santa Monica, California, USA"
BG_COLOR = "#0d1117"
ROAD_COLOR = "#ffffff"

print(f"Fetching road network for {place}...")
_, roads = ox.graph_to_gdfs(ox.graph_from_place(place, network_type="drive"))

fig, ax = plt.subplots(figsize=(12, 16), facecolor=BG_COLOR)
ax.set_facecolor(BG_COLOR)

road_widths = {
    "motorway":    2.5, 
    "trunk":       2.0,
    "primary":     1.5,
    "secondary":   1.0,
    "tertiary":    0.7,
    "residential": 0.4,
}

print("Plotting roads with width hierarchy...")
for road_type, width in road_widths.items():
    subset = roads[
        roads["highway"]
            .astype(str)
            .str.contains(road_type, na=False)
    ]
    if not subset.empty:
        subset.plot(ax=ax, color=ROAD_COLOR, 
            linewidth=width, alpha=0.9)

ax.axis("off")
output = "road_width_hierarchy.png"
plt.savefig(output, dpi=300, bbox_inches="tight", facecolor=BG_COLOR)
print(f"✅ Saved → {output}")
