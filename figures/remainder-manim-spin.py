from manim import *

class GiroDeVotosConRestos(Scene):
    def construct(self):
        radius = 3
        total_votos_A = 2.75  # 2 escaños y 75% de otro
        total_votos_B = 1.4   # 1 escaño y 40% de otro

        # Círculo base
        circle = Circle(radius=radius, color=WHITE)
        self.play(Create(circle))

        # Función para girar y dejar marcador
        def animar_partido(total, color, label_text, start_angle=0, y_shift=UP):
            vueltas = int(total)
            resto = total % 1
            total_angulo = TAU * total

            # Puntero inicial
            puntero = Dot(color=color).move_to(radius * RIGHT)
            label = Text(label_text, font_size=30, color=color).next_to(puntero, y_shift)

            contador = Integer(number=0, font_size=48, color=color)
            contador.move_to(LEFT * 4 + y_shift * 2)

            self.play(FadeIn(puntero), Write(label), FadeIn(contador))

            # Girar por escaños completos
            for i in range(vueltas):
                self.play(
                    Rotate(puntero, angle=TAU, about_point=ORIGIN, run_time=1),
                    ChangeDecimalToValue(contador, i + 1, run_time=1),
                )

            # Girar hasta resto
            if resto > 0:
                self.play(
                    Rotate(puntero, angle=resto * TAU, about_point=ORIGIN, run_time=1.5),
                )

            # Marcar el punto final
            resto_dot = Dot(puntero.get_center(), radius=0.1, color=color)
            self.play(FadeIn(resto_dot))
            self.wait(0.5)

            self.play(FadeOut(puntero), FadeOut(label), FadeOut(contador))

        # Partido A
        animar_partido(total_votos_A, BLUE, "Partido A", y_shift=UP)

        # Partido B
        animar_partido(total_votos_B, GREEN, "Partido B", y_shift=DOWN)

        self.wait(2)
