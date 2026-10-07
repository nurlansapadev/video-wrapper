"""Замеры обложек для разбора стиля (core/thumbnails.md, «Создание стиля»).

Использование:
    python tools/thumb_metrics.py <файл> [<файл> ...]

Принимает скрины из ленты YouTube (обрезает белую подпись под обложкой) и готовые обложки 1280x720.
Выводит: долю почти чёрного, среднюю насыщенность, долю красного, 6 доминирующих цветов (hex, %),
яркость верхней полосы 25% и правого нижнего угла (0–255).
"""
import colorsys
import sys

from PIL import Image


def crop_feed_caption(im):
    """Обрезать белую подпись под обложкой, если это скрин из ленты."""
    px = im.load()
    w, h = im.size
    for y in range(int(h * 0.3), h):
        row = [px[x, y] for x in range(10, w - 10, 5)]
        if sum(1 for r in row if min(r) > 245) / len(row) > 0.97:
            return im.crop((0, 0, w, y))
    return im


def luma(p):
    r, g, b = p
    return 0.299 * r + 0.587 * g + 0.114 * b


def measure(path):
    im = crop_feed_caption(Image.open(path).convert("RGB"))
    w, h = im.size
    pixels = list(im.resize((96, 54)).getdata())
    n = len(pixels)

    dark = sum(1 for p in pixels if luma(p) < 51) * 100 // n
    sat = sum(colorsys.rgb_to_hsv(*[c / 255 for c in p])[1] for p in pixels) / n
    red = sum(1 for r, g, b in pixels if r > 90 and r > 2 * g and r > 2 * b) * 100 // n

    q = im.resize((64, 36)).quantize(colors=6, method=Image.MEDIANCUT)
    pal = q.getpalette()
    colors = sorted(q.getcolors(), reverse=True)
    dominant = ", ".join(
        "#%02X%02X%02X %d%%" % (pal[i * 3], pal[i * 3 + 1], pal[i * 3 + 2], c * 100 // (64 * 36))
        for c, i in colors
    )

    top = list(im.crop((0, 0, w, int(h * 0.25))).resize((48, 8)).getdata())
    br = list(im.crop((int(w * 0.8), int(h * 0.8), w, h)).resize((16, 8)).getdata())

    print(f"\n{path}  ({w}x{h}, {w / h:.2f})")
    print(f"  почти чёрного (<20% яркости): {dark}%")
    print(f"  насыщенность (HSV): {sat:.2f}")
    print(f"  красного: {red}%")
    print(f"  доминирующие цвета: {dominant}")
    print(f"  яркость верхних 25%: {sum(map(luma, top)) / len(top):.0f} · правого нижнего угла: {sum(map(luma, br)) / len(br):.0f}")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    for f in sys.argv[1:]:
        measure(f)
