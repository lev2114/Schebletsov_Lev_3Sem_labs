import math
from .geometricFigure import GeometricFigure
from .figureColor import FigureColor

class Circle(GeometricFigure):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = FigureColor(color)

    FIGURE_TYPE = "Круг"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Круг радиусом {self.radius} цвета {self.color.color}"

    def __repr__(self):
        return "Фигура: {}, радиус = {}, цвет = {}, площадь = {:.2f}".format(
            self.get_figure_type(),
            self.radius,
            self.color.color,
            self.area()
        )
