import colour
import cairosvg

def darken(color, factor=0.6):
    try:
        base_color = colour.Color(color)
    except ValueError:
        return "#ff0000"
    
    # Obtenemos el color en formato RGB
    rgb = base_color.rgb
    
    # Convertimos el color RGB a HSL
    hsl = colour.rgb2hsl(rgb)
    
    # Aplicamos el factor de oscurcimiento en el canal de luminosidad (L)
    hsl = (hsl[0], hsl[1], max(0, min(1, hsl[2] * factor)))
    
    # Convertimos el color HSL de nuevo a RGB
    darkened_rgb = colour.hsl2rgb(hsl)
    
    # Devolvemos el color oscurecido en formato hexadecimal
    darkened_color = colour.Color(rgb=darkened_rgb).hex
    return darkened_color

def draw_text(text, target_x, target_y, label_x, label_y, align_v='bottom', align_h='left', font_size=14):
    alignments = {
        'left': lambda x: x,
        'center': lambda x: x - font_size / 2,
        'right': lambda x: x - font_size
    }
    label_x_adjusted = alignments[align_h](label_x)
    
    vertical_alignments = {
        'top': lambda y: y + font_size,
        'center': lambda y: y - font_size / 2,
        'bottom': lambda y: y - font_size
    }
    label_y_adjusted = vertical_alignments[align_v](label_y)
    
    # Dibujamos la línea y el texto
    line = f'<line x1="{target_x}" y1="{target_y}" x2="{label_x}" y2="{label_y}" stroke="#000000" stroke-width="1"/>'
    text_svg = f'<text x="{label_x_adjusted}" y="{label_y_adjusted}" font-size="{font_size}" font-family="sans-serif" text-anchor="middle">{text}</text>'
    return line + text_svg

def draw_annotation(text, target_x, target_y, label_x, label_y, align_v, align_h):
    return draw_text(text, target_x, target_y, label_x, label_y, align_v, align_h)

def draw_bar_segment(current_x, y, width, height, fill_color, stroke_color="#000000", stroke_width=2):
    return f'<rect x="{current_x}" y="{y}" width="{width}" height="{height}" fill="{fill_color}" stroke="{stroke_color}" stroke-width="{stroke_width}" />'

def draw_legend(legend_items, legend_x, legend_y, font_size=14, border_color="#000000"):
    legend = ""
    for label, color in legend_items:
        legend += (
            f'<rect x="{legend_x}" y="{legend_y}" width="20" height="20" fill="{color}" stroke="{border_color}" stroke-width="2" />'
            f'<text x="{legend_x + 25}" y="{legend_y + 15}" font-size="{font_size}" font-family="sans-serif">{label}</text>'
        )
        legend_x += 160
    return legend

def generate_seat_bar(
    total_votes=37000,
    votes_per_seat=10000,
    output_basename="seats-and-remainder"
):
    seats = total_votes // votes_per_seat
    remainder_votes = total_votes % votes_per_seat
    votes_to_next = votes_per_seat - remainder_votes if remainder_votes > 0 else 0
    margin = 40
    annotation_height = 40
    bar_height = 40
    legend_height = 60
    total_bar_width = 600
    svg_width = total_bar_width + 2 * margin
    svg_height = margin + annotation_height + bar_height + legend_height + margin
    seat_color = "#4F81BD"
    remainder_color = "#FF6F00"
    missing_color = "transparent"
    border_color = "#000000"
    stroke_width = 2
    font_size = 14
    seat_width = total_bar_width / (seats + 1)
    remainder_width = seat_width * (remainder_votes / votes_per_seat)
    missing_width = seat_width * (votes_to_next / votes_per_seat)
    bar_y = margin + annotation_height
    legend_y = bar_y + bar_height + 30
    votes_y = margin + annotation_height - 10
    votes_x = seat_width * seats + remainder_width
    cut_x = seat_width
    next_seat_x = seat_width * (seats + 1)
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{svg_width}" height="{svg_height}" xmlns="http://www.w3.org/2000/svg">
  <g transform="translate({margin}, 0)">
