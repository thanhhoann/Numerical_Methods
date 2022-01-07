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


def Euler_Method():
    y_Euler_old = y_0
    y_true_old = y_0

    print('x\ty_true\ty_Euler')
    for i in range(0, steps.__len__()):
        y_true = F(steps[i], y_true_old)
        y_Euler = y_Euler_old + f(steps[i], y_Euler_old) * h

        print('%s %10s %8s' % (steps[i], y_true, y_Euler_old))

        y_Euler_old = y_Euler
        y_true_old = y_true


Euler_Method()
