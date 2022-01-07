from __future__ import division
from math import sqrt

x_from = 0
x_to = 1
h = 0.25
x_0 = 0
y_0 = 1


def f(x, y):
    return (1+4*x)*sqrt(y)


def F(x, y):
    return ((x+2*x**2 + 2)/2)**2


def range_helper(start, stop, step=1):  # range() doesn't allow float steps, this helps
    n = int(round((stop - start)/float(step)))
    if n > 1:
        return([start + step*i for i in range(n+1)])
    elif n == 1:
        return([start])
    else:
        return([])


steps = (range_helper(x_from, x_to, h))


def cal_y_true():
    y_true_old = y_0

    print('x\ty_true')
    for i in range(0, steps.__len__()):
        y_true = F(steps[i], y_true_old)

        print('%s %10s' % (steps[i], round(y_true, 3)))

        y_true_old = y_true


def cal_y_Heun():
    print('y_Heun')
    y_old = y_0
    i_old = 0
    i_current = 0
    print(1)
    for i in range(0, steps.__len__()):
        i_old = steps[i]
        i_current = steps[i] + h

        if (i_current > x_to):
            break

        k_1 = f(i_old, y_old)
        k_2 = f(i_old + h, y_old + h * k_1)

        y_Heun = y_old + ((1/2)*k_1 + (1/2)*k_2)*h

        print(str(round(y_Heun, 3)))

        y_old = y_Heun


cal_y_true()
print('')
cal_y_Heun()
