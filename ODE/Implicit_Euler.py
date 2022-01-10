from math import exp, sqrt
_from = 0
_to = 0.4
h = 0.05
x_0 = 0
y_0 = 0


def f(x, y):  # dy/dx
    return -1000*y + 3000 - 2000*exp(-x)


def F(x, y):
    # bring all y to the left (if has) and cal the integral
    # x = x_0, y = y_0 to x = x, y = y
    return sqrt(6*x + 4*(exp(-x)-1))


def range_helper(start, stop, step=1):  # range() doesn't allow float steps, this helps
    n = int(round((stop - start)/float(step)))
    if n > 1:
        return([start + step*i for i in range(n+1)])
    elif n == 1:
        return([start])
    else:
        return([])


steps = (range_helper(_from, _to, h))


def Euler_Method():
    y_Euler_old = y_0
    y_true_old = y_0

    print('x\ty_true\ty_Euler')
    for i in range(0, steps.__len__()):
        y_true = F(steps[i], y_true_old)

        y_Euler = (y_Euler_old + 3000*h - 2000*h *
                   exp(steps[i]+1)) / (1 + 1000*h)

        print('%s %10s %8s' % (steps[i], y_true, y_Euler_old))

        y_Euler_old = y_Euler
        y_true_old = y_true


Euler_Method()
