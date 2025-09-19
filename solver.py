import sys
import math

class Solver:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        parts = []

        if self.a != 0:
            if abs(self.a) == 1:
                parts.append("x^4" if self.a > 0 else "-x^4")
            else:
                parts.append(f"{self.a}x^4")

        if self.b != 0:
            sign = "+" if self.b > 0 else "-"
            coeff = "" if abs(self.b) == 1 else str(abs(self.b))
            parts.append(f"{sign} {coeff}x^2")

        if self.c != 0:
            sign = "+" if self.c > 0 else "-"
            parts.append(f"{sign} {abs(self.c)}")
            return " ".join(parts)

    def solve(self):
        D = self.b**2 - 4*self.a*self.c
        if D<0:
            return "Действительных корней нет!"
        elif D == 0:
            root = (-self.b)/(2*self.a)
            if root < 0:
                return "Действительных корней нет!"
            elif root == 0:
                return "Корень: 0"
            else:
                return f"Корни: +-{math.sqrt(root)}"
        else:
            root1 = (-self.b + math.sqrt(D))/(2*self.a)
            root2 = (-self.b - math.sqrt(D))/(2*self.a)

            solutions = []

            for i in (root1, root2):
                if i > 0:
                    solutions.extend([math.sqrt(i), -math.sqrt(i)])
                elif i == 0:
                    solutions.append(0)

            if not solutions:
                return "Действительных корней нет!"
            else:
                return f"Корни: {', '.join(map(str, solutions))}"


args = []
argnames = ['A', 'B', 'C']

for i in range(3):
    value = None

    if len(sys.argv) > i + 1:
        try:
            value = float(sys.argv[i + 1])
        except ValueError:
            print(f"Ошибка: коэффициент {argnames[i]} некорректен")

    while value is None:
        try:
            value = float(input(f"Введите коэффициент {argnames[i]}: "))
        except ValueError:
            print("Ошибка: введите число.")

    args.append(value)

solver = Solver(*args)
print(solver)
print(solver.solve())
