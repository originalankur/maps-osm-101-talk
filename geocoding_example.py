import osmnx as ox

# Get the boundary polygon of a city
print("Fetching boundary for Santa Monica, California, USA...")
city = ox.geocode_to_gdf("Santa Monica, California, USA")
print(city.geometry)

# Simple lat/lon lookup
print("\nFetching coordinates for Colaba, Mumbai, India...")
point = ox.geocode("Colaba, Mumbai, India")
print(point) # (18.9067, 72.8147)

# Inspect returned columns
print("\nColumns in city GeoDataFrame:")
print(city.columns.tolist())
