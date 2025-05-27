import colour
import cairosvg
from pathlib import Path

def parse_scenario(filepath):
    candidatures = []
    especiales = {}
    print(f"=== Processing {filepath}")
    with Path(filepath).open(encoding='utf-8') as f:
        for line in f:
            if not line.strip():
                continue
            parts = line.strip().split('\t')
            if parts[0].lower() == "siglas":
                continue  # saltar cabecera
            key = parts[0]
            if key.lower() in ["censo", "participacion", "abstencion", "nulos", "blancos"]:
                especiales[key.lower()] = int(parts[1])
                continue
            votos = int(parts[1])
            diputados = int(parts[2]) if len(parts) > 2 else 0
            nombre = parts[3] if len(parts) > 3 else ""
            candidatures.append({
                "siglas": key,
                "votos": votos,
                "diputados": diputados,
                "nombre": nombre
            })
    return especiales, candidatures

def spnum(n):
    return f"{n:,}".translate(str.maketrans({',':'.', '.':','}))


def darken(color, factor=0.83):
    try:
        base_color = colour.Color(color)
    except ValueError:
        return colour.Color("grey").hex

    hsl = colour.rgb2hsl(base_color.rgb)
    hsl = (hsl[0], hsl[1], max(0, min(1, hsl[2] * factor)))
    darkened_rgb = colour.hsl2rgb((hsl[0], hsl[1], max(0, min(1, hsl[2] * factor))))
    darkened_color = colour.Color(rgb=darkened_rgb).hex
    return darkened_color


def draw_annotation(
    text,
    target_x,
    target_y,
    label_x,
    label_y,
    vertical_alignment="bottom",
    horizontal_alignment="right",
    font_size=14,
    color="#000000",
):
    """
    Draws an annotation with a line from target to label and places aligned text at the label point.
    """
    # Retornar el path generado en formato SVG
    return (
        f'<path d="M {target_x} {target_y} L {target_x} {(target_y + label_y)/2} {label_x} {label_y}" fill="none" stroke="{color}" stroke-width="1" />'
        + draw_text(
            label_x, label_y, text, horizontal_alignment, vertical_alignment, font_size
        )
    )


def draw_bar_segment(
    current_x, y, width, height, fill_color, stroke_width=4
):
    return f'<rect x="{current_x}" y="{y}" width="{width}" height="{height}" fill="{fill_color}" stroke="{darken(fill_color)}" stroke-width="{stroke_width}" />'


def draw_legend(legend_items, legend_x, legend_y, font_size=14, border_color="#000000"):
    legend = ""
    for label, color in legend_items:
        legend += (
            f'<rect x="{legend_x}" y="{legend_y}" width="20" height="20" fill="{color}" stroke="{border_color}" stroke-width="2" />'
            f'<text x="{legend_x + 25}" y="{legend_y + 15}" font-size="{font_size}" font-family="sans-serif">{label}</text>'
        )
        legend_x += 230
    return legend

def draw_text(
    x, y, text, horizontal_alignment="left", vertical_alignment="bottom", font_size=14, color="black",
):
    """
    Draws an SVG <text> element anchored at the given point using intuitive alignment terms.
    """
    horizontal_map = {"left": "start", "center": "middle", "right": "end"}
    vertical_map = {"top": "hanging", "center": "middle", "bottom": "text-after-edge"}

    text_anchor = horizontal_map[horizontal_alignment]
    dominant_baseline = vertical_map[vertical_alignment]

    return f"""
<text x="{x}" y="{y}" text-anchor="{text_anchor}" dominant-baseline="{dominant_baseline}" font-size="{font_size}" font-family="sans-serif" fill="{color}">
  {text}
</text>
    """

def export_png_pdf(svg_file):
    svgfile = Path(svg_file)

    pdf_file = str(svgfile.with_suffix('.pdf'))
    print(f"== Generating {pdf_file}...")
    cairosvg.svg2pdf(url=svg_file, write_to=pdf_file)

    png_file = str(svgfile.with_suffix('.png'))
    print(f"== Generating {png_file}...")
    cairosvg.svg2png(url=svg_file, write_to=png_file)


def dump_image(content, output_basename, width, height):
    svg = (
        f'<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">\n'
        + content +
        "</svg>"
    )

    svg_file = f"{output_basename}.svg"
    with open(svg_file, "w") as f:
        f.write(svg)
    export_png_pdf(svg_file)


