from __future__ import division
x_from = 0
x_to = 4
h = 0.5
x_0 = 0
y_0 = 1


def f(x, y):
    return (-2)*x**3 + 12*x**2 - 20*x + 8.5


def F(x, y):
    return (-0.5)*x**4 + (4)*x**3 - (10)*x**2 + 8.5*x + 1  # C = 1


def range_helper(start, stop, step=1):  # range() doesn't allow float steps, this helps
    n = int(round((stop - start)/float(step)))
    if n > 1:
        return([start + step*i for i in range(n+1)])
    elif n == 1:
        return([start])
    else:
        return([])


steps = (range_helper(x_from, x_to, h))


def Ralston_Method():
    y_Ralston_old = y_0
    y_true_old = y_0

    print('x\ty_true\ty_Ralston')
    for i in range(0, steps.__len__()):
        x_i = steps[i]
        k_1 = f(x_i, y_Ralston_old)

        k_2_x = x_i + (3/4)*h
        k_2_y = y_Ralston_old * k_1 * h
        k_2 = f(k_2_x, k_2_y)

        #  print('k_1 = {} | k_2 = {}'.format(k_1, k_2))

        y_Ralston = y_Ralston_old + ((1/3)*k_1 + (2/3)*k_2)*h
        y_true = F(steps[i], y_true_old)

        print('%s %10s %8s' % (x_i, y_true, y_Ralston_old))

        y_Ralston_old = y_Ralston
        y_true_old = y_true


Ralston_Method()
