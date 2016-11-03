from math import e, pi
from plotting import plot2

n = 20

def comp(inp):
    if inp:
        return (2*pi)/inp
    else:
        return 0

def ei_comp(x):
    cm = e ** complex(0, comp(x))
    return cm.real, cm.imag

pts = [ei_comp(x) for x in range(n)]
plot2(pts, rev=False)