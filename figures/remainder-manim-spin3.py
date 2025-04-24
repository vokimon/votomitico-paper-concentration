from manim import *

class GiroDeVotosConRestosVertical(Scene):
    def construct(self):
        radius = 3
        centro = DOWN * 1.5  # centro vertical del círculo
        total_votos_A = 2.75
        total_votos_B = 1.4

        # Círculo base
        circle = Circle(radius=radius, color=WHITE).move_to(centro)
        self.play(Create(circle))

        # Marca del 0%
        zero_marker = Line(
            start=centro + radius * RIGHT,
            end=centro + 1.2 * radius * RIGHT,
            color=RED
        )
        zero_label = Text("0%", font_size=30).next_to(zero_marker, RIGHT)
        self.add(zero_marker, zero_label)

        # Función para animar giro
        def animar_partido(total, color, label_text, y_shift=UP, mantener_anteriores=False):
            vueltas = int(total)
            resto = total % 1

            # Puntero inicial
            puntero = Dot(color=color).move_to(centro + radius * RIGHT)
            label = Text(label_text, font_size=30, color=color).next_to(puntero, y_shift)

            contador = Integer(number=0, font_size=48, color=color)
            contador_label = Text("escaños", font_size=24, color=color).next_to(contador, DOWN, buff=0.2)
            contador_group = VGroup(contador, contador_label).move_to(LEFT * 4 + y_shift * 2)

            self.play(FadeIn(puntero), Write(label), FadeIn(contador_group))

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
            self.wait(0.5)

            if not mantener_anteriores:
                self.play(FadeOut(puntero), FadeOut(label), FadeOut(contador_group))

        # Partido A
        animar_partido(total_votos_A, BLUE, "Partido A", y_shift=UP, mantener_anteriores=True)

        # Partido B
        animar_partido(total_votos_B, GREEN, "Partido B", y_shift=DOWN, mantener_anteriores=False)

        self.wait(2)
