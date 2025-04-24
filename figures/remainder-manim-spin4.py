from manim import *

class GiroDeVotosConRestosFinal(Scene):
    def construct(self):
        radius = 3
        centro = DOWN * 1.5
        total_votos_A = 2.75
        total_votos_B = 1.4

        # Círculo base
        circle = Arc(radius=radius, angle=TAU, start_angle=0, color=WHITE).move_arc_center_to(centro)
        arrow = CurvedArrow(
            start_point=centro + radius * RIGHT,
            end_point=centro + radius * UP,
            color=WHITE,
            tip_length=0.3,
            angle=-PI/2
        )
        self.play(FadeIn(circle, run_time=0.5), FadeIn(arrow, run_time=0.5))

        # Marca del 0%
        zero_marker = Line(
            start=centro + radius * RIGHT,
            end=centro + 1.2 * radius * RIGHT,
            color=RED
        )
        zero_label = Text("0%", font_size=30).next_to(zero_marker, RIGHT)
        self.add(zero_marker, zero_label)

        def animar_partido(total, color, label_text, y_shift=UP, mantener_anteriores=False):
            vueltas = int(total)
            resto = total % 1

            puntero = Dot(color=color).move_to(centro + radius * RIGHT)
            contador = Integer(number=0, font_size=36, color=color)
            etiqueta = Text(label_text, font_size=30, color=color)
            etiqueta_completa = VGroup(etiqueta, contador).arrange(RIGHT, buff=0.3).next_to(puntero, y_shift)
            etiqueta_label = Text("escaños", font_size=24, color=color).next_to(etiqueta_completa, DOWN, buff=0.2)

            self.play(FadeIn(puntero), Write(etiqueta_completa), FadeIn(etiqueta_label))

            for i in range(vueltas):
                self.play(
                    Rotate(puntero, angle=TAU, about_point=centro, run_time=1, rate_func=linear),
                    ChangeDecimalToValue(contador, i + 1, run_time=1),
                )
                escaño_marker = Dot(puntero.get_center(), radius=0.06, color=color)
                self.add(escaño_marker)

            if resto > 0:
                self.play(
                    Rotate(puntero, angle=resto * TAU, about_point=centro, run_time=1.5, rate_func=linear),
                )

            resto_dot = Dot(puntero.get_center(), radius=0.1, color=color)
            self.play(FadeIn(resto_dot))

            # Crear sector exterior y restarle uno interior para que parezca un anillo
            sector_externo = Sector(
                arc_center=centro,
                radius=radius * 1.1,
                start_angle=TAU * vueltas,
                angle=TAU * resto
            ).set_fill(color=color, opacity=0.4).set_stroke(width=0)

            sector_interno = Sector(
                arc_center=centro,
                radius=radius * 0.6,
                start_angle=TAU * vueltas,
                angle=TAU * resto
            ).set_fill(color=BLACK, opacity=1).set_stroke(width=0)

            anillo = VGroup(sector_externo, sector_interno)

            self.play(FadeIn(anillo), run_time=0.5)
            self.wait(1)
            self.play(FadeOut(anillo), run_time=0.5)

            if not mantener_anteriores:
                self.play(FadeOut(puntero), FadeOut(etiqueta_completa), FadeOut(etiqueta_label))

        animar_partido(total_votos_A, BLUE, "Partido A", y_shift=UP, mantener_anteriores=True)
        animar_partido(total_votos_B, GREEN, "Partido B", y_shift=DOWN, mantener_anteriores=False)

        self.wait(2)

