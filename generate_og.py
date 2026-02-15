"""Generate OG image matching the retro pixel theme."""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1200, 630
BG = (10, 10, 26)           # --bg-primary #0a0a1a
ACCENT = (0, 255, 136)      # --accent #00ff88
ACCENT2 = (255, 107, 157)   # --accent-secondary #ff6b9d
ACCENT3 = (78, 205, 196)    # --accent-tertiary #4ecdc4
BORDER = (51, 51, 102)      # --border-color #333366
TEXT_SEC = (136, 136, 187)   # --text-secondary #8888bb
SKIN = (255, 221, 187)
HELMET = (43, 58, 140)    # #2b3a8c
WINGS = (255, 204, 0)     # #ffcc00
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SUIT_ACC = (238, 51, 51)  # #ee3333

img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

# --- Scanline effect ---
for y in range(0, H, 4):
    draw.line([(0, y), (W, y)], fill=(0, 0, 0), width=1)

# --- Border frame ---
draw.rectangle([16, 16, W - 17, H - 17], outline=BORDER, width=3)
draw.rectangle([24, 24, W - 25, H - 25], outline=ACCENT, width=2)

# --- Stars ---
import random
random.seed(42)
for _ in range(80):
    x, y = random.randint(30, W - 30), random.randint(30, H - 30)
    brightness = random.randint(60, 160)
    draw.point((x, y), fill=(brightness, brightness, brightness + 40))

# --- New Pixel Avatar (Based on CSS 10x10 grid) ---
PX = 16
avatar_x, avatar_y = 100, 160

def draw_px(x_grid, y_grid, color, w=1, h=1):
    x = avatar_x + x_grid * PX
    y = avatar_y + y_grid * PX
    draw.rectangle([x, y, x + int(PX * w) - 1, y + int(PX * h) - 1], fill=color)

# Row 0: Helmet top
for c in [2, 3, 4, 5]: draw_px(c, 0, HELMET)
# Row 1: Helmet + Wings top
draw_px(1, 1, WINGS)
for c in [2, 3, 4, 5]: draw_px(c, 1, HELMET)
draw_px(6, 1, WINGS)
# Row 2: Helmet + Wings mid
draw_px(0, 2, WINGS); draw_px(1, 2, WINGS)
for c in [2, 3, 4, 5]: draw_px(c, 2, HELMET)
draw_px(6, 2, WINGS); draw_px(7, 2, WINGS)
# Row 3: Goggles top
draw_px(1, 3, HELMET)
draw_px(2, 3, WHITE)
draw_px(3, 3, HELMET)
draw_px(4, 3, WHITE)
for c in [5, 6]: draw_px(c, 3, HELMET)
# Row 4: Goggles mid (pupils)
draw_px(1, 4, HELMET)
draw_px(2, 4, WHITE)
draw_px(2.5, 4, BLACK, 0.5) # Pupil
draw_px(3, 4, HELMET)
draw_px(4, 4, WHITE)
draw_px(4.5, 4, BLACK, 0.5) # Pupil
draw_px(5, 4, HELMET)
# Row 5: Face/Mouth
draw_px(1, 5, HELMET)
for c in [2, 3, 4]: draw_px(c, 5, SKIN)
draw_px(5, 5, HELMET)
# Row 6: Suit start
for c in [1, 2, 4, 5]: draw_px(c, 6, WHITE)
for c in [3, 6]: draw_px(c, 6, SUIT_ACC)
# Row 7: Suit base
draw_px(0, 7, SUIT_ACC)
for c in [1, 2, 3, 4, 5, 6]: draw_px(c, 7, WHITE)
draw_px(7, 7, SUIT_ACC)

# --- Fonts ---
def get_font(size):
    # Try common pixel/retro font paths or standard Windows fonts
    fonts = [
        "C:/Windows/Fonts/PressStart2P-Regular.ttf", # If manually installed
        "C:/Windows/Fonts/consola.ttf",
        "C:/Windows/Fonts/lucon.ttf",
        "C:/Windows/Fonts/msgothic.ttc"
    ]
    for f in fonts:
        if os.path.exists(f):
            return ImageFont.truetype(f, size)
    return ImageFont.load_default()

font_title = get_font(70)
font_sub = get_font(20)
font_small = get_font(14)

title_x = 340
# Shadow
draw.text((title_x + 3, 193), "HONUX", fill=ACCENT2, font=font_title)
# Main
draw.text((title_x, 190), "HONUX", fill=ACCENT, font=font_title)

# --- Subtitle ---
draw.text((title_x, 285), "Software Developer", fill=TEXT_SEC, font=font_sub)
draw.text((title_x, 315), "& Bootcamp Organizer", fill=TEXT_SEC, font=font_sub)

# --- Stats bars ---
bar_y = 380
bar_x = title_x
bar_w = 160
bar_h = 16
labels = [("HP", 0.9, ACCENT), ("MP", 0.65, (68, 136, 255)), ("EXP", 0.75, (255, 204, 0))]
for i, (label, pct, color) in enumerate(labels):
    y = bar_y + i * 32
    draw.text((bar_x, y), label, fill=TEXT_SEC, font=font_small)
    bx = bar_x + 50
    draw.rectangle([bx, y + 2, bx + bar_w, y + bar_h], outline=BORDER, width=2)
    draw.rectangle([bx + 3, y + 5, bx + 3 + int((bar_w - 6) * pct), y + bar_h - 3], fill=color)

# --- Decorative corner brackets ---
corner_len = 20
for cx, cy in [(40, 40), (W - 40, 40), (40, H - 40), (W - 40, H - 40)]:
    dx = 1 if cx < W // 2 else -1
    dy = 1 if cy < H // 2 else -1
    draw.line([(cx, cy), (cx + corner_len * dx, cy)], fill=ACCENT3, width=2)
    draw.line([(cx, cy), (cx, cy + corner_len * dy)], fill=ACCENT3, width=2)

# --- URL at bottom ---
draw.text((W // 2 - 120, H - 70), "honux77.github.io", fill=ACCENT3, font=font_sub)

# --- Save ---
out_dir = os.path.join(os.path.dirname(__file__), "static", "img")
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "og.png")
img.save(out_path, "PNG", optimize=True)
print(f"OG image saved: {out_path} ({os.path.getsize(out_path)} bytes)")
