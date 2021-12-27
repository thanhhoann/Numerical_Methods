def f(x):
    return x


def Trapezodial(a, b, x_0, x_1):
    return (b-a) * (f(x_0) + f(x_1)) / 2


def Simpson_1_3(a, b, x_0, x_1, x_2):
    return (b-a) * (f(x_0)+4*f(x_1) + f(x_2)) / 6


def Simpson_3_8(a, b, x_0, x_1, x_2, x_3):
    return (b-a) * (f(x_0) + 3*f(x_1) + 3*f(x_2) + f(x_3)) / 8


def Boole(a, b, x_0, x_1, x_2, x_3, x_4):
    return (b-a) * (7*f(x_0) + 32*f(x_1) + 12*f(x_2) + 32*f(x_3) + 7*f(x_4))/90
