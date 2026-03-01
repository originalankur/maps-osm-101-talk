import osmnx as ox

place = "Santa Monica, California, USA"

print(f"Fetching features for {place}...")

# 🌳 Parks & green areas
print("Fetching parks...")
parks = ox.features_from_place(place,
            tags={"leisure": "park"})

# 💧 Water bodies
print("Fetching water bodies...")
water = ox.features_from_place(place,
            tags={"natural": "water"})

# 🏢 Buildings
print("Fetching buildings...")
buildings = ox.features_from_place(place,
            tags={"building": True})

print(f"\nParks type: {type(parks)}")
print(f"Parks shape: {parks.shape}")

# Geometry type breakdown
print("\nParks geometry type breakdown:")
print(parks.geometry.geom_type.value_counts())