'''
    current_x = 0
    bar_segments = ""
    for _ in range(seats):
        bar_segments += draw_bar_segment(current_x, bar_y, seat_width, bar_height, seat_color, border_color, stroke_width)
        current_x += seat_width
    if remainder_votes > 0:
        bar_segments += draw_bar_segment(current_x, bar_y, remainder_width, bar_height, remainder_color, border_color, stroke_width)
        current_x += remainder_width
    if missing_width > 0:
        bar_segments += draw_bar_segment(current_x, bar_y, missing_width, bar_height, missing_color, border_color, stroke_width)
    annotations = ""
    annotations += draw_annotation("Precio de corte", cut_x, votes_y, cut_x - 40, votes_y - 20, "top", "left")
    if remainder_votes > 0:
        annotations += draw_annotation("Votos", votes_x, votes_y, votes_x + 40, votes_y - 20, "top", "right")
    next_seat_y_top = bar_y + bar_height
    next_seat_y_label = next_seat_y_top + 10
    annotations += draw_annotation("Siguiente escaño", next_seat_x, next_seat_y_top, next_seat_x - 40, next_seat_y_label + 20, "bottom", "center")
    legend_items = [
        ("Escones", seat_color),
        ("Resto", remainder_color)
    ]
    legend = draw_legend(legend_items, margin, legend_y, font_size, border_color)
    svg += bar_segments + annotations + legend + "</g></svg>"
    
    svg_file = f"{output_basename}.svg"
    with open(svg_file, "w") as f:
        f.write(svg)

    pdf_file = f"{output_basename}.pdf"
    png_file = f"{output_basename}.png"

    cairosvg.svg2pdf(url=svg_file, write_to=pdf_file)
    cairosvg.svg2png(url=svg_file, write_to=png_file)

    print("Files generated:")
    print(f" - {svg_file}")
    print(f" - {pdf_file}")
    print(f" - {png_file}")

if __name__ == "__main__":
    generate_seat_bar()
bla

import colour

def darken(color, factor=0.6):
    try:
        base_color = colour.Color(color)
    except ValueError:
        return "#000000"
    rgb = base_color.rgb
    hsl = colour.rgb2hsl(rgb[0], rgb[1], rgb[2])
    hsl = (hsl[0], hsl[1], max(0, min(1, hsl[2] * factor)))
    darkened_rgb = colour.hsl2rgb(hsl[0], hsl[1], hsl[2])
    darkened_color = colour.Color(rgb=darkened_rgb).hex
    return darkened_color

def draw_text(text, target_x, target_y, label_x, label_y, align_v='bottom', align_h='left', font_size=14):
    alignments = {
        'left': lambda x: x,
        'center': lambda x: x - font_size / 2,
        'right': lambda x: x - font_size
    }
    label_x_adjusted = alignments[align_h](label_x)
    vertical_alignments = {
        'top': lambda y: y + font_size,
        'center': lambda y: y - font_size / 2,
        'bottom': lambda y: y - font_size
    }
    label_y_adjusted = vertical_alignments[align_v](label_y)
    line = f'<line x1="{target_x}" y1="{target_y}" x2="{label_x}" y2="{label_y}" stroke="#000000" stroke-width="1"/>'
    text_svg = f'<text x="{label_x_adjusted}" y="{label_y_adjusted}" font-size="{font_size}" font-family="sans-serif" text-anchor="middle">{text}</text>'
    return line + text_svg

def draw_annotation(text, target_x, target_y, label_x, label_y, align_v, align_h):
    return draw_text(text, target_x, target_y, label_x, label_y, align_v, align_h)

def draw_bar_segment(current_x, y, width, height, fill_color, stroke_color="#000000", stroke_width=2):
    return f'<rect x="{current_x}" y="{y}" width="{width}" height="{height}" fill="{fill_color}" stroke="{stroke_color}" stroke-width="{stroke_width}" />'

def draw_legend(legend_items, legend_x, legend_y, font_size=14, border_color="#000000"):
    legend = ""
    for label, color in legend_items:
        legend += (
            f'<rect x="{legend_x}" y="{legend_y}" width="20" height="20" fill="{color}" stroke="{border_color}" stroke-width="2" />'
            f'<text x="{legend_x + 25}" y="{legend_y + 15}" font-size="{font_size}" font-family="sans-serif">{label}</text>'
        )
        legend_x += 160
    return legend

def generate_seat_bar(
    total_votes=37000,
    votes_per_seat=10000,
    output_basename="seats-and-remainder"
):
    seats = total_votes // votes_per_seat
    remainder_votes = total_votes % votes_per_seat
    votes_to_next = votes_per_seat - remainder_votes if remainder_votes > 0 else 0
    margin = 40
    annotation_height = 40
    bar_height = 40
    legend_height = 60
    total_bar_width = 600
    svg_width = total_bar_width + 2 * margin
    svg_height = margin + annotation_height + bar_height + legend_height + margin
    seat_color = "#4F81BD"
    remainder_color = "#FF6F00"
    missing_color = "transparent"
    border_color = "#000000"
    stroke_width = 2
    font_size = 14
    seat_width = total_bar_width / (seats + 1)
    remainder_width = seat_width * (remainder_votes / votes_per_seat)
    missing_width = seat_width * (votes_to_next / votes_per_seat)
    bar_y = margin + annotation_height
    legend_y = bar_y + bar_height + 30
    votes_y = margin + annotation_height - 10
    votes_x = seat_width * seats + remainder_width
    cut_x = seat_width
    next_seat_x = seat_width * (seats + 1)
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{svg_width}" height="{svg_height}" xmlns="http://www.w3.org/2000/svg">
  <g transform="translate({margin}, 0)">
'''
    current_x = 0
    bar_segments = ""
    for _ in range(seats):
        bar_segments += draw_bar_segment(current_x, bar_y, seat_width, bar_height, seat_color, border_color, stroke_width)
        current_x += seat_width
    if remainder_votes > 0:
        bar_segments += draw_bar_segment(current_x, bar_y, remainder_width, bar_height, remainder_color, border_color, stroke_width)
        current_x += remainder_width
    if missing_width > 0:
        bar_segments += draw_bar_segment(current_x, bar_y, missing_width, bar_height, missing_color, border_color, stroke_width)
    annotations = ""
    annotations += draw_annotation("Precio de corte", cut_x, votes_y, cut_x - 40, votes_y - 20, "top", "left")
    if remainder_votes > 0:
        annotations += draw_annotation("Votos", votes_x, votes_y, votes_x + 40, votes_y - 20, "top", "right")
    next_seat_y_top = bar_y + bar_height
    next_seat_y_label = next_seat_y_top + 10
    annotations += draw_annotation("Siguiente escaño", next_seat_x, next_seat_y_top, next_seat_x - 40, next_seat_y_label + 20, "bottom", "center")
    legend_items = [
        ("Escones", seat_color),
        ("Resto", remainder_color)
    ]
    legend = draw_legend(legend_items, margin, legend_y, font_size, border_color)
    svg += bar_segments + annotations + legend + "</g></svg>"
    
    with open(f"{output_basename}.svg", "w") as f:
        f.write(svg)

    cairosvg.svg2pdf(url=svg_file, write_to=pdf_file)
    cairosvg.svg2png(url=svg_file, write_to=png_file)

    print("Files generated:")
    print(f" - {svg_file}")
    print(f" - {pdf_file}")
    print(f" - {png_file}")

if __name__ == "__main__":
    generate_seat_bar()

bla

import colour

def darken(color, factor=0.6):
    """
    Darkens a color by a factor using the 'colour' library.
    
    color: Color in any format supported by colour (e.g., '#RRGGBB', 'red', etc.)
    factor: Factor to darken the color. 0.0 will return black, 1.0 will return the original color.
    
    Returns: A darkened color in hexadecimal format.
    """
    try:
        # Convert the color to a colour.Color object (this handles many formats)
        base_color = colour.Color(color)
    except ValueError:
        # If the color is invalid, return black
        return "#000000"

    # Get the RGB values of the color
    rgb = base_color.rgb
    
    # Convert RGB to HSL (hue, saturation, lightness)
    hsl = colour.rgb2hsl(rgb)
    
    # Darken the color by reducing its lightness (clamping between 0 and 1)
    hsl = (hsl[0], hsl[1], max(0, min(1, hsl[2] * factor)))
    
    # Convert HSL back to RGB
    darkened_rgb = colour.hsl2rgb(hsl)
    
    # Convert the RGB back to hexadecimal
    darkened_color = colour.Color(rgb=darkened_rgb).hex
 
    return darkened_color


def draw_bar_segment(current_x, y, width, height, fill_color, stroke_color="#000000", stroke_width=2):
    """
    Draws a single bar segment using the provided color, darkening the stroke automatically.
    
    current_x: The x-coordinate where the segment starts.
    y: The y-coordinate of the bar.
    width: The width of the segment.
    height: The height of the segment.
    fill_color: The color to fill the segment with.
    stroke_color: The color of the border of the segment (default is black).
    stroke_width: The width of the border.
    """
    # Darken the fill color for the stroke color
    darkened_stroke_color = darken(fill_color, 0.8)  # Darken by 20%
    
    # Return the SVG code for the segment with darkened stroke
    return f'<rect x="{current_x}" y="{y}" width="{width}" height="{height}" fill="{fill_color}" stroke="{darkened_stroke_color}" stroke-width="{stroke_width}" />'


