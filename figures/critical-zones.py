from svgtools import *

import svgwrite
from cairosvg import svg2png, svg2pdf


def draw_seat_price_illustration(svg_filename="critical-zones.svg"):
    dwg = svgwrite.Drawing(svg_filename, size=("800px", "200px"))

    x_start = 100
    x_end = 700
    bar_y = 100
    bar_height = 20

    # Background bar with faded edges
    dwg.add(dwg.rect((x_start - 50, bar_y), (x_end - x_start + 100, bar_height), fill="lightgray", opacity=0.3, rx=10))
    dwg.add(dwg.rect((x_start, bar_y), (x_end - x_start, bar_height), fill="gray", rx=10))

    # Orange zone
    orange_start = 200
    orange_end = 600
    dwg.add(dwg.rect((orange_start, bar_y), (orange_end - orange_start, bar_height), fill="orange"))

    # Red block (N)
    red_width = 50
    dwg.add(dwg.rect((orange_start, bar_y), (red_width, bar_height), fill="red"))
    dwg.add(dwg.text(
        "N",
        insert=(orange_start + red_width, bar_y + 40),  # On the right edge of red block
        text_anchor="middle",
        font_size="12px",
    ))
    dwg.add(dwg.text(
        "Zona en la que perder 10.000 votos costaría un escaño",
        insert=(orange_start + red_width / 2, bar_y - 10),
        text_anchor="middle",
        font_size="11px",
    ))

    # Green block (P - N)
    green_width = 50
    green_start = orange_end - green_width
    dwg.add(dwg.rect((green_start, bar_y), (green_width, bar_height), fill="green"))
    dwg.add(dwg.text(
        "P - N",
        insert=(green_start, bar_y + 40),  # On the left edge of green block
        text_anchor="middle",
        font_size="12px",
    ))
    dwg.add(dwg.text(
        "Zona en la que ganar 10.000 votos valdría un escaño",
        insert=(green_start + green_width / 2, bar_y - 10),
        text_anchor="middle",
        font_size="11px",
    ))

    # Dashed boundary markers and labels
    for x, label in [(orange_start, "Último escaño conseguido"), (orange_end, "Umbral siguiente escaño")]:
        dwg.add(dwg.line((x, bar_y - 30), (x, bar_y + bar_height + 10), stroke="black", stroke_dasharray="5,5"))
        dwg.add(dwg.text(label, insert=(x, bar_y - 35), text_anchor="middle", font_size="11px"))

    # Define arrow marker for bidirectional arrow
    arrow_marker = dwg.marker(id="arrow", insert=(5, 5), size=(10, 10), orient="auto")
    arrow_marker.add(dwg.path("M0,5 L10,0 L10,10 Z", fill="black"))
    dwg.defs.add(arrow_marker)

    # Double-headed arrow (P)
    arrow_y = bar_y - 60
    arrow_line = dwg.line((orange_start, arrow_y), (orange_end, arrow_y), stroke="black", stroke_width=1)
    arrow_line.attribs["marker-start"] = arrow_marker.get_funciri()
    arrow_line.attribs["marker-end"] = arrow_marker.get_funciri()
    dwg.add(arrow_line)

    dwg.add(dwg.text(
        "Precio final del escaño P (pe. 100.000 votos)",
        insert=((orange_start + orange_end) / 2, arrow_y - 5),
        text_anchor="middle",
        font_size="11px",
    ))

    # Save the SVG
    dwg.save()

    # Export to PNG and PDF using CairoSVG
    with open(svg_filename, "rb") as f:
        svg_data = f.read()
        svg2png(bytestring=svg_data, write_to=svg_filename.replace(".svg", ".png"))
        svg2pdf(bytestring=svg_data, write_to=svg_filename.replace(".svg", ".pdf"))


# Run it
draw_seat_price_illustration()

