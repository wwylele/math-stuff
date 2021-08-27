import scipy.integrate;
import numpy;


def f2(xs):
    def g(a):
        b = numpy.arccosh(1/numpy.cos(a))
        return (1-numpy.exp(-b * abs(xs[0]-xs[1])) * numpy.cos(a * (xs[0] + xs[1]))) / (2 * numpy.pi * numpy.sin(a))
    return scipy.integrate.quad(g, 0, numpy.pi/2)[0]


def f(xs):
    n = len(xs)
    coef = 2 * (2 * numpy.pi)**(n - 1)
    def g(*args):
        a = numpy.arccosh(n - sum(numpy.cos(args)))
        return (1 - numpy.exp(-a*abs(xs[n-1])) * numpy.cos(sum([xs[i] * args[i] for i in range(n-1)])) ) / (coef * numpy.sinh(a))
    return scipy.integrate.nquad(g, [[0, 2*numpy.pi]] * (n - 1))[0]

def f_sym(xs):
    n = len(xs)
    X = numpy.array(xs)
    def f(*args):
        T = numpy.array(args)
        up = numpy.sin(numpy.sum(T * X))**2
        down = numpy.sum(numpy.sin(T)**2)
        return up/down 

    return scipy.integrate.nquad(f, [[0, numpy.pi]] * n)[0] / (numpy.pi) ** n / 2

P = [1,-2]

def I(xs):
    n = len(xs)
    return sum([ f(xs[0:i] + [xs[i]-1] + xs[i+1:n]) + f(xs[0:i] + [xs[i]+1] + xs[i+1:n]) for i in range(n) ]) - f(xs) * n * 2


print(f2(P))
print(f(P))
print(f_sym(P))
print(f"{I(P):f}")
print("====")

for y in range(-5, 6):
    for x in range(-5, 6):
        print(f"{f_sym([x,y]):+.5f}   ", end = '')
    print("")