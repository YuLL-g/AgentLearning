"""Render a slide-sized animated GIF for the Agent message history lesson.

Run with the bundled workspace Python (Pillow required). The GIF and poster PNG
are written next to this script; no application or repository files are changed.
"""

from __future__ import annotations

from math import cos, pi, sin
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


HERE = Path(__file__).resolve().parent
GIF_PATH = HERE / "Agent_Message_Growth.gif"
POSTER_PATH = HERE / "Agent_Message_Growth_Poster.png"
W, H = 1280, 720

BG = (10, 18, 33)
PANEL = (20, 32, 53)
CARD = (25, 40, 64)
CARD_ACTIVE = (32, 50, 78)
BORDER = (53, 72, 101)
TEXT = (239, 245, 253)
MUTED = (160, 178, 202)
FAINT = (104, 125, 154)
COLORS = {
    "system": (180, 143, 247),
    "user": (78, 218, 207),
    "assistant": (105, 164, 255),
    "tool": (255, 191, 94),
}

MESSAGES = [
    ("system", "content", "固定规则：依据工具结果回答"),
    ("user", "content", "列出 demo 目录中的文件"),
    ("assistant", "tool_calls", "read_dir(demo)"),
    ("tool", "content", "b.txt、a.txt"),
    ("assistant", "content", "demo 中有 b.txt 和 a.txt"),
    ("user", "content", "请按名称排序后再说一遍"),
    ("assistant", "content", "a.txt、b.txt"),
]

STAGES = [
    ("会话开始", "system 固定规则进入消息列表"),
    ("用户发起第 1 轮", "本轮任务作为 user 消息追加"),
    ("模型请求调用工具", "assistant 记录结构化工具请求"),
    ("工具结果写回", "执行结果作为 tool 消息追加"),
    ("模型形成答复", "assistant 的答复也进入历史"),
    ("用户发起第 2 轮", "前一轮消息成为本轮上下文"),
    ("沿用已有上下文", "模型依据历史结果回答新问题"),
]

FONT_CN = "/System/Library/Fonts/STHeiti Medium.ttc"
FONT_LATIN = "/System/Library/Fonts/HelveticaNeue.ttc"
FONT_MONO = "/System/Library/Fonts/Menlo.ttc"


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size)


F_TITLE = font(FONT_CN, 38)
F_SUB = font(FONT_CN, 19)
F_HEAD = font(FONT_CN, 21)
F_STAGE = font(FONT_CN, 27)
F_BODY = font(FONT_CN, 19)
F_CARD = font(FONT_CN, 23)
F_META = font(FONT_LATIN, 20)
F_MONO = font(FONT_MONO, 19)
F_NUM = font(FONT_MONO, 18)
F_ICON = font(FONT_LATIN, 34)


def text_center(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int],
                value: str, face: ImageFont.FreeTypeFont, fill: tuple[int, ...]) -> None:
    left, top, right, bottom = draw.textbbox((0, 0), value, font=face)
    width, height = right - left, bottom - top
    x0, y0, x1, y1 = box
    draw.text((x0 + (x1 - x0 - width) / 2, y0 + (y1 - y0 - height) / 2 - top),
              value, font=face, fill=fill)


def rounded(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int],
            radius: int, fill: tuple[int, ...], outline=None, width: int = 1) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def draw_icon(draw: ImageDraw.ImageDraw, role: str, cx: int, cy: int, color: tuple[int, ...]) -> None:
    if role == "system":
        points = [(cx, cy - 23), (cx + 20, cy - 14), (cx + 17, cy + 9),
                  (cx, cy + 25), (cx - 17, cy + 9), (cx - 20, cy - 14)]
        draw.polygon(points, outline=color, width=4)
        draw.line([(cx - 8, cy), (cx - 1, cy + 7), (cx + 11, cy - 9)], fill=color, width=4)
    elif role == "user":
        draw.ellipse((cx - 11, cy - 22, cx + 11, cy), outline=color, width=4)
        draw.arc((cx - 24, cy - 1, cx + 24, cy + 31), 180, 360, fill=color, width=4)
    elif role == "assistant":
        draw.polygon([(cx, cy - 27), (cx + 7, cy - 7), (cx + 27, cy),
                      (cx + 7, cy + 7), (cx, cy + 27), (cx - 7, cy + 7),
                      (cx - 27, cy), (cx - 7, cy - 7)], fill=color)
    else:
        draw.line((cx - 19, cy + 19, cx + 15, cy - 15), fill=color, width=7)
        draw.arc((cx + 4, cy - 28, cx + 29, cy - 3), 20, 250, fill=color, width=5)
        draw.ellipse((cx - 23, cy + 14, cx - 11, cy + 26), outline=color, width=3)


