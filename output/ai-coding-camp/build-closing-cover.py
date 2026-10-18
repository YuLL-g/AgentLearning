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
    31,
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


def draw_chinese_line(draw: ImageDraw.ImageDraw, text: str, x: int, y: int, fill: tuple[int, int, int, int]) -> None:
    """Place full-width punctuation at the same visual baseline as the Hanzi."""
    cursor = float(x)
    hanzi_height = cn_small.getbbox("进", anchor="lt")[3]
    for char in text:
        glyph_height = cn_small.getbbox(char, anchor="lt")[3]
        punctuation_shift = hanzi_height - glyph_height if char in "，。" else 0
        draw.text((round(cursor), y + punctuation_shift), char, font=cn_small, fill=fill, anchor="lt")
        cursor += draw.textlength(char, font=cn_small)

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
draw_chinese_line(draw, "从理解到实践，继续探索。", 116, 752, soft)
draw_chinese_line(draw, "相互交流，共同进步", 116, 810, soft)

draw.line((116, 954, 488, 954), fill=(161, 204, 227, 92), width=2)
draw.text((116, 978), "AI 编码训练营", font=cn_footer, fill=(204, 222, 233, 200), anchor="lt")

base = Image.alpha_composite(base, text_layer).convert("RGB")
base.save(HERE / "closing-cover.png", optimize=True)
print("Wrote closing-cover.png")
