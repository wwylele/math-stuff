import math

a = [0]
d = 1

for n in range(20):
    l = sum([math.sqrt(x*x + 1) for x in a]) / d
    print(l)
    d *= 2
    a = [x - 1 for x in a] + [x + 1 for x in a]