def generate_seat_bar(
    total_votes=37000,
    votes_per_seat=10000,
    output_basename="seats-and-remainder"
):
    # === Main logic ===
    seats = total_votes // votes_per_seat
    remainder_votes = total_votes % votes_per_seat
    votes_to_next = votes_per_seat - remainder_votes if remainder_votes > 0 else 0

    # === Dimensions and layout ===
    margin = 40
    annotation_height = 40
    bar_height = 40
    legend_height = 60
    total_bar_width = 600

    svg_width = total_bar_width + 2 * margin
    svg_height = margin + annotation_height + bar_height + legend_height + margin

    # === Colors ===
    seat_color = "#4F81BD"         # Medium blue
    remainder_color = "#FF6F00"    # Strong orange
    missing_color = "transparent"  # Transparent background
    border_color = "#000000"
    stroke_width = 2
    font_size = 14

    # === Width calculations ===
    seat_width = total_bar_width / (seats + 1)
    remainder_width = seat_width * (remainder_votes / votes_per_seat)
    missing_width = seat_width * (votes_to_next / votes_per_seat)

    # === Vertical positions ===
    bar_y = margin + annotation_height
    legend_y = bar_y + bar_height + 30
    votes_y = margin + annotation_height - 10  # For the annotations above the bar

    # === Key horizontal coordinates ===
    votes_x = seat_width * seats + remainder_width
    cut_x = seat_width
    next_seat_x = seat_width * (seats + 1)

    # === Construct SVG header ===
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{svg_width}" height="{svg_height}" xmlns="http://www.w3.org/2000/svg">
  <g transform="translate({margin}, 0)">
'''

    # === Draw the bar segments ===
    current_x = 0
    bar_segments = ""
    for _ in range(seats):
        bar_segments += draw_bar_segment(current_x, bar_y, seat_width, bar_height, seat_color, border_color, stroke_width)
        current_x += seat_width

    if remainder_votes > 0:
        bar_segments += draw_bar_segment(current_x, bar_y, remainder_width, bar_height, remainder_color, border_color, stroke_width)
        current_x += remainder_width

    if missing_width > 0:
        bar_segments += draw_bar_segment(current_x, bar_y, missing_width, bar_height, missing_color, border_color, stroke_width)

    # === Annotations ===
    annotations = ""

    # Price of cutoff (above left)
    annotations += draw_annotation("Precio de corte", cut_x, bar_y, cut_x - 40, votes_y - 20, "bottom", "left")

    # Votes (above right)
    if remainder_votes > 0:
        annotations += draw_annotation("Votos", votes_x, bar_y, votes_x + 40, votes_y - 20, "bottom", "left")

    # Next seat (below the bar)
    next_seat_y_top = bar_y + bar_height
    next_seat_y_label = next_seat_y_top + 10
    annotations += draw_annotation("Siguiente escaño", next_seat_x, next_seat_y_top, next_seat_x - 40, next_seat_y_label + 20, "top", "left")

    # === Legend ===
    legend_items = [("Escaños", seat_color), ("Restos", remainder_color)]
    legend = draw_legend(legend_items, 0, legend_y, font_size, border_color)

    # === Combine all SVG parts ===
    svg += bar_segments  # Add bar segments
    svg += annotations    # Add annotations
    svg += legend         # Add legend

    svg += "\n</g>\n</svg>"

    # === Save files ===
    svg_file = f"{output_basename}.svg"
    pdf_file = f"{output_basename}.pdf"
    png_file = f"{output_basename}.png"

    with open(svg_file, "w") as file:
        file.write(svg)

    cairosvg.svg2pdf(url=svg_file, write_to=pdf_file)
    cairosvg.svg2png(url=svg_file, write_to=png_file)

    print("Files generated:")
    print(f" - {svg_file}")
    print(f" - {pdf_file}")
    print(f" - {png_file}")

if __name__ == "__main__":
    generate_seat_bar()
bla

#!/usr/bin/env python3
import cairosvg

def draw_text(x, y, text, horizontal_alignment="left", vertical_alignment="bottom", font_size=14):
    """
    Draws an SVG <text> element anchored at the given point using intuitive alignment terms.
    """
    horizontal_map = {
        "left": "start",
        "center": "middle",
        "right": "end"
    }

    vertical_map = {
        "top": "hanging",
        "center": "middle",
        "bottom": "text-after-edge"
    }

    if horizontal_alignment not in horizontal_map:
        raise ValueError(f"Invalid horizontal alignment: {horizontal_alignment}")
    if vertical_alignment not in vertical_map:
        raise ValueError(f"Invalid vertical alignment: {vertical_alignment}")

    text_anchor = horizontal_map[horizontal_alignment]
    dominant_baseline = vertical_map[vertical_alignment]

    return f'''
<text x="{x}" y="{y}" text-anchor="{text_anchor}" dominant-baseline="{dominant_baseline}" font-size="{font_size}" font-family="sans-serif">
  {text}
