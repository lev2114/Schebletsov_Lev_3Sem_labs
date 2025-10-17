from .rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side, color):
        super().__init__(side, side, color)

    FIGURE_TYPE = "Квадрат"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __str__(self):
        return f"Квадрат со стороной {self.width} цвета {self.color.color}"

    def __repr__(self):
        return "Фигура: {}, сторона = {}, цвет = {}, площадь = {:.2f}".format(
            self.get_figure_type(),
            self.width,
            self.color.color,
            self.area()
        )
