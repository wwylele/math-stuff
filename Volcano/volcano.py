import random
import math
import matplotlib.pyplot as plt

def gen_seq(base):
    l = []
    for i in range(1, 10):
        digit = random.randrange(0, base)
        l += [i] * digit
    return l

def get_x(l, base):
    x = 0.0
    for d in l:
        x += math.pow(base, -d)
    return x

def get_y(l, base):
    y = 0.0
    for k, d in enumerate(l):
        y += math.pow(base, -d) * ((base - 1) * d - 2 * k)
    return y


base = 30
ll = [gen_seq(base) for x in range(1000)]
x = [get_x(l, base) for l in ll]
y = [get_y(l, base)/base for l in ll]

plt.plot(x, y, 'r.')
plt.show()
