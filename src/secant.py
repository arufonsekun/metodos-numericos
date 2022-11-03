def secant(x0: int, x1: int, precision: int, f, max_iter=50):
    """
    Implements string method aka secants method.

    Args:
        x0, x1 (int): Intial aproximations
        precision: function root precision
        f (lambda function): Function to find the root
        max_iter (int): Max number of iterations
    """

    if abs(f(x0)) <= precision:
        return (False, x0)

    if abs(f(x1)) <= precision:
        return (False, x1)

    print("i\t x\t\t f(x)")
    print("-\t{:e}\t{:e}".format(x0, f(x0)))
    print("-\t{:e}\t{:e}".format(x1, f(x1)))

    for i in range(max_iter):
        x2 = (x0 * f(x1) - x1 * f(x0)) / (f(x1) - f(x0))
        print("{}\t{:e}\t{:e}".format(i, x2, f(x2)))

        if abs(f(x2)) <= precision:
            return (True, x2)
        x0 = x1
        x1 = x2

    print("Número máximo de iterações atingido")
    return (True, x2)
   