</text>
    '''


def draw_annotation(text, target_x, target_y, label_x, label_y,
                    vertical_alignment="bottom", horizontal_alignment="center",
                    font_size=14, border_color="#000000"):
    """
    Draws an annotation with a line from target to label and places aligned text at the label point.
    """
    line = f'<line x1="{target_x}" y1="{target_y}" x2="{label_x}" y2="{label_y}" stroke="{border_color}" stroke-width="1" />'
    label = draw_text(label_x, label_y, text, horizontal_alignment, vertical_alignment, font_size)
    return line + label


def draw_bar_segment(current_x, y, width, height, fill_color, stroke_color="#000000", stroke_width=2):
    return f'<rect x="{current_x}" y="{y}" width="{width}" height="{height}" fill="{fill_color}" stroke="{stroke_color}" stroke-width="{stroke_width}" />'


def draw_legend(legend_items, legend_x, legend_y, font_size=14, border_color="#000000"):
    legend = ""
    for label, color in legend_items:
        legend += (
            f'<rect x="{legend_x}" y="{legend_y}" width="20" height="20" fill="{color}" stroke="{border_color}" stroke-width="2" />'
            f'<text x="{legend_x + 25}" y="{legend_y + 15}" font-size="{font_size}" font-family="sans-serif">{label}</text>'
        )
        legend_x += 160
    return legend


def generate_seat_bar(
    total_votes=37000,
    votes_per_seat=10000,
    output_basename="seats-and-remainder"
):
    seats = total_votes // votes_per_seat
    remainder_votes = total_votes % votes_per_seat
    votes_to_next = votes_per_seat - remainder_votes if remainder_votes > 0 else 0

    margin = 40
    annotation_height = 40
    bar_height = 40
    legend_height = 60
    total_bar_width = 600

    svg_width = total_bar_width + 2 * margin
    svg_height = margin + annotation_height + bar_height + legend_height + margin

    seat_color = "#4F81BD"
    remainder_color = "#FF6F00"
    missing_color = "transparent"
    border_color = "#000000"
    stroke_width = 2
    font_size = 14

    seat_width = total_bar_width / (seats + 1)
    remainder_width = seat_width * (remainder_votes / votes_per_seat)
    missing_width = seat_width * (votes_to_next / votes_per_seat)

    bar_y = margin + annotation_height
    legend_y = bar_y + bar_height + 30
    votes_y = margin + annotation_height - 10

    votes_x = seat_width * seats + remainder_width
    cut_x = seat_width
    next_seat_x = seat_width * (seats + 1)

    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{svg_width}" height="{svg_height}" xmlns="http://www.w3.org/2000/svg">
  <g transform="translate({margin}, 0)">
'''

    current_x = 0
    bar_segments = ""
    for _ in range(seats):
        bar_segments += draw_bar_segment(current_x, bar_y, seat_width, bar_height, seat_color, border_color, stroke_width)
        current_x += seat_width

    if remainder_votes > 0:
        bar_segments += draw_bar_segment(current_x, bar_y, remainder_width, bar_height, remainder_color, border_color, stroke_width)
        current_x += remainder_width

    if missing_width > 0:
        bar_segments += draw_bar_segment(current_x, bar_y, missing_width, bar_height, missing_color, border_color, stroke_width)

    annotations = ""

    # Cutoff annotation
    annotations += draw_annotation(
        "Precio de corte",
        target_x=cut_x + 5, target_y=bar_y,
        label_x=cut_x - 40, label_y=votes_y - 20,
        vertical_alignment="bottom", horizontal_alignment="center"
    )

    # Votes annotation
    if remainder_votes > 0:
        annotations += draw_annotation(
            "Votos",
            target_x=votes_x, target_y=bar_y,
            label_x=votes_x + 40, label_y=votes_y - 20,
            vertical_alignment="bottom", horizontal_alignment="center"
        )

    # Next seat annotation (below)
    annotations += draw_annotation(
        "Siguiente escaño",
        target_x=next_seat_x, target_y=bar_y + bar_height,
        label_x=next_seat_x - 40, label_y=bar_y + bar_height + 40,
        vertical_alignment="top", horizontal_alignment="center"
    )

    legend_items = [("Escaños", seat_color), ("Restos", remainder_color)]
    legend = draw_legend(legend_items, 0, legend_y, font_size, border_color)

    svg += bar_segments
    svg += annotations
    svg += legend
    svg += "\n</g>\n</svg>"

    svg_file = f"{output_basename}.svg"
    pdf_file = f"{output_basename}.pdf"
    png_file = f"{output_basename}.png"

    with open(svg_file, "w") as file:
        file.write(svg)

    cairosvg.svg2pdf(url=svg_file, write_to=pdf_file)
    cairosvg.svg2png(url=svg_file, write_to=png_file)

    print("Files generated:")
    print(f" - {svg_file}")
    print(f" - {pdf_file}")
    print(f" - {png_file}")


if __name__ == "__main__":
    generate_seat_bar()



bla

#!/usr/bin/env python3
import cairosvg

def draw_text(x, y, text, horizontal_alignment="left", vertical_alignment="top", font_size=14):
    """
    Generates an SVG text element aligned to a specified reference point.

    Parameters:
    - x, y: Coordinates of the alignment point.
    - text: The text to be displayed.
    - horizontal_alignment: 'left', 'center', or 'right'.
    - vertical_alignment: 'top', 'center', or 'bottom'.
    - font_size: Font size in pixels.

    Returns:
    - SVG <text> element as a string.
    """

    # Map intuitive CSS-style alignments to SVG equivalents
    horizontal_map = {
        "left": "start",
        "center": "middle",
        "right": "end"
    }

    vertical_map = {
        "top": "hanging",
        "center": "middle",
        "bottom": "text-after-edge"
    }

    text_anchor = horizontal_map[horizontal_alignment]
    dominant_baseline = vertical_map[vertical_alignment]

    return f'''
<text x="{x}" y="{y}" text-anchor="{text_anchor}" dominant-baseline="{dominant_baseline}" font-size="{font_size}" font-family="sans-serif">
  {text}
</text>
    '''

    

def draw_annotation(x1, y1, x2, y2, label_x, label_y, label_text, font_size=14, label_offset=20, border_color="#000000"):
    """
    Draws an annotation with an oblique line and a label.
    
    x1, y1: Starting coordinates of the vertical line.
    x2, y2: Ending coordinates of the vertical line on the bar.
    label_x, label_y: Position of the label.
    label_text: The text of the label.
    font_size: Font size for the label (optional).
    label_offset: Offset for the label (optional).
    border_color: Color of the line for the annotation.
    """
    # Calculating the oblique line coordinates
    oblique_x2 = x2 + (x2 - x1) * 0.4  # Shift oblique line for an angle
    oblique_y2 = y2 - (y2 - y1) * 0.4  # Similarly shift in the y direction for the oblique angle

    # Draw the oblique line
    annotation = (
        f'<line x1="{x1}" y1="{y1}" x2="{oblique_x2}" y2="{oblique_y2}" stroke="{border_color}" stroke-width="1"/>'
        f'<line x1="{oblique_x2}" y1="{oblique_y2}" x2="{x2}" y2="{y2}" stroke="{border_color}" stroke-width="1"/>'
    )
    annotation += draw_text(label_x, label_y, label_text, horizontal_alignment="center", vertical_alignment="bottom", font_size=font_size)
    return annotation


def draw_bar_segment(current_x, y, width, height, fill_color, stroke_color="#000000", stroke_width=2):
    """
    Draws a single bar segment.
    
    current_x: The x-coordinate where the segment starts.
    y: The y-coordinate of the bar.
    width: The width of the segment.
    height: The height of the segment.
    fill_color: The color to fill the segment with.
    stroke_color: The color of the border of the segment.
    stroke_width: The width of the border.
    """
    return f'<rect x="{current_x}" y="{y}" width="{width}" height="{height}" fill="{fill_color}" stroke="{stroke_color}" stroke-width="{stroke_width}" />'


