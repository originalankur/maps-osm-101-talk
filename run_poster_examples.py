from full_reusable_script import create_map_poster

# 🌙 Dark theme
print("\n--- Example 1: Dark Theme ---")
create_map_poster("Santa Monica, California, USA",
                  output="santa_monica_dark.png",
                  theme="dark")

# ☀️ Light theme
print("\n--- Example 2: Light Theme ---")
create_map_poster("Manhattan, New York City, New York, USA",
                  output="manhattan_light.png",
                  theme="light")

# 🌍 Any city on Earth!
print("\n--- Example 3: Tokyo (Shibuya) ---")
create_map_poster("Shibuya, Tokyo, Japan",
                  output="shibuya.png")
