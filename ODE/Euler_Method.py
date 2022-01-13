_from = 0
_to = 2
h = 0.25
x_0 = 0
y_0 = 1


def f(x, y):
    return y*x**3 - 1.5*y


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


steps = (range_helper(_from, _to, h))


def Euler_Method():
    y_Euler_old = y_0
    y_true_old = y_0

    print('t\ty_true\ty_Euler\t\tf(t,y)')
    for i in range(0, steps.__len__()):
        y_true = F(steps[i], y_true_old)
        y_Euler = y_Euler_old + f(steps[i], y_Euler_old) * h
        f_t_y = f(steps[i], y_Euler_old)

        print('%s %10s %10s %10s' %
              (steps[i], round(y_true, 3), round(y_Euler_old, 4), round(f_t_y, 4)))

        y_Euler_old = y_Euler
        y_true_old = y_true


Euler_Method()
