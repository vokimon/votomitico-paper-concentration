import colour
import cairosvg


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


def generate_seat_bar(
    votes=648,
    votes_per_seat=120,
    output_basename="seats-and-remainder"
):
    seats = votes // votes_per_seat
    remainder_votes = votes % votes_per_seat

    seat_color = "#4F81BD"
    remainder_color = "#F3A322"
    missing_color = "transparent"
    border_color = "#000000"

    margin = 20
    annotation_height = 30
    bar_height = 40
    legend_height = 30
    bar_width = 600
    svg_width = margin + bar_width + 2 * margin
    svg_height = margin + annotation_height + bar_height + legend_height + margin
    stroke_width = 2
    font_size = 14
    seat_width = bar_width / (seats + 1)
    remainder_width = seat_width * (remainder_votes / votes_per_seat)
    bar_y = margin + annotation_height
    legend_y = bar_y + bar_height + 30
    votes_x = margin + seat_width * seats + remainder_width
    cut_x = margin + seat_width

    svg = ""
    # border (debug)
    #svg += draw_bar_segment(0, 0, svg_width, svg_height, "beige", 10)

    current_x = margin

    svg += draw_bar_segment(
        current_x,
        bar_y,
        bar_width,
        bar_height,
        missing_color,
    )
    for _ in range(seats):
        svg += draw_bar_segment(
            current_x,
            bar_y,
            seat_width,
            bar_height,
            seat_color,
        )
        current_x += seat_width
    if remainder_votes > 0:
        svg += draw_bar_segment(
            current_x,
            bar_y,
            remainder_width,
            bar_height,
            remainder_color,
        )
        current_x += remainder_width

    svg += draw_annotation(
        f"Precio de corte ({spnum(votes_per_seat)})",
        cut_x, bar_y , cut_x + 20, legend_y, "top", "left"
    )
    svg += draw_annotation(
        f"Restos ({spnum(remainder_votes)})",
        margin + seat_width * seats + remainder_width / 2,
        bar_y + bar_height / 2,
        margin + seat_width * seats + remainder_width / 2 - 20,
        legend_y,
        "top", "right"
    )
    svg += draw_text(
        margin, bar_y - 25,
        f"Votos a la candidatura ({spnum(votes)})",
        "left", "bottom", 
    )
    next_seat_y_top = bar_y + bar_height
    next_seat_y_label = next_seat_y_top + 10
    for i in range(seats+2):
        svg += draw_annotation(
            f"{i}",
            margin + seat_width * i,
            bar_y + bar_height,
            margin + seat_width * i,
            bar_y + bar_height + 5,
            "top",
            "center",
        )
        svg += draw_annotation(
            f"{spnum(i*votes_per_seat)}",
            margin + seat_width * i,
            bar_y,
            margin + seat_width * i,
            bar_y - 5,
            "bottom",
            "center",
        )
    legend_items = [("Votos que consiguen escaño", seat_color), ("Restos", remainder_color)]
    #svg += draw_legend(legend_items, svg_width/2, legend_y, font_size, border_color)
    svg += draw_text(margin, bar_y + bar_height + 20 , f"Escaños ({spnum(seats)})", "left", "top")

    dump_image(svg, output_basename, svg_width, svg_height)


def dump_image(content, output_basename, width, height):
    svg = (
        f'<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">\n'
        + content +
        "</svg>"
    )

    svg_file = f"{output_basename}.svg"
    pdf_file = f"{output_basename}.pdf"
    png_file = f"{output_basename}.png"

    with open(svg_file, "w") as f:
        f.write(svg)
    cairosvg.svg2pdf(url=svg_file, write_to=pdf_file)
    cairosvg.svg2png(url=svg_file, write_to=png_file)

    print("Files generated:")
    print(f" - {svg_file}")
    print(f" - {pdf_file}")
    print(f" - {png_file}")


def generate_seat_cost(
    seats=5,
    output_basename="seat-cost",
):
    seat_color = "#4F81BD"
    first_seat_color = darken(seat_color)
    missing_color = "transparent"
    border_color = "#000000"

    margin = 20
    bar_height = 40
    bar_width = 600
    bar_gap = 10
    svg_width = margin + bar_width + margin
    svg_height = margin + seats * (bar_height + bar_gap) + margin
    stroke_width = 2
    font_size = 14
    seat_width = bar_width / (seats + 1)
    bar_y = margin

    svg = ""
    # border (debug)
    #svg += draw_bar_segment(0, 0, svg_width, svg_height, "beige", 10)
    for i in range(seats):
        price = bar_width/(i+1)
        for j in range(i+1):
            svg += draw_bar_segment(
                margin + j * price,
                bar_y + i * (bar_height+bar_gap),
                price,
                bar_height,
                seat_color,
            )
        svg += draw_bar_segment(
            margin,
            bar_y + i * (bar_height+bar_gap),
            price,
            bar_height,
            first_seat_color,
        )
        svg += draw_text(
            margin + price /2,
            bar_y + i * (bar_height+bar_gap) + bar_height/2,
            f"Vi / {i+1}",
            "center", "center",
            color="white"
        )
    dump_image(svg, "seat-costs", svg_width, svg_height)

if __name__ == "__main__":
    generate_seat_bar()
    generate_seat_cost()
