

import sys
import numpy as np
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QSlider, QLabel, QPushButton
from PyQt6.QtCore import Qt, QRectF
from PyQt6.QtGui import QPainter, QColor, QPen

class PriceOnTransferGraph(QWidget):
    def __init__(self):
        super().__init__()

        # Inicialización de los parámetros
        self.Vab = 10
        self.Eab = 5
        self.Fab = 0.5
        self.PD = 5

        # Configuración de la ventana
        self.setWindowTitle("Price on Transfer Graph")
        self.setGeometry(100, 100, 600, 600)

        # Layout de la interfaz
        layout = QVBoxLayout()

        # Etiquetas y sliders
        self.Vab_label = QLabel(f"Vab = {self.Vab}")
        layout.addWidget(self.Vab_label)
        self.Vab_slider = QSlider(Qt.Orientation.Horizontal)
        self.Vab_slider.setRange(1, 50)
        self.Vab_slider.setValue(self.Vab)
        self.Vab_slider.valueChanged.connect(self.update_Vab)
        layout.addWidget(self.Vab_slider)

        self.Eab_label = QLabel(f"Eab = {self.Eab}")
        layout.addWidget(self.Eab_label)
        self.Eab_slider = QSlider(Qt.Orientation.Horizontal)
        self.Eab_slider.setRange(1, 20)
        self.Eab_slider.setValue(self.Eab)
        self.Eab_slider.valueChanged.connect(self.update_Eab)
        layout.addWidget(self.Eab_slider)

        self.Fab_label = QLabel(f"Fab = {self.Fab}")
        layout.addWidget(self.Fab_label)
        self.Fab_slider = QSlider(Qt.Orientation.Horizontal)
        self.Fab_slider.setRange(0, 500)  # 0 to 500 for easier control
        self.Fab_slider.setValue(int(self.Fab * 500))  # Convert Fab to integer (scale by 500)
        self.Fab_slider.valueChanged.connect(self.update_Fab)
        layout.addWidget(self.Fab_slider)

        self.PD_label = QLabel(f"PD = {self.PD}")
        layout.addWidget(self.PD_label)
        self.PD_slider = QSlider(Qt.Orientation.Horizontal)
        self.PD_slider.setRange(0, self.Vab)  # Rango de 0 a Vab
        self.PD_slider.setValue(self.PD)
        self.PD_slider.valueChanged.connect(self.update_PD)
        layout.addWidget(self.PD_slider)

        # Botón para generar la gráfica
        self.generate_button = QPushButton("Generate Graph")
        layout.addWidget(self.generate_button)

        # Área para el gráfico
        self.graph_widget = GraphWidget(self)
        layout.addWidget(self.graph_widget)

        self.setLayout(layout)

    def update_Vab(self, value):
        self.Vab = value
        self.Vab_label.setText(f"Vab = {self.Vab}")
        self.graph_widget.update_graph(self.Vab, self.Eab, self.Fab, self.PD)

    def update_Eab(self, value):
        self.Eab = value
        self.Eab_label.setText(f"Eab = {self.Eab}")
        self.graph_widget.update_graph(self.Vab, self.Eab, self.Fab, self.PD)

    def update_Fab(self, value):
        self.Fab = value / 500  # Convertir el valor a un rango entre 0 y 1
        self.Fab_label.setText(f"Fab = {self.Fab:.2f}")
        self.graph_widget.update_graph(self.Vab, self.Eab, self.Fab, self.PD)

    def update_PD(self, value):
        self.PD = value
        self.PD_label.setText(f"PD = {self.PD:.2f}")
        self.graph_widget.update_graph(self.Vab, self.Eab, self.Fab, self.PD)

class GraphWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setFixedSize(500, 500)  # Tamaño del widget gráfico
        self.Vab = 10
        self.Eab = 5
        self.Fab = 0.5
        self.PD = 5

    def update_graph(self, Vab, Eab, Fab, PD):
        self.Vab = Vab
        self.Eab = Eab
        self.Fab = Fab
        self.PD = PD
        self.update()  # Actualiza el widget, lo que provoca que se llame a paintEvent

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Fondo blanco
        painter.setBrush(QColor(255, 255, 255))
        painter.drawRect(0, 0, self.width(), self.height())

        # Colores y grosor de las líneas
        pen_a = QPen(QColor(0, 0, 255), 2)  # Azul para C^i_a
        pen_b = QPen(QColor(255, 0, 0), 2)  # Rojo para C^1_b
        pen_pc = QPen(QColor(0, 255, 0), 2, Qt.PenStyle.DashLine)  # Verde para Pc
        pen_pd = QPen(QColor(255, 0, 255), 2, Qt.PenStyle.DashDotLine)  # Magenta para PD

        # Calcular el factor de escala para ajustar la gráfica al tamaño del widget
        scale_x = self.width() / self.Vab
        scale_y = self.height() / self.Vab  # Escalar en función de Vab

        # Dibujar las líneas C^i_a (0, 0) a (Vab, Vab/i)
        for i in range(1, self.Eab + 1):
            y = self.Vab / i
            painter.setPen(pen_a)
            # Convertir las coordenadas a enteros y escalar
            painter.drawLine(0, self.height(), int(self.Vab * scale_x), int(self.height() - y * scale_y))

        # Dibujar las líneas C^1_b (Vab, 0) a (0, Vab/i)
        for i in range(1, self.Eab + 1):
            y = self.Vab / i
            painter.setPen(pen_b)
            # Convertir las coordenadas a enteros y escalar
            painter.drawLine(int(self.Vab * scale_x), self.height(), 0, int(self.height() - y * scale_y))

        # Dibujar la línea Pc
        Pc = self.Vab / (self.Eab + self.Fab)
        painter.setPen(pen_pc)
        # Convertir las coordenadas a enteros y escalar
        painter.drawLine(0, int(self.height() - Pc * scale_y), int(self.Vab * scale_x), int(self.height() - Pc * scale_y))

        # Dibujar la línea PD
        painter.setPen(pen_pd)
        # Convertir las coordenadas a enteros y escalar
        painter.drawLine(0, int(self.height() - self.PD * scale_y), int(self.Vab * scale_x), int(self.height() - self.PD * scale_y))

        painter.end()

# Ejecutar la aplicación
app = QApplication(sys.argv)
window = PriceOnTransferGraph()
window.show()
sys.exit(app.exec())


import sys
import numpy as np
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QSlider, QLabel, QPushButton
from PyQt6.QtCore import Qt, QRectF
from PyQt6.QtGui import QPainter, QColor, QPen