def draw_legend(legend_items, legend_x, legend_y, font_size=14, border_color="#000000"):
    """
    Draws the legend on the image.
    
    legend_items: List of tuples (label, color) for each legend item.
    legend_x: The starting x-coordinate for the legend.
    legend_y: The y-coordinate for the legend.
    font_size: The font size for the legend text.
    border_color: The color for the borders in the legend.
    """
    legend = ""
    for label, color in legend_items:
        legend += (
            f'<rect x="{legend_x}" y="{legend_y}" width="20" height="20" fill="{color}" stroke="{border_color}" stroke-width="2" />'
            f'<text x="{legend_x + 25}" y="{legend_y + 15}" font-size="{font_size}" font-family="sans-serif">{label}</text>'
        )
        legend_x += 160
    return legend


def generate_seat_bar(
    total_votes=37000,
    votes_per_seat=10000,
    output_basename="seats-and-remainder"
):
    # === Main logic ===
    seats = total_votes // votes_per_seat
    remainder_votes = total_votes % votes_per_seat
    votes_to_next = votes_per_seat - remainder_votes if remainder_votes > 0 else 0

    # === Dimensions and layout ===
    margin = 40
    annotation_height = 40
    bar_height = 40
    legend_height = 60
    total_bar_width = 600

    svg_width = total_bar_width + 2 * margin
    svg_height = margin + annotation_height + bar_height + legend_height + margin

    # === Colors ===
    seat_color = "#4F81BD"         # Medium blue
    remainder_color = "#FF6F00"    # Strong orange
    missing_color = "transparent"  # Transparent background
    border_color = "#000000"
    stroke_width = 2
    font_size = 14

    # === Width calculations ===
    seat_width = total_bar_width / (seats + 1)
    remainder_width = seat_width * (remainder_votes / votes_per_seat)
    missing_width = seat_width * (votes_to_next / votes_per_seat)

    # === Vertical positions ===
    bar_y = margin + annotation_height
    legend_y = bar_y + bar_height + 30
    votes_y = margin + annotation_height - 10  # For the annotations above the bar

    # === Key horizontal coordinates ===
    votes_x = seat_width * seats + remainder_width
    cut_x = seat_width
    next_seat_x = seat_width * (seats + 1)

    # === Construct SVG header ===
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{svg_width}" height="{svg_height}" xmlns="http://www.w3.org/2000/svg">
  <g transform="translate({margin}, 0)">
