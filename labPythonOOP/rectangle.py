from .geometricFigure import GeometricFigure
from .figureColor import FigureColor

class Rectangle(GeometricFigure):
    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        self.color = FigureColor(color)

    FIGURE_TYPE = "Прямоугольник"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __repr__(self):
        return "Фигура: {}, ширина = {}, высота = {}, цвет = {}, площадь = {:.2f}".format(
        self.get_figure_type(),
        self.width,
        self.length,
        self.color.color,
        self.area()
        )

    def __str__(self):
        return f"Прямоугольник {self.width}x{self.length} цвета {self.color.color}"

    def area(self):
        return self.length*self.width
