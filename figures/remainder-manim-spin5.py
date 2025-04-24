from manim import *

class GiroDeVotosConRestosFinal(Scene):
    def construct(self):
        radius = 3
        centro = DOWN * 1.5
        total_votos_A = 2.75
        total_votos_B = 1.4

        # Círculo base
        circle = Arc(radius=radius, angle=TAU, start_angle=0, color=WHITE).move_arc_center_to(centro)
        self.play(FadeIn(circle, run_time=0.5))

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
            flecha = Arrow(start=ORIGIN, end=RIGHT * 0.6, color=color, max_tip_length_to_length_ratio=0.4)
            flecha.move_to(puntero.get_center()).rotate_about_origin(PI / 2)

            conjunto = VGroup(puntero, flecha)

            contador = Integer(number=0, font_size=36, color=color)
            etiqueta = Text(label_text, font_size=30, color=color)
            etiqueta_completa = VGroup(etiqueta, contador).arrange(RIGHT, buff=0.3).next_to(conjunto, y_shift)
            etiqueta_label = Text("escaños", font_size=24, color=color).next_to(etiqueta_completa, DOWN, buff=0.2)

            self.play(FadeIn(conjunto), Write(etiqueta_completa), FadeIn(etiqueta_label))

            for i in range(vueltas):
                self.play(
                    conjunto.animate.rotate(angle=TAU, about_point=centro),
                    ChangeDecimalToValue(contador, i + 1, run_time=1),
                )
                escaño_marker = Dot(puntero.get_center(), radius=0.06, color=color)
                self.add(escaño_marker)

            if resto > 0:
                self.play(
                    conjunto.animate.rotate(angle=resto * TAU, about_point=centro),
                )

            resto_dot = Dot(puntero.get_center(), radius=0.1, color=color)
            self.play(FadeIn(resto_dot))

            # Crear anillo de restos
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
                self.play(FadeOut(conjunto), FadeOut(etiqueta_completa), FadeOut(etiqueta_label))

        # Partido A
        animar_partido(total_votos_A, BLUE, "Partido A", y_shift=UP, mantener_anteriores=True)

        # Partido B
        animar_partido(total_votos_B, GREEN, "Partido B", y_shift=DOWN, mantener_anteriores=False)

        self.wait(2)
