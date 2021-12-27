def f(x):
    return 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5


a = 0
b = 0.8
h = (b-a)/3  # or (x_3 - x_0)/3
exact_integral = 1.640533


def I(x_0, x_1, x_2, x_3):
    return ((3*h) * (f(x_0) + 3*(f(x_1) + f(x_2)) + f(x_3))) / 8


def E_a(b):
    return -((((b)**5) / 6480) * (-2400))


res = I(0, 0.2667, 0.5333, 0.8)

print("I = " + str(res))
print("E_t = " + str(exact_integral-res))
print("E_a = " + str(E_a(b)))
print("True error = " + str(E_a(b) / exact_integral * 100) + "%")