'''

    # === Draw the bar segments ===
    current_x = 0
    bar_segments = ""
    for _ in range(seats):
        bar_segments += draw_bar_segment(current_x, bar_y, seat_width, bar_height, seat_color, border_color, stroke_width)
        current_x += seat_width

    if remainder_votes > 0:
        bar_segments += draw_bar_segment(current_x, bar_y, remainder_width, bar_height, remainder_color, border_color, stroke_width)
        current_x += remainder_width

    if missing_width > 0:
        bar_segments += draw_bar_segment(current_x, bar_y, missing_width, bar_height, missing_color, border_color, stroke_width)

    # === Annotations ===
    annotations = ""

    # Price of cutoff (above left)
    annotations += draw_annotation(cut_x, votes_y, cut_x, bar_y, cut_x - 40, votes_y - 20, "Precio de corte")

    # Votes (above right)
    if remainder_votes > 0:
        annotations += draw_annotation(votes_x, votes_y, votes_x, bar_y, votes_x + 40, votes_y - 20, "Votos")

    # Next seat (below the bar)
    next_seat_y_top = bar_y + bar_height
    next_seat_y_label = next_seat_y_top + 10
    annotations += draw_annotation(next_seat_x, next_seat_y_top, next_seat_x, next_seat_y_top + 10, next_seat_x - 40, next_seat_y_label + 20, "Siguiente escaño")

    # === Legend ===
    legend_items = [("Escaños", seat_color), ("Restos", remainder_color)]
    legend = draw_legend(legend_items, 0, legend_y, font_size, border_color)

    # === Combine all SVG parts ===
    svg += bar_segments  # Add bar segments
    svg += annotations    # Add annotations
    svg += legend         # Add legend

    svg += "\n</g>\n</svg>"

    # === Save files ===
    svg_file = f"{output_basename}.svg"
    pdf_file = f"{output_basename}.pdf"
    png_file = f"{output_basename}.png"

    with open(svg_file, "w") as file:
        file.write(svg)

    cairosvg.svg2pdf(url=svg_file, write_to=pdf_file)
    cairosvg.svg2png(url=svg_file, write_to=png_file)

    print("Files generated:")
    print(f" - {svg_file}")
    print(f" - {pdf_file}")
    print(f" - {png_file}")

if __name__ == "__main__":
    generate_seat_bar()


bla
#!/usr/bin/env python3
import cairosvg

def draw_annotation(x1, y1, x2, y2, label_x, label_y, label_text, font_size=14, label_offset=20, border_color="#000000"):
    """
    Draws an annotation with an oblique line and a label.
    
    x1, y1: Starting coordinates of the vertical line.
    x2, y2: Ending coordinates of the vertical line on the bar.
    label_x, label_y: Position of the label.
    label_text: The text of the label.
    font_size: Font size for the label (optional).
    label_offset: Offset for the label (optional).
    border_color: Color of the line for the annotation.
    """
    # Calculate the oblique line coordinates to make the line slanted
    oblique_x2 = x2 + (x2 - x1) * 0.4  # Shift oblique line for an angle
    oblique_y2 = y2 - (y2 - y1) * 0.4  # Similarly shift in the y direction for the oblique angle

    # Draw the oblique line
    annotation = (
        f'<line x1="{x1}" y1="{y1}" x2="{oblique_x2}" y2="{oblique_y2}" stroke="{border_color}" stroke-width="1"/>'
        f'<line x1="{oblique_x2}" y1="{oblique_y2}" x2="{x2}" y2="{y2}" stroke="{border_color}" stroke-width="1"/>'
        f'<text x="{label_x}" y="{label_y}" font-size="{font_size}" font-family="sans-serif" text-anchor="middle">{label_text}</text>'
    )
    return annotation


def draw_annotation(x1, y1, x2, y2, label_x, label_y, label_text, font_size=14, label_offset=20, border_color="#000000"):
    """
    Draws an annotation with an oblique line and a label using an SVG path.

    x1, y1: Starting coordinates of the vertical line.
    x2, y2: Ending coordinates of the vertical line on the bar.
    label_x, label_y: Position of the label.
    label_text: The text of the label.
    font_size: Font size for the label (optional).
    label_offset: Offset for the label (optional).
    border_color: Color of the line for the annotation.
    """
    mid_y = (y1 + y2) / 2  # Midpoint in Y
    oblique_x1 = x1  # Same X as the start point
    oblique_y1 = y1  # Same Y as the start point

    # First segment: move vertically in Y
    first_segment = f'<line x1="{oblique_x1}" y1="{oblique_y1}" x2="{oblique_x1}" y2="{mid_y}" stroke="{border_color}" stroke-width="1"/>'

    # Second segment: move from the midpoint in both X and Y to the final point
    second_segment = f'<line x1="{oblique_x1}" y1="{mid_y}" x2="{x2}" y2="{y2}" stroke="{border_color}" stroke-width="1"/>'

    # Combine the two segments
    annotation = (
        first_segment +
        second_segment +
        f'<text x="{label_x}" y="{label_y}" font-size="{font_size}" font-family="sans-serif" text-anchor="middle">{label_text}</text>'
    )
    return annotation

def draw_bar_segment(current_x, y, width, height, fill_color, stroke_color="#000000", stroke_width=2):
    """
    Draws a single bar segment.
    
    current_x: The x-coordinate where the segment starts.
    y: The y-coordinate of the bar.
    width: The width of the segment.
    height: The height of the segment.
    fill_color: The color to fill the segment with.
    stroke_color: The color of the border of the segment.
    stroke_width: The width of the border.
    """
    return f'<rect x="{current_x}" y="{y}" width="{width}" height="{height}" fill="{fill_color}" stroke="{stroke_color}" stroke-width="{stroke_width}" />'


def draw_legend(legend_items, legend_x, legend_y, font_size=14, border_color="#000000"):
    """
    Draws the legend on the image.
    
    legend_items: List of tuples (label, color) for each legend item.
    legend_x: The starting x-coordinate for the legend.
    legend_y: The y-coordinate for the legend.
    font_size: The font size for the legend text.
    border_color: The color for the borders in the legend.
    """
    legend = ""
    for label, color in legend_items:
        legend += (
            f'<rect x="{legend_x}" y="{legend_y}" width="20" height="20" fill="{color}" stroke="{border_color}" stroke-width="2" />'
            f'<text x="{legend_x + 25}" y="{legend_y + 15}" font-size="{font_size}" font-family="sans-serif">{label}</text>'
        )
        legend_x += 160
    return legend


def generate_seat_bar(
    total_votes=37000,
    votes_per_seat=10000,
    output_basename="seats-and-remainder"
):
    # === Main logic ===
    seats = total_votes // votes_per_seat
    remainder_votes = total_votes % votes_per_seat
    votes_to_next = votes_per_seat - remainder_votes if remainder_votes > 0 else 0

    # === Dimensions and layout ===
    margin = 40
    annotation_height = 40
    bar_height = 40
    legend_height = 60
    total_bar_width = 600

    svg_width = total_bar_width + 2 * margin
    svg_height = margin + annotation_height + bar_height + legend_height + margin

    # === Colors ===
    seat_color = "#4F81BD"         # Medium blue
    remainder_color = "#FF6F00"    # Strong orange
    missing_color = "transparent"  # Transparent background
    border_color = "#000000"
    stroke_width = 2
    font_size = 14

    # === Width calculations ===
    seat_width = total_bar_width / (seats + 1)
    remainder_width = seat_width * (remainder_votes / votes_per_seat)
    missing_width = seat_width * (votes_to_next / votes_per_seat)

    # === Vertical positions ===
    bar_y = margin + annotation_height
    legend_y = bar_y + bar_height + 30
    votes_y = margin + annotation_height - 10  # For the annotations above the bar

    # === Key horizontal coordinates ===
    votes_x = seat_width * seats + remainder_width
    cut_x = seat_width
    next_seat_x = seat_width * (seats + 1)

    # === Construct SVG header ===
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{svg_width}" height="{svg_height}" xmlns="http://www.w3.org/2000/svg">
  <g transform="translate({margin}, 0)">
'''

    # === Draw the bar segments ===
    current_x = 0
    bar_segments = ""
    for _ in range(seats):
        bar_segments += draw_bar_segment(current_x, bar_y, seat_width, bar_height, seat_color, border_color, stroke_width)
        current_x += seat_width

    if remainder_votes > 0:
        bar_segments += draw_bar_segment(current_x, bar_y, remainder_width, bar_height, remainder_color, border_color, stroke_width)
        current_x += remainder_width

    if missing_width > 0:
        bar_segments += draw_bar_segment(current_x, bar_y, missing_width, bar_height, missing_color, border_color, stroke_width)

    # === Annotations ===
    annotations = ""

    # Price of cutoff (above left)
    annotations += draw_annotation(cut_x, votes_y, cut_x, bar_y, cut_x - 40, votes_y - 20, "Precio de corte")

    # Votes (above right)
    if remainder_votes > 0:
        annotations += draw_annotation(votes_x, votes_y, votes_x, bar_y, votes_x + 40, votes_y - 20, "Votos")

    # Next seat (below the bar)
    next_seat_y_top = bar_y + bar_height
    next_seat_y_label = next_seat_y_top + 10
    annotations += draw_annotation(next_seat_x, next_seat_y_top, next_seat_x, next_seat_y_top + 10, next_seat_x - 40, next_seat_y_label + 20, "Siguiente escaño")

    # === Legend ===
    legend_items = [("Escaños", seat_color), ("Restos", remainder_color)]
    legend = draw_legend(legend_items, 0, legend_y, font_size, border_color)

    # === Combine all SVG parts ===
    svg += bar_segments  # Add bar segments
    svg += annotations    # Add annotations
    #svg += block_annotations  # Add block annotations
    svg += legend         # Add legend

    svg += "\n</g>\n</svg>"

    # === Save files ===
    svg_file = f"{output_basename}.svg"
    pdf_file = f"{output_basename}.pdf"
    png_file = f"{output_basename}.png"

    with open(svg_file, "w") as file:
        file.write(svg)

    cairosvg.svg2pdf(url=svg_file, write_to=pdf_file)
    cairosvg.svg2png(url=svg_file, write_to=png_file)

    print("Files generated:")
    print(f" - {svg_file}")
    print(f" - {pdf_file}")
    print(f" - {png_file}")


if __name__ == "__main__":
    generate_seat_bar()

bla


#!/usr/bin/env python3
import cairosvg

def draw_annotation(x1, y1, x2, y2, label_x, label_y, label_text, font_size=14, label_offset=20, border_color="#000000"):
    """
    Draws an annotation with an oblique line and a label.
    
    x1, y1: Starting coordinates of the vertical line.
    x2, y2: Ending coordinates of the vertical line on the bar.
    label_x, label_y: Position of the label.
    label_text: The text of the label.
    font_size: Font size for the label (optional).
    label_offset: Offset for the label (optional).
    border_color: Color of the line for the annotation.
    """
    # Calculating the oblique line coordinates
    oblique_x2 = x2 + (x2 - x1) * 0.4  # Shift oblique line for an angle
    oblique_y2 = y2 - (y2 - y1) * 0.4  # Similarly shift in the y direction for the oblique angle

    # Draw the oblique line
    annotation = (
        f'<line x1="{x1}" y1="{y1}" x2="{oblique_x2}" y2="{oblique_y2}" stroke="{border_color}" stroke-width="1"/>'
        f'<line x1="{oblique_x2}" y1="{oblique_y2}" x2="{x2}" y2="{y2}" stroke="{border_color}" stroke-width="1"/>'
        f'<text x="{label_x}" y="{label_y}" font-size="{font_size}" font-family="sans-serif" text-anchor="middle">{label_text}</text>'
    )
    return annotation