class PriceOnTransferGraph(QWidget):
    def __init__(self):
        super().__init__()

        # Inicialización de los parámetros
        self.Vab = 10
        self.Eab = 5
        self.Fab = 0.5
        self.PD = 5

        # Configuración de la ventana
        self.setWindowTitle("Price on Transfer Graph")
        self.setGeometry(100, 100, 600, 600)

        # Layout de la interfaz
        layout = QVBoxLayout()

        # Etiquetas y sliders
        self.Vab_label = QLabel(f"Vab = {self.Vab}")
        layout.addWidget(self.Vab_label)
        self.Vab_slider = QSlider(Qt.Orientation.Horizontal)
        self.Vab_slider.setRange(1, 50)
        self.Vab_slider.setValue(self.Vab)
        self.Vab_slider.valueChanged.connect(self.update_Vab)
        layout.addWidget(self.Vab_slider)

        self.Eab_label = QLabel(f"Eab = {self.Eab}")
        layout.addWidget(self.Eab_label)
        self.Eab_slider = QSlider(Qt.Orientation.Horizontal)
        self.Eab_slider.setRange(1, 20)
        self.Eab_slider.setValue(self.Eab)
        self.Eab_slider.valueChanged.connect(self.update_Eab)
        layout.addWidget(self.Eab_slider)

        self.Fab_label = QLabel(f"Fab = {self.Fab}")
        layout.addWidget(self.Fab_label)
        self.Fab_slider = QSlider(Qt.Orientation.Horizontal)
        self.Fab_slider.setRange(0, 500)  # 0 to 500 for easier control
        self.Fab_slider.setValue(int(self.Fab * 500))  # Convert Fab to integer (scale by 500)
        self.Fab_slider.valueChanged.connect(self.update_Fab)
        layout.addWidget(self.Fab_slider)

        self.PD_label = QLabel(f"PD = {self.PD}")
        layout.addWidget(self.PD_label)
        self.PD_slider = QSlider(Qt.Orientation.Horizontal)
        self.PD_slider.setRange(0, self.Vab)  # Rango de 0 a Vab
        self.PD_slider.setValue(self.PD)
        self.PD_slider.valueChanged.connect(self.update_PD)
        layout.addWidget(self.PD_slider)

        # Botón para generar la gráfica
        self.generate_button = QPushButton("Generate Graph")
        layout.addWidget(self.generate_button)

        # Área para el gráfico
        self.graph_widget = GraphWidget(self)
        layout.addWidget(self.graph_widget)

        self.setLayout(layout)

    def update_Vab(self, value):
        self.Vab = value
        self.Vab_label.setText(f"Vab = {self.Vab}")
        self.graph_widget.update_graph(self.Vab, self.Eab, self.Fab, self.PD)

    def update_Eab(self, value):
        self.Eab = value
        self.Eab_label.setText(f"Eab = {self.Eab}")
        self.graph_widget.update_graph(self.Vab, self.Eab, self.Fab, self.PD)

    def update_Fab(self, value):
        self.Fab = value / 500  # Convertir el valor a un rango entre 0 y 1
        self.Fab_label.setText(f"Fab = {self.Fab:.2f}")
        self.graph_widget.update_graph(self.Vab, self.Eab, self.Fab, self.PD)

    def update_PD(self, value):
        self.PD = value
        self.PD_label.setText(f"PD = {self.PD:.2f}")
        self.graph_widget.update_graph(self.Vab, self.Eab, self.Fab, self.PD)

class GraphWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setFixedSize(500, 500)  # Tamaño del widget gráfico
        self.Vab = 10
        self.Eab = 5
        self.Fab = 0.5
        self.PD = 5

    def update_graph(self, Vab, Eab, Fab, PD):
        self.Vab = Vab
        self.Eab = Eab
        self.Fab = Fab
        self.PD = PD
        self.update()  # Actualiza el widget, lo que provoca que se llame a paintEvent

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Fondo blanco
        painter.setBrush(QColor(255, 255, 255))
        painter.drawRect(0, 0, self.width(), self.height())

        # Colores y grosor de las líneas
        pen_a = QPen(QColor(0, 0, 255), 2)  # Azul para C^i_a
        pen_b = QPen(QColor(255, 0, 0), 2)  # Rojo para C^1_b
        pen_pc = QPen(QColor(0, 255, 0), 2, Qt.PenStyle.DashLine)  # Verde para Pc
        pen_pd = QPen(QColor(255, 0, 255), 2, Qt.PenStyle.DashDotLine)  # Magenta para PD

        # Calcular el factor de escala para ajustar la gráfica al tamaño del widget
        scale_x = self.width() / self.Vab
        scale_y = self.height() / (self.Vab / self.Eab)  # Escalar en función de Eab

        # Dibujar las líneas C^i_a (0, 0) a (Vab, Vab/i)
        for i in range(1, self.Eab + 1):
            y = self.Vab / i
            painter.setPen(pen_a)
            # Convertir las coordenadas a enteros y escalar
            painter.drawLine(0, 0, int(self.Vab * scale_x), int(y * scale_y))

        # Dibujar las líneas C^1_b (Vab, 0) a (0, Vab/i)
        for i in range(1, self.Eab + 1):
            y = self.Vab / i
            painter.setPen(pen_b)
            # Convertir las coordenadas a enteros y escalar
            painter.drawLine(int(self.Vab * scale_x), 0, 0, int(y * scale_y))

        # Dibujar la línea Pc
        Pc = self.Vab / (self.Eab + self.Fab)
        painter.setPen(pen_pc)
        # Convertir las coordenadas a enteros y escalar
        painter.drawLine(0, int(Pc * scale_y), int(self.Vab * scale_x), int(Pc * scale_y))

        # Dibujar la línea PD
        painter.setPen(pen_pd)
        # Convertir las coordenadas a enteros y escalar
        painter.drawLine(0, int(self.PD * scale_y), int(self.Vab * scale_x), int(self.PD * scale_y))

        painter.end()

