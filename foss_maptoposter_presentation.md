---
marp: true
theme: default
paginate: true
backgroundColor: #fbfaf8
color: #37352f
style: |
  section {
    font-family: 'JetBrains Mono', 'Fira Code', 'Menlo', 'Monaco', monospace;
    font-size: 28px;
    padding: 50px 70px;
    background-color: #fbfaf8;
    color: #37352f;
  }
  h1 { 
    color: #37352f; 
    font-size: 2.2em; 
    margin-bottom: 0.5em;
    border-bottom: 1px solid #edece9;
    padding-bottom: 10px;
  }
  h2 { 
    color: #37352f; 
    font-size: 1.6em;
    margin-top: 0.5em;
    margin-bottom: 0.4em;
  }
  h3 { color: #787774; font-size: 1.1em; font-weight: normal; }
  strong { color: #2383e2; }
  a { color: #2383e2; text-decoration: none; border-bottom: 1px solid rgba(35, 131, 226, 0.4); }
  code { 
    background: #f1f1ef; 
    color: #eb5757; 
    padding: 0.2em 0.4em; 
    border-radius: 3px; 
    font-size: 0.85em;
  }
  pre { 
    background: #f7f6f3; 
    border: 1px solid #edece9;
    border-radius: 6px; 
    padding: 20px; 
    font-size: 0.8em; 
    line-height: 1.5;
    color: #37352f;
  }
  blockquote {
    background: #f7f6f3;
    border-left: 3px solid #37352f;
    margin: 1em 0;
    padding: 10px 20px;
    color: #787774;
    font-style: normal;
  }
  table { 
    width: 100%; 
    border-collapse: collapse; 
    margin-top: 20px;
    font-size: 0.8em;
  }
  th { 
    text-align: left;
    padding: 12px;
    border-bottom: 2px solid #edece9;
    color: #787774;
    text-transform: uppercase;
    font-size: 0.75em;
    letter-spacing: 0.05em;
  }
  td { 
    padding: 12px; 
    border-bottom: 1px solid #edece9; 
  }
  .columns { display: grid; grid-template-columns: 1fr 1fr; gap: 30px; }
  section.lead {
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
  }
  section.lead h1 { border-bottom: none; font-size: 3em; }
  section.lead blockquote {
    border: 1px solid #edece9;
    border-radius: 8px;
    background: #f7f6f3;
    display: inline-block;
    padding: 20px 30px;
    margin: 20px auto;
  }
---

<!-- _class: lead invert -->

<!-- _class: lead -->

<div style="display: flex; flex-direction: column; align-items: center; justify-content: center;">

<img src="https://raw.githubusercontent.com/originalankur/maptoposter/main/posters/melbourne_forest_20260118_153446.png" height="300px" style="border-radius: 4px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); margin-top: 40px;">

<div style="margin-top: 20px;">

## 🗺️ MapToPoster

### Creating Visually Stunning Map Posters using OpenStreetMap

> *A map is the greatest of all epic poems. Its lines and colours show the realisation of great dreams.*
> — Gilbert H. Grosvenor

**github.com/originalankur/maptoposter**

</div>

</div>

---

## 👋 The Story Behind MapToPoster

- Sitting at a **café in Mumbai**, spotted a minimalist aerial map on the wall
- Thought: *"I can build this — and make it look better"*
- Built MapToPoster as a **fun side project** over a weekend

<br>

### The Result 🚀

| Metric | Number |
|---|---|
| Social media views | **2.3 Million+** |
| Cities mappable | **Any city on Earth** |
| Lines of core code | ~100 |

---

## 🎯 What You'll Learn Today

By building a map **from scratch**, you'll walk away with:

1. **Maps 101** — How do digital maps actually work?
2. **OpenStreetMap** — The Wikipedia of maps
3. **Extracting geospatial data** — Roads, parks, water, buildings
4. **Python tools** — `osmnx` · `geopandas` · `Nominatim` · `matplotlib`
5. **Putting it all together** — A working map poster

---

## 📐 Part 1 — Maps 101

Before we build anything, let's understand how maps represent the **real world digitally**.

We'll cover **6 foundational concepts**:

| # | Concept | One-liner |
|---|---|---|
| 1 | **Coordinates** | Pinpointing any location on Earth |
| 2 | **Geometry Types** | Points, Lines, Polygons |
| 3 | **Scale & Zoom** | From the whole planet to a single building |
| 4 | **Map Projections** | Flattening a sphere onto a screen |
| 5 | **Map Tiles** | Loading maps as small image squares |
| 6 | **Layers** | Stacking data to build a complete map |

---

## 🌐 1. Coordinates — Latitude & Longitude

The **geographic coordinate system** pinpoints any location on Earth using two numbers:

| Axis | Measures | Range | Example |
|---|---|---|---|
| **Latitude** | North ↔ South | -90° to +90° | `19.0760° N` |
| **Longitude** | East ↔ West | -180° to +180° | `72.8777° E` |

### Quick Reference

```
         +90° (North Pole)
           |
  -180° ───┼─── +180°    ← Longitude (E/W)
           |
         -90° (South Pole)
           ↕ Latitude (N/S)
```

- `(19.0760° N, 72.8777° E)` → **Mumbai, India**
- `(35.6762° N, 139.6503° E)` → **Tokyo, Japan**
- Standard used by GPS & OSM: **WGS 84 (EPSG:4326)**

---

## 📍 2. Geometry Types — Vector Data

Digital map features are drawn using **three basic geometric primitives**:

### Points — A single location

- A tree 🌳, a monument, a restaurant 🍽️, a bus stop 🚏
- Stored as one `(lat, lon)` pair

### Lines (LineStrings) — A connected series of points

- A road 🛣️, a river 🏞️, a railway 🚂, a hiking trail
- Stored as an ordered list of `(lat, lon)` pairs

---

## 📍 2. Geometry Types — Vector Data

### Polygons — A closed area

- A building footprint 🏢, a lake 💧, a park 🌿, a country border
- Stored as a ring of `(lat, lon)` pairs where **first = last**

```
Point         Line             Polygon
  •         •───•───•        •───•───•
                               |       |
                               •───•───•
```

---


## 🔍 3. Scale & Zoom Levels

**Scale** = the ratio between distance on the map and distance on the ground.

In web mapping, scale is expressed as **Zoom Levels**:

| Zoom | You See | ~Ground Resolution |
|---|---|---|
| **0** | Entire world | ~156 km/pixel |
| **5** | Continent / large country | ~5 km/pixel |
| **10** | City-level overview | ~150 m/pixel |
| **13** | Neighborhoods & major roads | ~19 m/pixel |
| **16** | Individual streets & blocks | ~2.4 m/pixel |
| **19+** | Building details, doors | ~0.3 m/pixel |

<br>

> As you **zoom in**, the zoom level number **increases**, and you see **more detail** in a **smaller area**. Most web maps support zoom levels **0 – 19**.

---

## 🗺️ 4. Map Projections

A **map projection** is the mathematical method used to flatten the **3D sphere** of Earth onto a **2D screen or paper**.

### The Problem

> You **cannot** perfectly represent a sphere on a flat surface — every projection **distorts** something: area, shape, distance, or direction.

---
## 🗺️ 4. Map Projections

### Web Mercator (EPSG:3857)

The standard projection for **almost all web maps** (OSM, Google Maps, etc.):

| Property | Behavior |
|---|---|
| **Shape** | ✅ Preserved locally (conformal) |
| **Area** | ❌ Distorted — Greenland looks as big as Africa |
| **Direction** | ✅ Preserved — great for navigation |
| **Used by** | OpenStreetMap, Google Maps, Mapbox, Leaflet |

> **Why Mercator?** Straight lines on the map = constant compass bearing. Perfect for navigation, but misleading for comparing sizes of countries.

---

## 🧩 5. Map Tiles

Web maps are **not** loaded as one giant image. Instead, the map is chopped into many small **256×256 pixel squares** called **tiles**.

### How It Works

```
Zoom 0 → 1 tile   (the whole world)
Zoom 1 → 4 tiles  (2×2 grid)
Zoom 2 → 16 tiles (4×4 grid)
  ...
Zoom n → 4ⁿ tiles
```

| Zoom Level | Total Tiles | What You See |
|---|---|---|
| 0 | 1 | World on a postage stamp |
| 10 | ~1 million | City streets appear |
| 18 | ~69 billion | Individual buildings |

### Why Tiles?

- **Performance** — browser only downloads the tiles visible on screen
- **Caching** — tiles are reused across sessions & users
- **Standard URL pattern**: `/{z}/{x}/{y}.png`

---

## 🗂️ 6. Layers

Maps are built by **stacking data** — each layer adds a different category of information:

### Typical Layer Stack (bottom → top)

```
  ┌─────────────────────────┐  ← Labels (street names, POI names)
  ├─────────────────────────┤  ← Points of Interest (cafés, ATMs)
  ├─────────────────────────┤  ← Roads & paths
  ├─────────────────────────┤  ← Buildings
  ├─────────────────────────┤  ← Parks & green areas
  ├─────────────────────────┤  ← Water bodies (rivers, lakes)
  └─────────────────────────┘  ← Base map (land vs ocean)
```

---

### Why Layers Matter

| Benefit | Description |
|---|---|
| **Selective rendering** | Show/hide categories independently |
| **Draw order** | Later layers paint over earlier ones |
| **Styling** | Each layer gets its own colors & line widths |
| **Data sources** | Layers can come from different providers |

> In our MapToPoster project, we'll stack **parks → water → roads → boundary** as separate layers to build the final poster 🗺️

---

## 🌍 Part 2 — OpenStreetMap (OSM)

**Free, editable map of the world** — built by millions of volunteers

### The OSM Data Model

```
Node     ──►  A single point (lat, lon) + tags
Way      ──►  An ordered list of nodes  (road, building outline)
Relation ──►  A group of ways/nodes     (city boundary, bus route)
```

### Tags — The DNA of OSM

```
highway=residential   →  a local road
natural=water         →  a lake or river
leisure=park          →  a park
building=yes          →  a building footprint
amenity=cafe          →  a café ☕
```

---

## 🐍 Part 3 — Your Python Toolkit

### Installation

```bash
pip install osmnx geopandas matplotlib shapely
```

### The Stack

| Library | Role |
|---|---|
| `osmnx` | Downloads OSM data, builds street networks |
| `geopandas` | Geospatial data (pandas + geometry) |
| `Nominatim` | Geocoding — place names → coordinates |
| `matplotlib` | Renders the final map visual |
| `shapely` | Geometric operations (union, buffer, etc.) |

---

## 📍 Part 4 — Nominatim: Geocoding

Converting a **place name → coordinates** (and vice versa)

```python
import osmnx as ox

# Get the boundary polygon of a city
city = ox.geocode_to_gdf("Mumbai, India")
print(city.geometry)
# POLYGON ((72.775... 18.893..., ...))
# Simple lat/lon lookup
point = ox.geocode("Colaba, Mumbai, India")
print(point) # (18.9067, 72.8147)

# Inspect returned columns
print(city.columns.tolist())
# ['geometry', 'bbox_north', 'bbox_south',
#  'bbox_east', 'bbox_west', 'display_name', ...]
```

> `geocode_to_gdf` returns a **GeoDataFrame** — a table where one column holds geometry (polygon, point …)

---

## 🛣️ Part 5 — osmnx: Street Networks

```python
import osmnx as ox

# Download drivable road network
G = ox.graph_from_place("Bandra, Mumbai, India",
                         network_type="drive")

# Basic stats
print(ox.basic_stats(G))
# {'n': 1423, 'm': 3201, 'k_avg': 4.49, ...}

# Convert graph → GeoDataFrames
nodes, edges = ox.graph_to_gdfs(G)
print(edges[["highway", "length", "geometry"]].head())
```

### Network Types

```python
"drive"   # drivable roads only
"walk"    # walkable paths
"bike"    # cyclable paths
"all"     # everything OSM has
```

---

## 🌿 Part 6 — geopandas: Feature Layers

```python
import osmnx as ox

place = "Bandra, Mumbai, India"

# 🌳 Parks & green areas
parks = ox.features_from_place(place,
            tags={"leisure": "park"})

# 💧 Water bodies
water = ox.features_from_place(place,
            tags={"natural": "water"})

# 🏢 Buildings
buildings = ox.features_from_place(place,
            tags={"building": True})

print(type(parks))   # <geopandas.GeoDataFrame>
print(parks.shape)   # (42, 17) — 42 parks, 17 columns

# Geometry type breakdown
print(parks.geometry.geom_type.value_counts())
# Polygon         38
# MultiPolygon     4
```

---

## 🎨 Part 7 — Rendering the Map - Part 1

### Color Palette Setup

```python
import matplotlib.pyplot as plt

BG_COLOR       = "#0d1117"   # near-black background
ROAD_COLOR     = "#ffffff"   # white roads
PARK_COLOR     = "#1a4731"   # dark green parks
WATER_COLOR    = "#1a3a5c"   # deep blue water
```

---


## 🎨 Part 7 — Rendering the Map - Part 2

### Draw Layers (order matters — bottom → top)

```python
fig, ax = plt.subplots(figsize=(12, 16), facecolor=BG_COLOR)
ax.set_facecolor(BG_COLOR)

parks.plot(ax=ax, color=PARK_COLOR, alpha=0.8, linewidth=0)
water.plot(ax=ax, color=WATER_COLOR, alpha=0.9, linewidth=0)
roads.plot(ax=ax, color=ROAD_COLOR, linewidth=0.5, alpha=0.9)
boundary.plot(ax=ax, color="none",
              edgecolor="#ffffff", linewidth=1.5, alpha=0.5)
ax.axis("off")
```

---


## 🛣️ Road Width Hierarchy

Give roads **visual weight** based on their type:

```python
road_widths = {
    "motorway":    2.5, 
    "trunk":       2.0,
    "primary":     1.5,
    "secondary":   1.0,
    "tertiary":    0.7,
    "residential": 0.4,
}

for road_type, width in road_widths.items():
    subset = roads[
        roads["highway"]
            .astype(str)
            .str.contains(road_type, na=False)
    ]
    if not subset.empty:
        subset.plot(ax=ax, color=ROAD_COLOR, 
            linewidth=width, alpha=0.9)
```

---

## �� Part 8 — Full Reusable Script

```python
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
    boundary = ox.geocode_to_gdf(place)
    _, roads = ox.graph_to_gdfs(
                   ox.graph_from_place(place, network_type="all"))
    parks = ox.features_from_place(place,
                tags={"leisure":["park","garden"]})
    water = ox.features_from_place(place,
                tags={"natural":"water","waterway":"river"})
    fig, ax = plt.subplots(figsize=figsize, facecolor=C["bg"])
    ax.set_facecolor(C["bg"])
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
```

---

## ▶️ Run It!

```python
# 🌙 Dark theme
create_map_poster("Bandra, Mumbai, India",
                  output="bandra_dark.png",
                  theme="dark")

# ☀️ Light theme
create_map_poster("Connaught Place, New Delhi, India",
                  output="connaught_light.png",
                  theme="light")

# 🌍 Any city on Earth!
create_map_poster("Shibuya, Tokyo, Japan",
                  output="shibuya.png")
```

---

## 💡 Pro Tips

### Cache downloads — don't re-fetch every run
```python
ox.settings.use_cache = True
ox.settings.cache_folder = "./osm_cache"
```

### Use a bounding box instead of a place name
```python
# north, south, east, west
G = ox.graph_from_bbox(19.08, 18.96, 72.92, 72.79,
                        network_type="drive")
```

### Export SVG for print-quality posters
```python
# Open in Inkscape / Illustrator for further design
plt.savefig("poster.svg", format="svg", bbox_inches="tight")
```

---

## 🧩 Ideas to Extend

| Idea | How |
|---|---|
| Multi-city comparison grid | `plt.subplots(1, 3)` |
| Animated commute routes | `osmnx` shortest path + `animation` |
| 3D elevation maps | `elevation` lib + `matplotlib` 3D axes |
| Interactive web version | `folium` or `leaflet.js` |
| Generate at scale | Loop over city list, batch-save all posters |

---

## 📚 Resources

| Resource | URL |
|---|---|
| 🗂️ MapToPoster GitHub | `github.com/originalankur/maptoposter` |
| 🌍 OSM Wiki | `wiki.openstreetmap.org` |
| 📘 osmnx Docs | `osmnx.readthedocs.io` |
| 🐼 geopandas Docs | `geopandas.org/docs` |
| 📍 Nominatim API | `nominatim.org` |
| 🏷️ OSM Tag Explorer | `taginfo.openstreetmap.org` |

---

<!-- _class: lead invert -->

## 🙏 Thank You!

```bash
pip install osmnx geopandas matplotlib
```

```python
import osmnx as ox, matplotlib.pyplot as plt

_, roads = ox.graph_to_gdfs(
    ox.graph_from_place("YOUR CITY, COUNTRY"))

fig, ax = plt.subplots(figsize=(10, 10), facecolor="black")
roads.plot(ax=ax, color="white", linewidth=0.3)
ax.axis("off")
plt.show()
```

> Questions? Open an issue on GitHub or find me at the conference! 🗺️
