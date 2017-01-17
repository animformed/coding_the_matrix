from pprint import pprint 
from math import e, pi

def transform(a, b, L):
	result = []
	for c in L:
		result.append(a*c + b)
	return result

a = 3 + 2j
print 'a', a

b = 2 + 3j
print 'b', b

print 'L'
L = \
[(6+3.30789538039j),
(4+2.10735964129j),
(3+7.83487879415j),
(108+4.46941876974j),
(90+7.65527467896j),
(42+10.4434009298j),
(42+14.3005419538j),
(152+8j),
(189+9j),
(80+13.8544970565j)]
pprint(L)

from plotting import plot2
plot2(L)

# 1.7.12
#result = transform(a, b, L)
#print 'result'
#pprint(result)
#plot2(result)

# 1.7.12a
def transform2(L):
	result = []
	for c in L:
		c = complex(1, 1) + c   # move 1, 1
		c = pow(e, complex(0, pi*0.5)) * c   # rotate clockwise 90
		c = c * 2	# scale x2
		result.append(c)
	return result

#result = transform2(L)
#plot2(result)


# 1.7.12b
def transform3(L):
	result = []
	for c in L:
		c = complex(c.real*2.0, c.imag*3.0)
		c = c * e ** complex(0, -pi/4)
		c = complex(-3, -2) + c
		result.append(c)
	return result

result = transform3(L)
plot2(result)