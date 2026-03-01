import osmnx as ox
import matplotlib.pyplot as plt

place = "Santa Monica, California, USA"
BG_COLOR       = "#0d1117"
ROAD_COLOR     = "#ffffff"
PARK_COLOR     = "#1a4731"
WATER_COLOR    = "#1a3a5c"

print(f"Preparing data for rendering {place}...")
boundary = ox.geocode_to_gdf(place)
_, roads = ox.graph_to_gdfs(ox.graph_from_place(place, network_type="drive"))
parks = ox.features_from_place(place, tags={"leisure": "park"})
water = ox.features_from_place(place, tags={"natural": "water"})

print("Rendering layers...")
fig, ax = plt.subplots(figsize=(12, 16), facecolor=BG_COLOR)
ax.set_facecolor(BG_COLOR)

parks.plot(ax=ax, color=PARK_COLOR, alpha=0.8, linewidth=0)
water.plot(ax=ax, color=WATER_COLOR, alpha=0.9, linewidth=0)
roads.plot(ax=ax, color=ROAD_COLOR, linewidth=0.5, alpha=0.9)
boundary.plot(ax=ax, color="none",
              edgecolor="#ffffff", linewidth=1.5, alpha=0.5)
ax.axis("off")

output = "layers_render.png"
plt.savefig(output, dpi=300, bbox_inches="tight", facecolor=BG_COLOR)
print(f"✅ Saved → {output}")