def draw_card(index: int, active: bool) -> Image.Image:
    role, field, value = MESSAGES[index]
    accent = COLORS[role]
    layer = Image.new("RGBA", (786, 70), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    rounded(d, (4, 5, 782, 68), 15, (0, 0, 0, 60))
    rounded(d, (1, 1, 778, 64), 15, CARD_ACTIVE if active else CARD,
            accent if active else BORDER, width=2 if active else 1)
    rounded(d, (1, 12, 6, 53), 3, accent)
    d.text((27, 19), f"{index + 1:02d}", font=F_NUM, fill=FAINT)
    rounded(d, (79, 13, 220, 52), 11, (*accent, 36), accent, 1)
    text_center(d, (79, 13, 220, 52), role, F_META, accent)
    d.text((245, 20), field, font=F_MONO, fill=MUTED)
    d.text((400, 17), value, font=F_CARD, fill=TEXT)
    return layer


def draw_base() -> Image.Image:
    image = Image.new("RGBA", (W, H), (*BG, 255))
    d = ImageDraw.Draw(image)

    # Small structural dots add depth without competing with the message stack.
    for yy in range(22, H, 36):
        for xx in range(22, W, 36):
            if xx < 60 or xx > 1220 or yy < 138:
                d.ellipse((xx, yy, xx + 1, yy + 1), fill=(37, 55, 80))

    d.text((68, 38), "Agent 会话中的消息如何累积", font=F_TITLE, fill=TEXT)
    d.text((70, 98), "固定规则  →  第一轮任务  →  工具调用  →  工具结果  →  下一轮输入",
           font=F_SUB, fill=MUTED)

    d.text((113, 139), "messages[]", font=F_MONO, fill=MUTED)
    d.line((82, 162, 82, 645), fill=BORDER, width=3)
    d.line((82, 162, 96, 162), fill=BORDER, width=3)
    d.line((82, 645, 96, 645), fill=BORDER, width=3)

    rounded(d, (902, 151, 1214, 647), 22, PANEL, BORDER, 1)
    d.text((930, 178), "当前追加", font=F_HEAD, fill=MUTED)
    d.line((930, 460, 1186, 460), fill=BORDER, width=2)
    d.text((930, 479), "消息历史", font=F_HEAD, fill=MUTED)
    rounded(d, (958, 565, 1157, 616), 13, (33, 53, 82), BORDER, 1)
    text_center(d, (958, 565, 1157, 616), "LLM 下一次调用", F_BODY, TEXT)
    d.line((1058, 538, 1058, 558), fill=FAINT, width=3)
    d.polygon([(1052, 552), (1064, 552), (1058, 560)], fill=FAINT)
    d.text((70, 678), "示意结构 · 工具调用字段与上下文保留方式因 Agent 而异",
           font=F_SUB, fill=FAINT)
    return image


def draw_stage(step: int, progress: float) -> Image.Image:
    image = draw_base()
    d = ImageDraw.Draw(image)
    role = MESSAGES[step][0]
    accent = COLORS[role]

    # Earlier messages stay in place. The newest card slides into the array.
    for index in range(step + 1):
        y = 167 + 69 * index
        if index == step:
            x = 110 + round(56 * (1 - progress))
            card = draw_card(index, active=True)
            alpha = card.getchannel("A").point(lambda v: round(v * progress))
            card.putalpha(alpha)
        else:
            x = 110
            card = draw_card(index, active=False)
        image.alpha_composite(card, (x, y))
        d = ImageDraw.Draw(image)

    # Moving dot and arrow show the current item entering the message array.
    y_mid = 200 + 69 * step
    d.line((878, y_mid, 901, y_mid), fill=accent, width=3)
    d.polygon([(878, y_mid), (889, y_mid - 6), (889, y_mid + 6)], fill=accent)
    dot_x = 900 - round(20 * progress)
    d.ellipse((dot_x - 5, y_mid - 5, dot_x + 5, y_mid + 5), fill=accent)

    d.text((1130, 180), f"{step + 1:02d}/07", font=F_MONO, fill=TEXT)
    cx, cy = 1058, 279
    pulse = 3 * (1 - cos(pi * progress)) / 2
    r = round(58 + pulse)
    icon_bg = tuple(round(BG[channel] * 0.72 + accent[channel] * 0.28)
                    for channel in range(3))
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=icon_bg, outline=accent, width=3)
    draw_icon(d, role, cx, cy, accent)

    title, detail = STAGES[step]
    d.text((930, 365), title, font=F_STAGE, fill=TEXT)
    d.text((930, 407), detail, font=F_BODY, fill=MUTED)
    for idx, (message_role, _, _) in enumerate(MESSAGES):
        x0 = 930 + idx * 37
        if idx <= step:
            fill = COLORS[message_role]
        else:
            fill = (58, 75, 102)
        rounded(d, (x0, 515, x0 + 28, 526), 5, fill)

    return image.convert("RGB")


def main() -> None:
    frames: list[Image.Image] = []
    durations: list[int] = []
    for step in range(len(MESSAGES)):
        for progress in (0.25, 0.50, 0.75, 1.0):
            frames.append(draw_stage(step, progress))
            durations.append(90 if progress < 1 else (1900 if step == 6 else 900))

    frames[-1].save(POSTER_PATH, optimize=True)
    palette = frames[-1].quantize(colors=128, method=Image.Quantize.MEDIANCUT)
    gif_frames = [frame.quantize(palette=palette, dither=Image.Dither.NONE)
                  for frame in frames]
    gif_frames[0].save(
        GIF_PATH,
        save_all=True,
        append_images=gif_frames[1:],
        duration=durations,
        loop=0,
        disposal=2,
        optimize=True,
    )
    print(f"{GIF_PATH} ({len(frames)} frames, {W}×{H})")
    print(POSTER_PATH)


if __name__ == "__main__":
    main()
