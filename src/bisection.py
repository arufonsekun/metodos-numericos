def bisection(a: int, b: int, precision: float, f):
    """
    Implements bisection method.

    Args:
        a, b (int): Xs coordinates which is know there is a in between
        precision: function root precision
        f (lambda function): Function to find the root
    """
    i = 0
    y = precision + 1
    print("i\t\t a\t\t b\t\t x\t\t f(x)")
    while abs(y) >= precision:
        x = (a + b) / 2
        y = f(x)
        print("{}\t\t {}\t\t {}\t\t {:e}\t\t {:e}".format(i, a, b, x, y))
        if y < 0:
            a = x
        else:
            b = x
        i += 1
        if y == 0:
            return x
    return x