def draw_bar_segment(current_x, y, width, height, fill_color, stroke_color="#000000", stroke_width=2):
    """
    Draws a single bar segment.
    
    current_x: The x-coordinate where the segment starts.
    y: The y-coordinate of the bar.
    width: The width of the segment.
    height: The height of the segment.
    fill_color: The color to fill the segment with.
    stroke_color: The color of the border of the segment.
    stroke_width: The width of the border.
    """
    return f'<rect x="{current_x}" y="{y}" width="{width}" height="{height}" fill="{fill_color}" stroke="{stroke_color}" stroke-width="{stroke_width}" />'


def draw_legend(legend_items, legend_x, legend_y, font_size=14, border_color="#000000"):
    """
    Draws the legend on the image.
    
    legend_items: List of tuples (label, color) for each legend item.
    legend_x: The starting x-coordinate for the legend.
    legend_y: The y-coordinate for the legend.
    font_size: The font size for the legend text.
    border_color: The color for the borders in the legend.
    """
    legend = ""
    for label, color in legend_items:
        legend += (
            f'<rect x="{legend_x}" y="{legend_y}" width="20" height="20" fill="{color}" stroke="{border_color}" stroke-width="2" />'
            f'<text x="{legend_x + 25}" y="{legend_y + 15}" font-size="{font_size}" font-family="sans-serif">{label}</text>'
        )
        legend_x += 160
    return legend


def generate_seat_bar(
    total_votes=37000,
    votes_per_seat=10000,
    output_basename="seats-and-remainder"
):
    # === Main logic ===
    seats = total_votes // votes_per_seat
    remainder_votes = total_votes % votes_per_seat
    votes_to_next = votes_per_seat - remainder_votes if remainder_votes > 0 else 0

    # === Dimensions and layout ===
    margin = 40
    annotation_height = 40
    bar_height = 40
    legend_height = 60
    total_bar_width = 600

    svg_width = total_bar_width + 2 * margin
    svg_height = margin + annotation_height + bar_height + legend_height + margin

    # === Colors ===
    seat_color = "#4F81BD"         # Medium blue
    remainder_color = "#FF6F00"    # Strong orange
    missing_color = "transparent"  # Transparent background
    border_color = "#000000"
    stroke_width = 2
    font_size = 14

    # === Width calculations ===
    seat_width = total_bar_width / (seats + 1)
    remainder_width = seat_width * (remainder_votes / votes_per_seat)
    missing_width = seat_width * (votes_to_next / votes_per_seat)

    # === Vertical positions ===
    bar_y = margin + annotation_height
    legend_y = bar_y + bar_height + 30
    votes_y = margin + annotation_height - 10  # For the annotations above the bar

    # === Key horizontal coordinates ===
    votes_x = seat_width * seats + remainder_width
    cut_x = seat_width
    next_seat_x = seat_width * (seats + 1)

    # === Construct SVG header ===
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{svg_width}" height="{svg_height}" xmlns="http://www.w3.org/2000/svg">
  <g transform="translate({margin}, 0)">
