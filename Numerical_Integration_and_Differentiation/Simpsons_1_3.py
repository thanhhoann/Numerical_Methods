def f(x):
    return 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5


a = 0
b = 0.8
h = (b-a)/2  # or (x_2 - x_0) / 2
exact_integral = 1.640533


def I(x_0, x_1, x_2):
    return h*(f(x_0) + 4*f(x_1) + f(x_2)) / 3


def E_a(b):
    return -((((b)**5) / 2880) * (-2400))


res = I(0, 0.4, 0.8)

print("I = " + str(res))
print("E_t = " + str(exact_integral-res))
print("E_a = " + str(E_a(b)))
print("True error = " + str(E_a(b) / exact_integral * 100) + "%")
