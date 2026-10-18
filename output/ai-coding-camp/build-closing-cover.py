"""Build the final full-bleed thank-you cover from the opening artwork."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont


HERE = Path(__file__).parent
SIZE = (1920, 1080)


def font(paths: list[str], size: int) -> ImageFont.FreeTypeFont:
    for item in paths:
        path = Path(item)
        if path.exists():
            return ImageFont.truetype(str(path), size)
    raise FileNotFoundError(f"No suitable font found: {paths}")


cn_font = font(
    [
        "/System/Library/Fonts/STHeiti Medium.ttc",
        "/System/Library/Fonts/Hiragino Sans GB.ttc",
    ],
    118,
)
cn_large = font(
    [
        "/System/Library/Fonts/STHeiti Medium.ttc",
        "/System/Library/Fonts/Hiragino Sans GB.ttc",
    ],
    147,
)
cn_small = font(
    [
        "/System/Library/Fonts/STHeiti Medium.ttc",
        "/System/Library/Fonts/Hiragino Sans GB.ttc",
    ],
    34,
)
cn_footer = font(
    [
        "/System/Library/Fonts/STHeiti Medium.ttc",
        "/System/Library/Fonts/Hiragino Sans GB.ttc",
    ],
    20,
)
mono = font(
    [
        "/System/Library/Fonts/Menlo.ttc",
        "/System/Library/Fonts/Supplemental/Courier New.ttf",
    ],
    20,
)
mono_kicker = font(
    [
        "/System/Library/Fonts/Menlo.ttc",
        "/System/Library/Fonts/Supplemental/Courier New.ttf",
    ],
    24,
)


def draw_motto_row(
    draw: ImageDraw.ImageDraw,
    y: int,
    number: str,
    left: str,
    right: str,
    accent: tuple[int, int, int, int],
) -> None:
    """Render matching four-character halves with a baseline-aligned comma."""
    draw.rounded_rectangle(
        (116, y, 751, y + 74), radius=15,
        fill=(13, 42, 61, 204), outline=(*accent[:3], 105), width=2,
    )
    draw.rounded_rectangle((116, y + 14, 122, y + 60), radius=3, fill=accent)
    draw.text((145, y + 24), number, font=mono, fill=accent, anchor="lt")
    draw.line((186, y + 17, 186, y + 57), fill=(*accent[:3], 95), width=2)
    text_y = y + 20
    draw.text((207, text_y), left, font=cn_small, fill=(228, 240, 247, 255), anchor="lt")
    comma_height = cn_small.getbbox("，", anchor="lt")[3]
    hanzi_height = cn_small.getbbox("进", anchor="lt")[3]
    draw.text((354, text_y + hanzi_height - comma_height), "，", font=cn_small, fill=accent, anchor="lt")
    draw.text((401, text_y), right, font=cn_small, fill=accent, anchor="lt")
    draw.line((693, y + 37, 718, y + 37), fill=(*accent[:3], 170), width=3)
    draw.line((709, y + 28, 718, y + 37, 709, y + 46), fill=(*accent[:3], 170), width=3)

base = Image.open(HERE / "cover.png").convert("RGBA")
base = base.resize(SIZE, Image.Resampling.LANCZOS)

shade = Image.new("RGBA", SIZE, (4, 15, 29, 0))
shade_mask = Image.new("L", SIZE)
mask_pixels = shade_mask.load()
for x in range(SIZE[0]):
    amount = int(max(0, 145 * (1 - x / 1240)))
    for y in range(SIZE[1]):
        mask_pixels[x, y] = amount
shade.putalpha(shade_mask)
base = Image.alpha_composite(base, shade)

bottom = Image.new("RGBA", SIZE, (0, 0, 0, 0))
bottom_draw = ImageDraw.Draw(bottom)
bottom_draw.rectangle((0, 902, 1920, 1080), fill=(2, 12, 24, 50))
bottom = bottom.filter(ImageFilter.GaussianBlur(38))
base = Image.alpha_composite(base, bottom)

text_layer = Image.new("RGBA", SIZE, (0, 0, 0, 0))
draw = ImageDraw.Draw(text_layer)

white = (245, 248, 252, 255)
cyan = (114, 210, 255, 255)
amber = (255, 193, 123, 255)
soft = (202, 221, 232, 255)

for x, y, color in [
    (116, 91, cyan),
    (128, 91, amber),
    (116, 103, amber),
    (128, 103, cyan),
]:
    draw.rounded_rectangle((x, y, x + 8, y + 8), radius=2, fill=color)
draw.text((161, 90), "AI CODING CAMP", font=mono, fill=white, anchor="lt")
draw.line((388, 91, 388, 115), fill=(187, 216, 232, 120), width=2)
draw.text((412, 90), "课程结束", font=cn_footer, fill=(190, 209, 222, 255), anchor="lt")

draw.rounded_rectangle((116, 355, 221, 361), radius=3, fill=amber)
draw.text((116, 383), "THANK YOU", font=mono_kicker, fill=amber, anchor="lt")

glow = Image.new("RGBA", SIZE, (0, 0, 0, 0))
glow_draw = ImageDraw.Draw(glow)
glow_draw.text((108, 552), "参加", font=cn_large, fill=(114, 210, 255, 85), stroke_width=2, anchor="lt")
glow = glow.filter(ImageFilter.GaussianBlur(20))
base = Image.alpha_composite(base, glow)

draw.text((108, 427), "感谢大家", font=cn_font, fill=white, stroke_width=1, anchor="lt")
draw.text((108, 552), "参加", font=cn_large, fill=cyan, stroke_width=1, anchor="lt")
draw.rounded_rectangle((425, 667, 592, 671), radius=2, fill=amber)
draw_motto_row(draw, 723, "01", "理解原理", "动手实践", amber)
draw_motto_row(draw, 809, "02", "相互交流", "共同进步", cyan)

draw.line((116, 954, 488, 954), fill=(161, 204, 227, 92), width=2)
draw.text((116, 978), "AI 编码训练营", font=cn_footer, fill=(204, 222, 233, 200), anchor="lt")

base = Image.alpha_composite(base, text_layer).convert("RGB")
base.save(HERE / "closing-cover.png", optimize=True)
print("Wrote closing-cover.png")
