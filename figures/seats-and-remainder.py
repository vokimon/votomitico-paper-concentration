from svgtools import *


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
