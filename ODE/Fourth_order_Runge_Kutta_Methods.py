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


def Fourth_order_RK_Method():
    y_old = y_0
    y_true_old = y_0

    print('x\ty_true\ty_Fourth_order_RK')
    for i in range(0, steps.__len__()):
        x_i = steps[i]
        y_true = F(steps[i], y_true_old)

        k_1 = f(x_i, y_old)
        k_2 = f(x_i + (1/2)*h, y_old + (1/2) * k_1 * h)
        k_3 = f(x_i + (1/2)*h, y_old + (1/2) * k_2 * h)
        k_4 = f(x_i + h, y_old + k_3 * h)

        _y = y_old + (1/6)*(k_1 + 2*k_2 + 2*k_3 + k_4)*h

        print('%s %10s %8s' % (x_i, y_true, y_old))

        y_old = _y
        y_true_old = y_true


Fourth_order_RK_Method()
