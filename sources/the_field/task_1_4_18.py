from math import e, pi
from plotting import plot2

S = {2+2j, 3+2j, 1.75+1j, 2+1j, 2.25+1j, 2.5+1j, 2.75+1j, 3+1j, 3.25+1j}

a = pi / 4.0

pts = [c * (e ** complex(0, (pi/4))) for c in S]

plot2(pts, range=6)