# Ejecutar la aplicación
app = QApplication(sys.argv)
window = PriceOnTransferGraph()
window.show()
sys.exit(app.exec())


import sys
import numpy as np
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QSlider, QLabel, QPushButton
from PyQt6.QtCore import Qt, QRectF
from PyQt6.QtGui import QPainter, QColor, QPen

class PriceOnTransferGraph(QWidget):
    def __init__(self):
        super().__init__()

        # Inicialización de los parámetros
        self.Vab = 10
        self.Eab = 5
        self.Fab = 0.5
        self.PD = 5

        # Configuración de la ventana
        self.setWindowTitle("Price on Transfer Graph")
        self.setGeometry(100, 100, 600, 600)

        # Layout de la interfaz
        layout = QVBoxLayout()

        # Etiquetas y sliders
        self.Vab_label = QLabel(f"Vab = {self.Vab}")
        layout.addWidget(self.Vab_label)
        self.Vab_slider = QSlider(Qt.Orientation.Horizontal)
        self.Vab_slider.setRange(1, 50)
        self.Vab_slider.setValue(self.Vab)
        self.Vab_slider.valueChanged.connect(self.update_Vab)
        layout.addWidget(self.Vab_slider)

        self.Eab_label = QLabel(f"Eab = {self.Eab}")
        layout.addWidget(self.Eab_label)
        self.Eab_slider = QSlider(Qt.Orientation.Horizontal)
        self.Eab_slider.setRange(1, 20)
        self.Eab_slider.setValue(self.Eab)
        self.Eab_slider.valueChanged.connect(self.update_Eab)
        layout.addWidget(self.Eab_slider)

        self.Fab_label = QLabel(f"Fab = {self.Fab}")
        layout.addWidget(self.Fab_label)
        self.Fab_slider = QSlider(Qt.Orientation.Horizontal)
        self.Fab_slider.setRange(0, 500)  # 0 to 500 for easier control
        self.Fab_slider.setValue(int(self.Fab * 500))  # Convert Fab to integer (scale by 500)
        self.Fab_slider.valueChanged.connect(self.update_Fab)
        layout.addWidget(self.Fab_slider)

        self.PD_label = QLabel(f"PD = {self.PD}")
        layout.addWidget(self.PD_label)
        self.PD_slider = QSlider(Qt.Orientation.Horizontal)
        self.PD_slider.setRange(0, self.Vab)  # Rango de 0 a Vab
        self.PD_slider.setValue(self.PD)
        self.PD_slider.valueChanged.connect(self.update_PD)
        layout.addWidget(self.PD_slider)

        # Botón para generar la gráfica
        self.generate_button = QPushButton("Generate Graph")
        layout.addWidget(self.generate_button)

        # Área para el gráfico
        self.graph_widget = GraphWidget(self)
        layout.addWidget(self.graph_widget)

        self.setLayout(layout)

    def update_Vab(self, value):
        self.Vab = value
        self.Vab_label.setText(f"Vab = {self.Vab}")
        self.graph_widget.update_graph(self.Vab, self.Eab, self.Fab, self.PD)

    def update_Eab(self, value):
        self.Eab = value
        self.Eab_label.setText(f"Eab = {self.Eab}")
        self.graph_widget.update_graph(self.Vab, self.Eab, self.Fab, self.PD)

    def update_Fab(self, value):
        self.Fab = value / 500  # Convertir el valor a un rango entre 0 y 1
        self.Fab_label.setText(f"Fab = {self.Fab:.2f}")
        self.graph_widget.update_graph(self.Vab, self.Eab, self.Fab, self.PD)

    def update_PD(self, value):
        self.PD = value
        self.PD_label.setText(f"PD = {self.PD:.2f}")
        self.graph_widget.update_graph(self.Vab, self.Eab, self.Fab, self.PD)

class GraphWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setFixedSize(500, 500)  # Tamaño del widget gráfico
        self.Vab = 10
        self.Eab = 5
        self.Fab = 0.5
        self.PD = 5

    def update_graph(self, Vab, Eab, Fab, PD):
        self.Vab = Vab
        self.Eab = Eab
        self.Fab = Fab
        self.PD = PD
        self.update()  # Actualiza el widget, lo que provoca que se llame a paintEvent

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Fondo blanco
        painter.setBrush(QColor(255, 255, 255))
        painter.drawRect(0, 0, self.width(), self.height())

        # Colores y grosor de las líneas
        pen_a = QPen(QColor(0, 0, 255), 2)  # Azul para C^i_a
        pen_b = QPen(QColor(255, 0, 0), 2)  # Rojo para C^1_b
        pen_pc = QPen(QColor(0, 255, 0), 2, Qt.PenStyle.DashLine)  # Verde para Pc
        pen_pd = QPen(QColor(255, 0, 255), 2, Qt.PenStyle.DashDotLine)  # Magenta para PD

        # Dibujar las líneas C^i_a (0, 0) a (Vab, Vab/i)
        for i in range(1, self.Eab + 1):
            y = self.Vab / i
            painter.setPen(pen_a)
            # Convertir las coordenadas a enteros
            painter.drawLine(0, 0, int(self.Vab), int(y))

        # Dibujar las líneas C^1_b (Vab, 0) a (0, Vab/i)
        for i in range(1, self.Eab + 1):
            y = self.Vab / i
            painter.setPen(pen_b)
            # Convertir las coordenadas a enteros
            painter.drawLine(int(self.Vab), 0, 0, int(y))

        # Dibujar la línea Pc
        Pc = self.Vab / (self.Eab + self.Fab)
        painter.setPen(pen_pc)
        # Convertir las coordenadas a enteros
        painter.drawLine(0, int(Pc), int(self.Vab), int(Pc))

        # Dibujar la línea PD
        painter.setPen(pen_pd)
        # Convertir las coordenadas a enteros
        painter.drawLine(0, int(self.PD), int(self.Vab), int(self.PD))

        painter.end()

# Ejecutar la aplicación
app = QApplication(sys.argv)
window = PriceOnTransferGraph()
window.show()
sys.exit(app.exec())


import sys
import numpy as np
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QSlider, QLabel, QPushButton
from PyQt6.QtCore import Qt, QRectF
from PyQt6.QtGui import QPainter, QColor, QPen

