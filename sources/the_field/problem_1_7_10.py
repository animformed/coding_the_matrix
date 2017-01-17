from plotting import plot2

cm_set = set([(3+1j), (2+2j)])
#cm_set = set([(-1+2j), (1-1j)])
#cm_set = set([(2+0j), (-3+0.001j)])
#cm_set = set([(0+2j), (0.001+1j)])

print 'cm_set', cm_set
cm_set_add = complex()
for c in cm_set:
	cm_set_add = cm_set_add + c

cm_set.add(cm_set_add)

print cm_set

plot2(cm_set)