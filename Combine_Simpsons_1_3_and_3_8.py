def f(x):
    return 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5


a = 0
b = 0.8
n = 5  # number of segments
h = (b-a)/n


def x_i(i):
    return a + i*h


for i in range(0, 6):
    print("x_" + str(i) + " = " + str(x_i(i)))

print("")

for i in range(0, 6):
    print("f(" + str(x_i(i)) + ") = " + str(f(x_i(i))))


'''
The integral for the first 2 segments can be obtained using Simpson's 1/3 Rule.
'''


def I_1_3(x_0, x_1, x_2):
    return (h/3) * (f(x_0) + 4*f(x_1) + f(x_2))


i_1 = I_1_3(x_i(0), x_i(1), x_i(2))

print("\nUsing Simpson's 1/3 Rule: ")
print("I = " + str(i_1))

'''
For the last 3 segments, the Simpson's 3/8 Rule can be used to obtain the result.
'''


def I_3_8(x_2, x_3, x_4, x_5):
    return ((3*h)/8) * (f(x_2) + 3*(f(x_3) + f(x_4)) + f(x_5))


i_2 = I_3_8(x_i(2), x_i(3), x_i(4), x_i(5))

print("\nUsing Simpson's 3/8 Rule: ")
print("I = " + str(i_2))

'''
The total integral is computed by using the sum of previous results.
'''

print("\nTotal Integral: ")
print("I = " + str(i_1+i_2))
