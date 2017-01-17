from GF2 import one, zero

def n_encode(*args):
	if not len(args) in (1, 2):
		raise RuntimeError('Invalid bit pair for n encoding. Cannot proceed.')
	if len(args) == 2:
		return (args[0]+args[1], True)
	return (args[0], False)

def n_decode(*args):
	if not len(args) in (1, 2):
		raise RuntimeError('Invalid bit pair for n decoding. Cannot proceed.')
	b1, b1_gf2_sum = args[0][0], args[0][1]
	if len(args) == 2:
		b2, b2_gf2_sum = args[1][0], args[1][1]
		if b1_gf2_sum and b2_gf2_sum:
			raise RuntimeError('Incorrect bit pair for n decoding. Both are GF2 encoded.')
		if b1_gf2_sum:
			b1 = b1 + b2
		if b2_gf2_sum:
			b2 = b1 + b2
		return b1, b2
	return b1



# Source 
b1 = one
b2 = zero

# node1
N1_out = b1

# node 2
N2_out = b2

# node 3
N3_out = n_encode(N1_out, N2_out)

# node 4
N4_out = N3_out

print 'N4_out', N4_out
# C 
b1 = n_encode(b1)
C_in = n_decode(b1, N4_out)

# D
D_in = n_decode(N4_out)

