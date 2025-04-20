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
