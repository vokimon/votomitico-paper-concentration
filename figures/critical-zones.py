import svgwrite
from cairosvg import svg2png, svg2pdf


def draw_seat_price_illustration(svg_filename="critical-zones.svg"):
    dwg = svgwrite.Drawing(svg_filename, size=("800px", "250px"))

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
    red_center = orange_start + red_width / 2
    dwg.add(dwg.rect((orange_start, bar_y), (red_width, bar_height), fill="red"))
    dwg.add(dwg.text("N", insert=(orange_start + red_width, bar_y + 40), text_anchor="middle", font_size="12px"))

    # Green block (P - N)
    green_width = 50
    green_start = orange_end - green_width
    green_center = green_start + green_width / 2
    dwg.add(dwg.rect((green_start, bar_y), (green_width, bar_height), fill="green"))
    dwg.add(dwg.text("P - N", insert=(green_start, bar_y + 40), text_anchor="middle", font_size="12px"))

    # Dashed vertical lines and labels
    for x, label in [(orange_start, "Último escaño conseguido"), (orange_end, "Umbral siguiente escaño")]:
        dwg.add(dwg.line((x, bar_y - 30), (x, bar_y + bar_height + 10), stroke="black", stroke_dasharray="5,5"))
        dwg.add(dwg.text(label, insert=(x, bar_y - 35), text_anchor="middle", font_size="11px"))

    # Define arrow markers
    arrow_left = dwg.marker(id="arrow-left", insert=(5, 5), size=(10, 10), orient="auto")
    arrow_left.add(dwg.path("M10,0 L0,5 L10,10 Z", fill="black"))
    dwg.defs.add(arrow_left)

    arrow_right = dwg.marker(id="arrow-right", insert=(5, 5), size=(10, 10), orient="auto")
    arrow_right.add(dwg.path("M0,0 L10,5 L0,10 Z", fill="black"))
    dwg.defs.add(arrow_right)

    # Double-headed arrow (Precio del escaño)
    arrow_y = bar_y - 60
    arrow_line = dwg.line((orange_start, arrow_y), (orange_end, arrow_y), stroke="black", stroke_width=1)
    arrow_line.attribs["marker-start"] = arrow_left.get_funciri()
    arrow_line.attribs["marker-end"] = arrow_right.get_funciri()
    dwg.add(arrow_line)

    dwg.add(dwg.text(
        "Precio final del escaño P (pe. 100.000 votos)",
        insert=((orange_start + orange_end) / 2, arrow_y - 5),
        text_anchor="middle",
        font_size="11px",
    ))

    # --- Red zone multiline text and arrow ---
    multiline_font_size = "11px"
    line_spacing = 14
    text_block_y = bar_y + 60

    red_lines = [
        "Zona en la que",
        "perder 10.000 votos",
        "costaría un escaño",
    ]
    for i, line in enumerate(red_lines):
        dy = text_block_y + i * line_spacing
        dwg.add(dwg.text(line, insert=(red_center, dy), text_anchor="middle", font_size=multiline_font_size))

    dwg.add(dwg.line(
        (red_center, text_block_y + len(red_lines) * line_spacing - 2),
        (red_center, bar_y + bar_height / 2),
        stroke="black",
        stroke_width=1,
        marker_end=arrow_right.get_funciri()
    ))

    # --- Green zone multiline text and arrow ---
    green_lines = [
        "Zona en la que",
        "ganar 10.000 votos",
        "valdría un escaño",
    ]
    for i, line in enumerate(green_lines):
        dy = text_block_y + i * line_spacing
        dwg.add(dwg.text(line, insert=(green_center, dy), text_anchor="middle", font_size=multiline_font_size))

    dwg.add(dwg.line(
        (green_center, text_block_y + len(green_lines) * line_spacing - 2),
        (green_center, bar_y + bar_height / 2),
        stroke="black",
        stroke_width=1,
        marker_end=arrow_right.get_funciri()
    ))

    # Save the SVG
    dwg.save()

    # Export to PNG and PDF using CairoSVG
    with open(svg_filename, "rb") as f:
        svg_data = f.read()
        svg2png(bytestring=svg_data, write_to=svg_filename.replace(".svg", ".png"))
        svg2pdf(bytestring=svg_data, write_to=svg_filename.replace(".svg", ".pdf"))


# Run the function
draw_seat_price_illustration()

