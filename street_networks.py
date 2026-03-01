import osmnx as ox

# Download drivable road network
print("Downloading street network for Santa Monica, California, USA...")
G = ox.graph_from_place("Santa Monica, California, USA",
                         network_type="drive")

# Basic stats
print("\nBasic network stats:")
print(ox.basic_stats(G))

# Convert graph → GeoDataFrames
print("\nConverting graph to GeoDataFrames...")
nodes, edges = ox.graph_to_gdfs(G)
print("\nEdges head (highway, length, geometry):")
print(edges[["highway", "length", "geometry"]].head())

print("\nNetwork Types reference:")
print('"drive"   # drivable roads only')
print('"walk"    # walkable paths')
print('"bike"    # cyclable paths')
print('"all"     # everything OSM has')
