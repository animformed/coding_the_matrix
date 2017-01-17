def my_filter(L, num):
	return [x for x in L if x % num]

print 'my_filter', my_filter([1, 2, 4, 5, 7], 2)


def my_lists(L):
	return [range(1, x+1) for x in L]

print 'my_lists', my_lists([1, 2, 4])
print 'my_lists', my_lists([0])


def my_function_composition(f, g):
	return {f_key: g[f_val] for f_key, f_val in f.items()}

print 'my_function_composition', my_function_composition({0:'a', 1:'b'}, {'a':'apple', 'b':'banana'})


def mySum(L):
	current = 0
	for x in L:
		current = current + x
	return current

def myProduct(L):
	current = 1.0
	for x in L:
		current = current * x
	return current

def myMin(L):
	current = 0
	for x in L:
		current = x if x < current else current
	return current

def myConcat(L):
	current = ''
	for x in L:
		current = current + x
	return current

def myUnion(L):
	current = set()
	for x in L:
		current = current.union(x)
	return current

print 'myUnion', myUnion([set([1, 2, 3]), set(['F', 'G', 'H']), set([3, 7, 9])])
