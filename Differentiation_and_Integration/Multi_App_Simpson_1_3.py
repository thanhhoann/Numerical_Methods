def f(x):
    return 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5


a = 0
b = 0.8
n = 4
h = (b-a)/n
exact_integral = 1.640533


def I(x_0, x_1, x_2, x_3, x_4):
    return (b-a) * (f(x_0) + 4*(f(x_1)+f(x_3)) + 2*f(x_2) + f(x_4)) / (3*n)


res = I(0, 0.2, 0.4, 0.6, 0.8)
print("I = " + str(res))

E_t = exact_integral - res
print("E_t = " + str(E_t))
E_a = -((0.8**5)/(180*4**4)) * (-2400)
print("E_a = " + str(E_a))
print("True error = " + str(E_t/exact_integral*100) + "%")
