def newton(x0: int, precision: float, f, f_linha, max_iter=50):
    """
    Implements newton method for finding function root.

    Args:
        a, b (int): Xs coordinates which is know there is a in between
        precision: function root precision
        f (lambda function): Function to find the root
    """
    if abs(f(x0)) <= precision:
        return (False, x0)

    print("i\t x\t\t f(x)\t\t f'(x)")
    print("{}\t {:e}\t {:e}\t {:e}".format(0, x0, f(x0), f_linha(x0)))
    # print("-\t{:e}\t{:e}".format(x1, f(x1)))

    for i in range(1, max_iter+1):
        x1 = x0 - f(x0) / f_linha(x0)
        print("{}\t {:e}\t {:e}\t {:e}".format(i, x0, f(x0), f_linha(x0)))

        if abs(f(x1)) <= precision:
            return (False, x1)
        x0 = x1

    print("Número máximo iterações atingido")
    return (True, x1)
