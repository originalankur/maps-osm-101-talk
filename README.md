# 🗺️ MapToPoster Script Collection

This directory contains standalone Python scripts extracted from the MapToPoster technical presentation. These scripts provide a step-by-step guide to building visually stunning map posters using OpenStreetMap data and Python.

## 📁 Directory Structure

```text
maptoposter_scripts/
├── venv/                   # Python virtual environment
├── geocoding_example.py     # Part 4: Coordinates & Geocoding
├── street_networks.py       # Part 5: Road network extraction
├── feature_layers.py        # Part 6: Parks, Water & Buildings
├── color_palette.py         # Part 7: Design & Aesthetics
├── render_layers.py         # Part 7: Layer stacking & plotting
├── road_width_hierarchy.py  # Advanced: Visual weight for roads
├── full_reusable_script.py  # Part 8: Consolidated poster function
└── run_poster_examples.py   # Demonstration: Multi-city examples
```

## 📜 Script Reference

| Script | What it Does | Key Learnings |
|---|---|---|
| `geocoding_example.py` | Converts "Santa Monica, CA" into geometry and "Colaba, Mumbai" into Coordinates. | `osmnx.geocode_to_gdf`, `osmnx.geocode`, GeoDataFrame columns. |
| `street_networks.py` | Downloads a drivable road network and calculates basic stats (circuity, node count). | `ox.graph_from_place`, `ox.graph_to_gdfs`, network types ("drive", "walk"). |
| `feature_layers.py` | Extracts specific OSM features like parks (`leisure: park`) and water bodies. | `ox.features_from_place`, OSM tagging system (`leisure`, `natural`). |
| `color_palette.py` | Defines the hex codes for a "Dark" map theme (High contrast). | Visualizing design tokens before implementation. |
| `render_layers.py` | Stacks parks, water, and roads using Matplotlib plotting order. | Layering logic: Parks (bottom) → Water → Roads → Boundary (top). |
| `road_width_hierarchy.py` | Assigns different line widths to `motorway` vs `residential` roads. | Loop-based styling, conditional filtering in GeoPandas. |
| `full_reusable_script.py` | Provides a robust `create_map_poster` function with Light/Dark themes. | Procedural map generation, reusable Python functions. |
| `run_poster_examples.py` | Generates posters for Santa Monica, Manhattan, and Shibuya. | Script automation, parameterizing the poster function. |

## 🚀 Getting Started

To run these scripts, you need to use the provided virtual environment:

1. **Navigate to this folder:**
   ```bash
   cd /Users/ank/Documents/nanobot/maptoposter_scripts
   ```

2. **Activate the environment:**
   ```bash
   source venv/bin/activate
   ```

3. **Run any script:**
   ```bash
   python3 run_poster_examples.py
   ```

---
*Created as part of the MapToPoster Technical Presentation workshop.* 🗺️
