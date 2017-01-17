from math import pi, e

#pw_set = set([(0+1j), (0+2j)])
#pw_set = set([complex(0, pi/4), complex(0, (2*pi)/3)])
pw_set = set([complex(0, -pi/4), complex(0, (2*pi)/3)])

print 'pw_set', pw_set

pw_sum = complex()
for c in pw_set:
	pw_sum = pw_sum + c

print 'pw_sum', pw_sum
print 'E pow', pow(e, pw_sum)