'''

    # === Draw the bar segments ===
    current_x = 0
    bar_segments = ""
    for _ in range(seats):
        bar_segments += draw_bar_segment(current_x, bar_y, seat_width, bar_height, seat_color, border_color, stroke_width)
        current_x += seat_width

    if remainder_votes > 0:
        bar_segments += draw_bar_segment(current_x, bar_y, remainder_width, bar_height, remainder_color, border_color, stroke_width)
        current_x += remainder_width

    if missing_width > 0:
        bar_segments += draw_bar_segment(current_x, bar_y, missing_width, bar_height, missing_color, border_color, stroke_width)

    # === Annotations ===
    annotations = ""

    # Price of cutoff (above left)
    annotations += draw_annotation(cut_x, votes_y, cut_x, bar_y, cut_x - 40, votes_y - 20, "Precio de corte")

    # Votes (above right)
    if remainder_votes > 0:
        annotations += draw_annotation(votes_x, votes_y, votes_x, bar_y, votes_x + 40, votes_y - 20, "Votos")

    # Next seat (below the bar)
    next_seat_y_top = bar_y + bar_height
    next_seat_y_label = next_seat_y_top + 10
    annotations += draw_annotation(next_seat_x, next_seat_y_top, next_seat_x, next_seat_y_top + 10, next_seat_x - 40, next_seat_y_label + 20, "Siguiente escaño")

    # === Block Annotations ===
    block_annotations = ""

    # Escaños: Annotations for seats, pointing to the center of each segment
    for i in range(seats):
        block_annotations += draw_annotation(current_x - seat_width + (seat_width / 2), bar_y, current_x - seat_width + (seat_width / 2), bar_y + bar_height,
                                              current_x - seat_width + (seat_width / 2), bar_y + bar_height + 20, "Escaños")

    # Restos: Annotation for remainder
    if remainder_votes > 0:
        block_annotations += draw_annotation(current_x - remainder_width + (remainder_width / 2), bar_y, current_x - remainder_width + (remainder_width / 2), bar_y + bar_height,
                                              current_x - remainder_width + (remainder_width / 2), bar_y + bar_height + 20, "Restos")

    # === Legend ===
    legend_items = [("Escaños", seat_color), ("Restos", remainder_color)]
    legend = draw_legend(legend_items, 0, legend_y, font_size, border_color)

    # === Combine all SVG parts ===
    svg += bar_segments  # Add bar segments
    svg += annotations    # Add annotations
    svg += block_annotations  # Add block annotations
    svg += legend         # Add legend

    svg += "\n</g>\n</svg>"

    # === Save files ===
    svg_file = f"{output_basename}.svg"
    pdf_file = f"{output_basename}.pdf"
    png_file = f"{output_basename}.png"

    with open(svg_file, "w") as file:
        file.write(svg)

    cairosvg.svg2pdf(url=svg_file, write_to=pdf_file)
    cairosvg.svg2png(url=svg_file, write_to=png_file)

    print("Files generated:")
    print(f" - {svg_file}")
    print(f" - {pdf_file}")
    print(f" - {png_file}")

if __name__ == "__main__":
    generate_seat_bar()

bla

#!/usr/bin/env python3
import cairosvg

def draw_annotation(x1, y1, x2, y2, label_x, label_y, label_text, font_size=14, label_offset=20, border_color="#000000"):
    """
    Draws an annotation with an oblique line and a label.
    
    x1, y1: Starting coordinates of the vertical line.
    x2, y2: Ending coordinates of the vertical line on the bar.
    label_x, label_y: Position of the label.
    label_text: The text of the label.
    font_size: Font size for the label (optional).
    label_offset: Offset for the label (optional).
    border_color: Color of the line for the annotation.
    """
    # Calculating the oblique line coordinates
    oblique_x2 = x2 + (x2 - x1) * 0.4  # Shift oblique line for an angle
    oblique_y2 = y2 - (y2 - y1) * 0.4  # Similarly shift in the y direction for the oblique angle

    # Draw the oblique line
    annotation = (
        f'<line x1="{x1}" y1="{y1}" x2="{oblique_x2}" y2="{oblique_y2}" stroke="{border_color}" stroke-width="1"/>'
        f'<line x1="{oblique_x2}" y1="{oblique_y2}" x2="{x2}" y2="{y2}" stroke="{border_color}" stroke-width="1"/>'
        f'<text x="{label_x}" y="{label_y}" font-size="{font_size}" font-family="sans-serif" text-anchor="middle">{label_text}</text>'
    )
    return annotation


def draw_bar_segment(current_x, y, width, height, fill_color, stroke_color="#000000", stroke_width=2):
    """
    Draws a single bar segment.
    
    current_x: The x-coordinate where the segment starts.
    y: The y-coordinate of the bar.
    width: The width of the segment.
    height: The height of the segment.
    fill_color: The color to fill the segment with.
    stroke_color: The color of the border of the segment.
    stroke_width: The width of the border.
    """
    return f'<rect x="{current_x}" y="{y}" width="{width}" height="{height}" fill="{fill_color}" stroke="{stroke_color}" stroke-width="{stroke_width}" />'


def draw_legend(legend_items, legend_x, legend_y, font_size=14, border_color="#000000"):
    """
    Draws the legend on the image.
    
    legend_items: List of tuples (label, color) for each legend item.
    legend_x: The starting x-coordinate for the legend.
    legend_y: The y-coordinate for the legend.
    font_size: The font size for the legend text.
    border_color: The color for the borders in the legend.
    """
    legend = ""
    for label, color in legend_items:
        legend += (
            f'<rect x="{legend_x}" y="{legend_y}" width="20" height="20" fill="{color}" stroke="{border_color}" stroke-width="2" />'
            f'<text x="{legend_x + 25}" y="{legend_y + 15}" font-size="{font_size}" font-family="sans-serif">{label}</text>'
        )
        legend_x += 160
    return legend


def generate_seat_bar(
    total_votes=37000,
    votes_per_seat=10000,
    output_basename="seats-and-remainder"
):
    # === Main logic ===
    seats = total_votes // votes_per_seat
    remainder_votes = total_votes % votes_per_seat
    votes_to_next = votes_per_seat - remainder_votes if remainder_votes > 0 else 0

    # === Dimensions and layout ===
    margin = 40
    annotation_height = 40
    bar_height = 40
    legend_height = 60
    total_bar_width = 600

    svg_width = total_bar_width + 2 * margin
    svg_height = margin + annotation_height + bar_height + legend_height + margin

    # === Colors ===
    seat_color = "#4F81BD"         # Medium blue
    remainder_color = "#FF6F00"    # Strong orange
    missing_color = "transparent"  # Transparent background
    border_color = "#000000"
    stroke_width = 2
    font_size = 14

    # === Width calculations ===
    seat_width = total_bar_width / (seats + 1)
    remainder_width = seat_width * (remainder_votes / votes_per_seat)
    missing_width = seat_width * (votes_to_next / votes_per_seat)

    # === Vertical positions ===
    bar_y = margin + annotation_height
    legend_y = bar_y + bar_height + 30
    votes_y = margin + annotation_height - 10  # For the annotations above the bar

    # === Key horizontal coordinates ===
    votes_x = seat_width * seats + remainder_width
    cut_x = seat_width
    next_seat_x = seat_width * (seats + 1)

    # === Construct SVG header ===
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{svg_width}" height="{svg_height}" xmlns="http://www.w3.org/2000/svg">
  <g transform="translate({margin}, 0)">
'''

    # === Draw the bar segments ===
    current_x = 0
    bar_segments = ""
    for _ in range(seats):
        bar_segments += draw_bar_segment(current_x, bar_y, seat_width, bar_height, seat_color, border_color, stroke_width)
        current_x += seat_width

    if remainder_votes > 0:
        bar_segments += draw_bar_segment(current_x, bar_y, remainder_width, bar_height, remainder_color, border_color, stroke_width)
        current_x += remainder_width

    if missing_width > 0:
        bar_segments += draw_bar_segment(current_x, bar_y, missing_width, bar_height, missing_color, border_color, stroke_width)

    # === Annotations ===
    annotations = ""

    # Price of cutoff (above left)
    annotations += draw_annotation(cut_x, votes_y, cut_x, bar_y, cut_x - 40, votes_y - 20, "Precio de corte")

    # Votes (above right)
    if remainder_votes > 0:
        annotations += draw_annotation(votes_x, votes_y, votes_x, bar_y, votes_x + 40, votes_y - 20, "Votos")

    # Next seat (below the bar)
    next_seat_y_top = bar_y + bar_height
    next_seat_y_label = next_seat_y_top + 10
    annotations += draw_annotation(next_seat_x, next_seat_y_top, next_seat_x, next_seat_y_top + 10, next_seat_x - 40, next_seat_y_label + 20, "Siguiente escaño")

    # === Legend ===
    legend_items = [("Escaños", seat_color), ("Restos", remainder_color)]
    legend = draw_legend(legend_items, 0, legend_y, font_size, border_color)

    # === Combine all SVG parts ===
    svg += bar_segments  # Add bar segments
    svg += annotations    # Add annotations
    svg += legend         # Add legend

    svg += "\n</g>\n</svg>"

    # === Save files ===
    svg_file = f"{output_basename}.svg"
    pdf_file = f"{output_basename}.pdf"
    png_file = f"{output_basename}.png"

    with open(svg_file, "w") as file:
        file.write(svg)

    cairosvg.svg2pdf(url=svg_file, write_to=pdf_file)
    cairosvg.svg2png(url=svg_file, write_to=png_file)

    print("Files generated:")
    print(f" - {svg_file}")
    print(f" - {pdf_file}")
    print(f" - {png_file}")

if __name__ == "__main__":
    generate_seat_bar()

