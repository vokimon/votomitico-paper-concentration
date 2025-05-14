import svgwrite
from cairosvg import svg2png, svg2pdf

# New helper function to handle multiline text
def add_text(dwg, x, y, lines, font_size="11px", line_spacing=14, text_anchor='middle', dominant_baseline="auto"):
    """
    Adds multiline text to the drawing.
    
    :param dwg: The SVG drawing object.
    :param x: horizontal position of the insertion point
    :param y: vertical position of the insertion point
    :param lines: List of text lines to be added.
    :param font_size: The font size of the text.
    :param line_spacing: The space between lines.
    """
    if type(lines) == str:
        lines = lines.split('\n')
    if dominant_baseline != "hanging":
        y = y - (len(lines)-1) * line_spacing
    for i, line in enumerate(lines):
        dwg.add(dwg.text(
            line,
            insert=(x, y + i*line_spacing),
            text_anchor=text_anchor,
            dominant_baseline=dominant_baseline,
            font_size=font_size,
        ))


def draw_seat_price_illustration(svg_filename="critical-zones.svg"):
    dwg = svgwrite.Drawing(svg_filename, size=("700px", "250px"))

    x_start = 50
    x_end = 650
    bar_y = 100
    bar_height = 50
    bar_color = "#335566"
    transfer_size = 50


    # --- Gradient fade background (dark blue with transparent edges) ---
    gradient = dwg.linearGradient(start=(0, 0), end=(1, 0), id="fade-gradient")
    gradient.add_stop_color(offset="0%", color=bar_color, opacity=0)
    gradient.add_stop_color(offset="5%", color=bar_color, opacity=1)
    gradient.add_stop_color(offset="95%", color=bar_color, opacity=1)
    gradient.add_stop_color(offset="100%", color=bar_color, opacity=0)
    dwg.defs.add(gradient)

    dwg.add(
        dwg.rect(
            insert=(x_start, bar_y),
            size=(x_end - x_start, bar_height),
            fill="url(#fade-gradient)"
        )
    )

    # Orange zone
    orange_start = 120
    orange_end = 580
    dwg.add(dwg.rect(
        (orange_start, bar_y),
        (orange_end - orange_start, bar_height),
        fill="orange",
    ))

    ordenate_offset = 4

    add_text(dwg, orange_end, bar_y + bar_height + ordenate_offset, "P\n100.000", text_anchor="middle", dominant_baseline="hanging", font_size="12px")
    add_text(dwg, orange_start, bar_y + bar_height + ordenate_offset, "0", text_anchor="middle", dominant_baseline="hanging", font_size="12px")
    # Red block (N)
    red_center = orange_start + transfer_size / 2
    dwg.add(dwg.rect((orange_start, bar_y), (transfer_size, bar_height), fill="red"))
    add_text(dwg, orange_start + transfer_size, bar_y + bar_height + ordenate_offset, "N\n10.000", text_anchor="middle", dominant_baseline="hanging", font_size="12px")

    # Green block (P - N)
    green_start = orange_end - transfer_size
    green_center = green_start + transfer_size / 2
    dwg.add(dwg.rect((green_start, bar_y), (transfer_size, bar_height), fill="#4b3"))
    add_text(dwg, green_start, bar_y + bar_height + ordenate_offset, "P - N\n90.000", text_anchor="middle", dominant_baseline="hanging", font_size="12px")

    def add_measure(x, label):
        dwg.add(dwg.line((x, bar_y - 30), (x, bar_y + bar_height + 10), stroke="black", stroke_dasharray="5,5"))
        add_text(dwg, x, bar_y -35, label, text_anchor="middle", font_size="11px")

    add_measure(orange_start, ["Último escaño", "conseguido"])
    add_measure(orange_end, ["Umbral siguiente", "escaño"])

    # Define arrow markers
    arrow_left = dwg.marker(id="arrow-left", insert=(0, 5), size=(10, 10), orient="auto")
    arrow_left.add(dwg.path("M10,0 L0,5 L10,10 Z", fill="black"))  # left-pointing
    dwg.defs.add(arrow_left)

    arrow_right = dwg.marker(id="arrow-right", insert=(10, 5), size=(10, 10), orient="auto")
    arrow_right.add(dwg.path("M0,0 L10,5 L0,10 Z", fill="black"))
    dwg.defs.add(arrow_right)

    # Seat price
    arrow_y = bar_y - 15
    arrow_line = dwg.line((orange_start, arrow_y), (orange_end, arrow_y), stroke="black", stroke_width=1)
    arrow_line.attribs["marker-start"] = arrow_left.get_funciri()
    arrow_line.attribs["marker-end"] = arrow_right.get_funciri()
    dwg.add(arrow_line)

    add_text(dwg,
        x = (orange_start + orange_end) / 2,
        y = arrow_y - 5,
        lines= "Precio del escaño, P\n(pe. 100.000 votos)",
        text_anchor="middle",
        dominant_baseline="auto",
        font_size="11px",
    )

    # Critical zones

    text_block_y = bar_y + 90
    offset_x = -90

    # --- Red zone multiline text and arrow ---
    red_text_x = red_center - offset_x
    add_text(dwg, red_text_x, text_block_y, [
        "Zona en la que",
        "perder 10.000 votos",
        "quitaría un escaño",
    ], dominant_baseline="hanging")

    dwg.add(dwg.line(
        (red_text_x, text_block_y - 5),
        (red_center, bar_y + bar_height / 2),
        stroke="black",
        stroke_width=1,
        marker_end=arrow_right.get_funciri()
    ))

    # --- Green zone multiline text and arrow ---
    green_text_x = green_center + offset_x
    add_text(dwg, green_text_x, text_block_y, [
        "Zona en la que",
        "ganar 10.000 votos",
        "añadiría un escaño",
    ], dominant_baseline="hanging")

    dwg.add(dwg.line(
        (green_text_x, text_block_y - 5),
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

