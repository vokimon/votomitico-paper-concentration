
import svgwrite
import cairosvg

class LinearScale:
    def __init__(self, domain_min, domain_max, canvas_min, canvas_max):
        self.domain_min = domain_min
        self.domain_max = domain_max
        self.canvas_min = canvas_min
        self.canvas_max = canvas_max

    def __call__(self, value):
        return self.canvas_min + (
            (value - self.domain_min) / (self.domain_max - self.domain_min)
        ) * (self.canvas_max - self.canvas_min)

    def inverse(self):
        return LinearScale(canvas_min, canvas_max, domain_min, domain_max)

def draw_axis_labels(dwg, x_scale, y_scale, step_pct):
    for pct in range(0, 101, int(step_pct)):
        x = x_scale(pct)
        y = y_scale.canvas_min + 15
        dwg.add(
            dwg.text(
                f"{pct}%",
                insert=(x, y),
                font_size="10px",
                text_anchor="middle",
            )
        )

def draw_plot_labels(dwg, width, height, title, x_label, y_label):
    dwg.add(
        dwg.text(
            x_label,
            insert=(width // 2, height - 5),
            font_size="12px",
            text_anchor="middle",
        )
    )

    dwg.add(
        dwg.text(
            y_label,
            insert=(10, height//2),
            transform=f"rotate(-90, 10, {height//2})",
            font_size="12px",
            text_anchor="middle",
        )
    )

    dwg.add(
        dwg.text(
            title,
            insert=(width // 2, margin // 2),
            font_size="14px",
            text_anchor="middle",
            font_weight="bold",
        )
    )

def draw_line(dwg, x_scale, y_scale, x_vals, y_vals, stroke_color, dashed=False, stroke_width=2):
    points = list(zip(map(x_scale,x_vals), map(y_scale,y_vals)))
    style = {
        "stroke": stroke_color,
        "stroke_width": stroke_width,
        "fill": "none",
    }
    if dashed:
        style["stroke_dasharray"] = "6,4"
    polyline = dwg.polyline(points, **style)
    clip_id = "plot_area_clip"
    group = dwg.g(clip_path=f"url(#{clip_id})")
    group.add(polyline)
    dwg.add(group)

def label_line(dwg, x_scale, y_scale, x, y, text, color, dx=0, dy=0, font_weight="normal", anchor="start"):
    dwg.add(
        dwg.text(
            text,
            insert=(x_scale(x) + dx, y_scale(y) + dy),
            font_size="10px",
            fill=color,
            font_weight=font_weight,
            text_anchor=anchor,
        )
    )

def cutting_price(pc, pd, eab, vab):
    points = (
        ([
            (e*pc, pc)
            for e in range(eab+1)
        ] + [
            (vab - pc*e, pc)
            for e in range(eab+1)
        ] if pc<vab/eab else [
            (e*vab/eab, vab/eab)
            for e in range(eab+1)
        ]) + ([
            (vab - pd*e, pd)
            for e in range(1, eab+1)
        ] + [
            (e*pd, pd)
            for e in range(1, eab+1)
        ] if pd>vab/(eab+1) else [
            (e*vab/(eab+1), vab/(eab+1))
            for e in range(1, eab+1)
        ])
    )
    points.sort()
    return zip(*points)

def clip_path(dwg, clip_id, x_scale, y_scale):
    clip_path = dwg.defs.add(dwg.clipPath(id=clip_id))
    clip_path.add(dwg.rect(
        insert=(  # top-left corner of the plot
            min(x_scale.canvas_min, x_scale.canvas_max),
            min(y_scale.canvas_min, y_scale.canvas_max),
        ),
        size=(
            abs(x_scale.canvas_max - x_scale.canvas_min),
            abs(y_scale.canvas_max - y_scale.canvas_min),
        ),
    ))

def plot_canvas(dwg, x_scale, y_scale):
    clip_path(
        dwg,
        clip_id = "plot_area_clip",
        x_scale = x_scale,
        y_scale = y_scale,
    )
    dwg.add(dwg.line((x_scale.canvas_min, y_scale.canvas_min), (x_scale.canvas_max, y_scale.canvas_min), stroke="black"))
    dwg.add(dwg.line((x_scale.canvas_max, y_scale.canvas_min), (x_scale.canvas_max, y_scale.canvas_max), stroke="black"))
    dwg.add(dwg.line((x_scale.canvas_min, y_scale.canvas_min), (x_scale.canvas_min, y_scale.canvas_max), stroke="black"))
    draw_axis_labels(dwg, x_scale, y_scale, step_pct=10)

def generate_transfer_space_results(
    Vab,
    width,
    height,
    margin,
    basename,
    title,
    Fc=0.2,
    Fd=0.6,
    Eab=4,
    y_low=0.0,
    y_top=1.0,
    show_price=True,
):
    output_svg = f"{basename}.svg"
    output_png = f"{basename}.png"
    output_pdf = f"{basename}.pdf"

    dwg = svgwrite.Drawing(output_svg, size=(width, height))

    x_scale = LinearScale(0, 100, margin, width - margin)
    y_scale = LinearScale(Vab * y_low, Vab * y_top, height - margin, margin)

    plot_canvas(dwg, x_scale, y_scale)

    higher_e = int(1/y_low) if y_low > 1.0/16 else Eab +1
    x_vals = [0, 100]
    va_div = {j:[0, Vab/j] for j in range(1, Eab+1)}
    vb_div = {j:[Vab/j, 0] for j in range(1, Eab+1)}
    Pmax = Vab / (Eab + Fc)
    Pmin = Vab / (Eab + Fc + Fd)
    pc_vals = [Pmax, Pmax]
    pd_vals = [Pmin, Pmin]
    x_price, y_price = cutting_price(Pmax, Pmin, Eab, Vab)

    def result_block(start, size, text, stroke, fill):
        if not size: return
        dwg.add(dwg.rect(
            insert=(
                x_scale(start),
                y_scale.canvas_max,
            ),
            size=(
                x_scale(size)-x_scale(0),
                abs(y_scale.canvas_max - y_scale.canvas_min),
            ),
            fill=fill,
            stroke=stroke,
            stroke_width="2px",
            #opacity=0.4,
        ))
        for i, line in enumerate(text.splitlines()):
            dwg.add(dwg.text(
                line,
                insert=(
                    x_scale(start + size/2),
                    (y_scale.canvas_max + y_scale.canvas_min)/2 + i*12 - 24,
                ),
                font_size="10px",
                text_anchor="middle",
                fill="#fff",
            ))

    block_size = Vab - Eab * Pmin
    inter_size = Pmin * (Eab + 1) - Vab

    for k in range(0, Eab+1):
        result_block(
            start=k*(block_size + inter_size),
            size=block_size,
            text=f"Ea={k}\nEb={Eab-k}\n\nEa+Eb={Eab}",
            fill="#484",
            stroke="#444",
        )
    for k in range(0, Eab):
        result_block(
            start=block_size + k*(block_size + inter_size),
            size=inter_size,
            text=f"Ea={k}\nEb={Eab-k-1}\n\nEa+Eb={Eab-1}",
            fill="#e77",
            stroke="#444",
        )

    draw_plot_labels(
        dwg, width, height,
        title = title,
        x_label = "Concentración del voto A-B en A (%)",
        y_label = "",
    )

    dwg.save()
    cairosvg.svg2png(url=output_svg, write_to=output_png)
    cairosvg.svg2pdf(url=output_svg, write_to=output_pdf)


def generate_transfer_space_price(
    Vab,
    width,
    height,
    margin,
    basename,
    title,
    Fc=0.2,
    Fd=0.6,
    Eab=4,
    y_low=0.0,
    y_top=1.0,
    show_price=True,
):
    output_svg = f"{basename}.svg"
    output_png = f"{basename}.png"
    output_pdf = f"{basename}.pdf"

    dwg = svgwrite.Drawing(output_svg, size=(width, height))

    x_scale = LinearScale(0, 100, margin, width - margin)
    y_scale = LinearScale(Vab * y_low, Vab * y_top, height - margin, margin)

    plot_canvas(dwg, x_scale, y_scale)

    higher_e = int(1/y_low) if y_low > 1.0/16 else Eab +1
    x_vals = [0, 100]
    va_div = {j:[0, Vab/j] for j in range(1, Eab+1)}
    vb_div = {j:[Vab/j, 0] for j in range(1, Eab+1)}
    Pmax = Vab / (Eab + Fc)
    Pmin = Vab / (Eab + Fc + Fd)
    pc_vals = [Pmax, Pmax]
    pd_vals = [Pmin, Pmin]
    x_price, y_price = cutting_price(Pmax, Pmin, Eab, Vab)


    for j in range(1, higher_e+1):
        y = y_scale(Vab / j)
        dwg.add(dwg.line((x_scale(0), y), (x_scale(100), y), stroke="#ccc", stroke_dasharray="4,2"))
        dwg.add(
            dwg.text(
                f"Vab/{j}",
                insert=(x_scale(0) - 10, y + 4),
                font_size="10px",
                text_anchor="end",
                fill="#666",
            )
        )
    if show_price:
        # Línea de precio de corte (Eab+1)-ésima curva más alta, considerando todas las líneas
        draw_line(
            dwg, x_scale, y_scale,
            x_price,
            y_price,
            stroke_color="green",
            stroke_width=5,
        )
        draw_line(
            dwg, x_scale, y_scale,
            x_price,
            y_price,
            stroke_color="white",
            stroke_width=2,
        )

    def cut_line_top(xs, ys):
        p1, p2 = zip(xs, ys)
        # ordena puntos por y
        p1, p2 = list(sorted([p1,p2],key=lambda p: p[1]))
        if p2[1] <= y_scale.domain_max:
            return p2
        factor = y_scale.domain_max / p2[1]
        return (
            p1[0] + factor*(p2[0]-p1[0]),
            y_scale.domain_max,
        )

    # Dibujar curvas Va/j y etiquetas dentro del gráfico
    for j in sorted(va_div.keys()):
        draw_line(dwg, x_scale, y_scale, x_vals, va_div[j], "blue", dashed=True)
        label_pos = cut_line_top(x_vals, va_div[j])
        label_line(
            dwg, x_scale, y_scale,
            label_pos[0],
            label_pos[1],
            f"Va/{j}",
            color="blue",
            anchor="end",
            dx=-5,
        )

    # Dibujar curvas Vb/j y etiquetas dentro del gráfico
    for j in sorted(vb_div.keys()):
        draw_line(dwg, x_scale, y_scale, x_vals, vb_div[j], "red", dashed=True)
        label_pos = cut_line_top(x_vals, vb_div[j])
        label_line(
            dwg, x_scale, y_scale,
            label_pos[0],
            label_pos[1],
            f"Vb/{j}",
            color="red",
            dx=5,
        )

    # Dibujar las líneas de Pmax y Pmin como constantes
    draw_line(
        dwg, x_scale, y_scale,
        x_vals,
        pc_vals,
        stroke_color="purple",
        stroke_width=2,
        dashed=True,
    )
    draw_line(
        dwg, x_scale, y_scale,
        x_vals,
        pd_vals,
        stroke_color="orange",
        stroke_width=2,
        dashed=True,
    )

    # Etiquetas de Pmax y Pmin
    label_line(
        dwg, x_scale, y_scale,
        x_vals[-1],
        pc_vals[-1],  # encima de la línea
        "Pmax",
        color="purple",
        anchor="start",
        dx=+5,
    )
    label_line(
        dwg, x_scale, y_scale,
        x_vals[-1],
        pd_vals[-1],  # encima de la línea
        "Pmin",
        color="orange",
        anchor="start",
        dx=+5,
    )

    if show_price:
        label_line(
            dwg, x_scale, y_scale,
            x_vals[-1],
            y_price[-1],
            f"P",
            font_weight="bold",
            color="green",
            dx=-5,
            dy=15,
            anchor="end",
        )

    draw_plot_labels(
        dwg, width, height,
        title = title,
        x_label = "Concentración del voto A-B en A (%)",
        y_label = "Votos",
    )

    dwg.save()
    cairosvg.svg2png(url=output_svg, write_to=output_png)
    cairosvg.svg2pdf(url=output_svg, write_to=output_pdf)

if __name__ == "__main__":
    size = 500
    margin = 50
    Fc = 0.2  # Factor para la tercera candidatura (Pmax)
    Fd = 0.6  # Factor para la cuarta candidatura (Pmin)
    Eab = 4  # Fijamos Eab a 4
    generate_transfer_space_price(
        Vab=100,
        width=size+2*margin,
        height=size+2*margin,
        margin=margin,
        title="Espacio de Transferencia de Votos",
        basename="transferspace",
        Fc=0.2,
        Fd=0.6,
        Eab=Eab,
        show_price=False,
    )
    generate_transfer_space_price(
        Vab=100,
        width=size+2*margin,
        height=size/2+2*margin,
        margin=margin,
        title="Variación del precio en el espacio de transferencia",
        basename="transferspace-price-third",
        Fc=0.2,
        Fd=0.5,
        Eab=Eab,
        y_low=1.0/8,
        y_top=1.0/3,
    )
    generate_transfer_space_price(
        Vab=100,
        width=size+2*margin,
        height=size/2+2*margin,
        margin=margin,
        title="Variación del precio en el espacio de transferencia, sin efecto de terceros",
        basename="transferspace-price-direct",
        Fc=0.0,
        Fd=1.0,
        Eab=Eab,
        y_low=1.0/8,
        y_top=1.0/3,
    )

    generate_transfer_space_results(
        Vab=100,
        width=size+2*margin,
        height=size/5+2*margin,
        margin=margin,
        title="Resultados a lo largo de espacio de trasvases",
        basename="transferspace-seat-third",
        Fc=0.0,
        Fd=0.6,
        Eab=Eab,
    )

    generate_transfer_space_results(
        Vab=100,
        width=size+2*margin,
        height=size/5+2*margin,
        margin=margin,
        title="Resultados a lo largo de espacio de trasvases",
        basename="transferspace-seat-direct",
        Fc=0.0,
        Fd=1.,
        Eab=Eab,
    )


