def f(x):
    return 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5


a = 0
b = 0.8


def Trapezodial_integral(a, b, number_of_segments):
    h = (b-a)/number_of_segments
    x = a

    In = f(a)
    for _ in range(1, number_of_segments):
        x = x + h
        In += 2*f(x)

    return (In + f(b))*h*0.5


def I_j_2(i_first, i_last):
    return (4*i_first - i_last) / 3


def I_j_3(i_first, i_last):
    return (16*i_first - i_last) / 15


def I_j_4(i_first, i_last):
    return (64*i_first - i_last) / 63


print("Segments\th\tIntegral")
print("--------------------------------")
h = b
for i in range(0, 5):
    n = 2**i
    print("%4s\t%9s\t%8s" % (n, h, Trapezodial_integral(0, 0.8, n)))
    h /= 2

print("\nLevel 1, k = 1, O(h^2)")
i_1_1 = Trapezodial_integral(0, b, 1)
i_2_1 = Trapezodial_integral(0, b, 2)
i_3_1 = Trapezodial_integral(0, b, 4)
i_4_1 = Trapezodial_integral(0, b, 8)
i_5_1 = Trapezodial_integral(0, b, 16)
print("I_1_1 = " + str(i_1_1))
print("I_2_1 = " + str(i_2_1))
print("I_3_1 = " + str(i_3_1))
print("I_4_1 = " + str(i_4_1))
print("I_5_1 = " + str(i_5_1))

print("\nLevel 2, k = 2, O(h^4)")
i_1_2 = I_j_2(i_2_1, i_1_1)
i_2_2 = I_j_2(i_3_1, i_2_1)
i_3_2 = I_j_2(i_4_1, i_3_1)
print("I_1_2 = " + str(i_1_2))
print("I_2_2 = " + str(i_2_2))
print("I_3_2 = " + str(i_3_2))

print("\nLevel 3, k = 3, O(h^6)")
i_1_3 = I_j_3(i_2_2, i_1_2)
i_2_3 = I_j_3(i_3_2, i_2_2)
print("I_1_3 = " + str(i_1_3))
print("I_2_3 = " + str(i_2_3))

print("\nLevel 4, k = 4, O(h^8)")
i_1_4 = I_j_4(i_2_3, i_1_3)
print("I_1_4 = " + str(i_1_4))
