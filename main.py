from src.bisection import *
from src.secant import *
from src.newton import *

def Bisection():
    a = 0
    b = 3
    f = lambda x: (x ** 3) - (5 * x**2) + x + 3
    root = bisection(4, 6, 0.01, f)
    print(f"A raiz aproximada da função é { root }")


def Secants():
    f = lambda x: x**3 - 5 * x**2 + x + 3
    x0 = -2
    x1 = 0
    precision = 0.00001
    max_iter = 50
    _, root = secant(x0, x1, precision, f, max_iter)
    print(f"A raiz da função é {root}")


def Newton():
    f = lambda x: x**3 - 5 * x**2 + x + 3
    f_linha = lambda x: 3 * x**2 - 10 * x + 1
    x0 = 3
    precision = 0.00001
    max_iter = 50
    _, root = newton(x0, precision, f, f_linha, max_iter)
    print(f"A raiz da função é {root}")

if __name__ == "__main__":
    Bisection()
    # Secants()
    # Newton()