class PriceOnTransferGraph(QWidget):
    def __init__(self):
        super().__init__()

        # Inicialización de los parámetros
        self.Vab = 10
        self.Eab = 5
        self.Fab = 0.5
        self.PD = 5

        # Configuración de la ventana
        self.setWindowTitle("Price on Transfer Graph")
        self.setGeometry(100, 100, 600, 600)

        # Layout de la interfaz
        layout = QVBoxLayout()

        # Etiquetas y sliders
        self.Vab_label = QLabel(f"Vab = {self.Vab}")
        layout.addWidget(self.Vab_label)
        self.Vab_slider = QSlider(Qt.Orientation.Horizontal)
        self.Vab_slider.setRange(1, 50)
        self.Vab_slider.setValue(self.Vab)
        self.Vab_slider.valueChanged.connect(self.update_Vab)
        layout.addWidget(self.Vab_slider)

        self.Eab_label = QLabel(f"Eab = {self.Eab}")
        layout.addWidget(self.Eab_label)
        self.Eab_slider = QSlider(Qt.Orientation.Horizontal)
        self.Eab_slider.setRange(1, 20)
        self.Eab_slider.setValue(self.Eab)
        self.Eab_slider.valueChanged.connect(self.update_Eab)
        layout.addWidget(self.Eab_slider)

        self.Fab_label = QLabel(f"Fab = {self.Fab}")
        layout.addWidget(self.Fab_label)
        self.Fab_slider = QSlider(Qt.Orientation.Horizontal)
        self.Fab_slider.setRange(0, 500)  # 0 to 500 for easier control
        self.Fab_slider.setValue(int(self.Fab * 500))  # Convert Fab to integer (scale by 500)
        self.Fab_slider.valueChanged.connect(self.update_Fab)
        layout.addWidget(self.Fab_slider)

        self.PD_label = QLabel(f"PD = {self.PD}")
        layout.addWidget(self.PD_label)
        self.PD_slider = QSlider(Qt.Orientation.Horizontal)
        self.PD_slider.setRange(0, self.Vab)  # Rango de 0 a Vab
        self.PD_slider.setValue(self.PD)
        self.PD_slider.valueChanged.connect(self.update_PD)
        layout.addWidget(self.PD_slider)

        # Botón para generar la gráfica
        self.generate_button = QPushButton("Generate Graph")
        layout.addWidget(self.generate_button)

        # Área para el gráfico
        self.graph_widget = GraphWidget(self)
        layout.addWidget(self.graph_widget)

        self.setLayout(layout)

    def update_Vab(self, value):
        self.Vab = value
        self.Vab_label.setText(f"Vab = {self.Vab}")
        self.graph_widget.update_graph(self.Vab, self.Eab, self.Fab, self.PD)

    def update_Eab(self, value):
        self.Eab = value
        self.Eab_label.setText(f"Eab = {self.Eab}")
        self.graph_widget.update_graph(self.Vab, self.Eab, self.Fab, self.PD)

    def update_Fab(self, value):
        self.Fab = value / 500  # Convertir el valor a un rango entre 0 y 1
        self.Fab_label.setText(f"Fab = {self.Fab:.2f}")
        self.graph_widget.update_graph(self.Vab, self.Eab, self.Fab, self.PD)

    def update_PD(self, value):
        self.PD = value
        self.PD_label.setText(f"PD = {self.PD:.2f}")
        self.graph_widget.update_graph(self.Vab, self.Eab, self.Fab, self.PD)

class GraphWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setFixedSize(500, 500)  # Tamaño del widget gráfico
        self.Vab = 10
        self.Eab = 5
        self.Fab = 0.5
        self.PD = 5

    def update_graph(self, Vab, Eab, Fab, PD):
        self.Vab = Vab
        self.Eab = Eab
        self.Fab = Fab
        self.PD = PD
        self.update()  # Actualiza el widget, lo que provoca que se llame a paintEvent

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Fondo blanco
        painter.setBrush(QColor(255, 255, 255))
        painter.drawRect(0, 0, self.width(), self.height())

        # Colores y grosor de las líneas
        pen_a = QPen(QColor(0, 0, 255), 2)  # Azul para C^i_a
        pen_b = QPen(QColor(255, 0, 0), 2)  # Rojo para C^1_b
        pen_pc = QPen(QColor(0, 255, 0), 2, Qt.PenStyle.DashLine)  # Verde para Pc
        pen_pd = QPen(QColor(255, 0, 255), 2, Qt.PenStyle.DashDotLine)  # Magenta para PD

        # Dibujar las líneas C^i_a (0, 0) a (Vab, Vab/i)
        for i in range(1, self.Eab + 1):
            painter.setPen(pen_a)
            painter.drawLine(0, 0, self.Vab, self.Vab / i)

        # Dibujar las líneas C^1_b (Vab, 0) a (0, Vab/i)
        for i in range(1, self.Eab + 1):
            painter.setPen(pen_b)
            painter.drawLine(self.Vab, 0, 0, self.Vab / i)

        # Dibujar la línea Pc
        Pc = self.Vab / (self.Eab + self.Fab)
        painter.setPen(pen_pc)
        painter.drawLine(0, Pc, self.Vab, Pc)

        # Dibujar la línea PD
        painter.setPen(pen_pd)
        painter.drawLine(0, self.PD, self.Vab, self.PD)

        painter.end()

# Ejecutar la aplicación
app = QApplication(sys.argv)
window = PriceOnTransferGraph()
window.show()
sys.exit(app.exec())
