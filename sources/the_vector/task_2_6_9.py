from plotting import plot2

def segment(pt1, pt2, segments=100):
	pt1_inc = (pt2[0] - pt1[0]) / segments
	pt2_inc = (pt2[1] - pt1[1]) / segments
	pts = []
	for i in range(segments):
		pts.append((pt1[0]+(i*pt1_inc), pt1[1]+(i*pt1_inc)))
	return pts

pts = segment([3.5, 3], [0.5, 1.0])
print len(pts)
plot2(pts)
