from labPythonOOP.rectangle import Rectangle
from labPythonOOP.circle import Circle
from labPythonOOP.square import Square
from colorama import Fore, Style, init

def main():

    init()

    r = Rectangle(25, 25, "синий")
    c = Circle(25, "зелёный")
    s = Square(25, "красный")

    print(Fore.BLUE, r, Style.RESET_ALL)
    print(Fore.GREEN, c, Style.RESET_ALL)
    print(Fore.RED, s, Style.RESET_ALL)

    print(repr(r))
    print(repr(c))
    print(repr(s))

if __name__ == "__main__":
    main()
