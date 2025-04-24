from manim import *

class RestosEnEspacioCircular(Scene):
    def construct(self):
        # Parámetros
        radius = 3
        partidoA_resto = 0.65  # 65% del cociente
        partidoB_resto = 0.35  # 35% del cociente
        trasvase = 0.20        # Movimiento en % del cociente
        
        # Círculo base
        circle = Circle(radius=radius, color=WHITE).move_to(ORIGIN)
        self.play(Create(circle))

        # Marcas de referencia (0%, 25%, 50%, 75%, 100%)
        for i in range(5):
            angle = i * PI / 2
            line = Line(
                start=radius * np.array([np.cos(angle), np.sin(angle), 0]),
                end=1.1 * radius * np.array([np.cos(angle), np.sin(angle), 0]),
                color=GRAY
            )
            self.add(line)
            label = Text(f"{i*25}%", font_size=30).move_to(1.3 * radius * np.array([np.cos(angle), np.sin(angle), 0]))
            self.add(label)

        # Partidos antes del trasvase
        def punto_en_resto(resto):
            angle = resto * TAU
            return Dot(point=radius * np.array([np.cos(angle), np.sin(angle), 0]), color=BLUE)

        puntoA = punto_en_resto(partidoA_resto)
        puntoB = punto_en_resto(partidoB_resto)

        labelA = Text("A", font_size=36, color=BLUE).next_to(puntoA, UP)
        labelB = Text("B", font_size=36, color=GREEN).next_to(puntoB, DOWN)

        self.play(FadeIn(puntoA), FadeIn(puntoB), Write(labelA), Write(labelB))

        # Mostrar flecha de trasvase
        flecha = Arrow(puntoA.get_center(), puntoB.get_center(), color=YELLOW)
        self.play(GrowArrow(flecha))
        self.wait(1)

        # Movimiento: trasvase
        nuevoA = punto_en_resto(partidoA_resto - trasvase)
        nuevoB = punto_en_resto(partidoB_resto + trasvase)

        self.play(
            Transform(puntoA, nuevoA),
            Transform(puntoB, nuevoB),
            labelA.animate.next_to(nuevoA, UP),
            labelB.animate.next_to(nuevoB, DOWN),
        )

        self.wait(2)
