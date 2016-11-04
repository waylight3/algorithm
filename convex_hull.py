import sys, math

def ccw(p0, p1, p2):
	return (p1[1] - p0[1]) * (p2[0] - p0[0]) - (p2[1] - p0[1]) * (p1[0] - p0[0])

def dist(p1, p2):
	return math.sqrt((p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1]))

def convex_hull(p):
	n = len(p)
	p = sorted(p)
	p = [p[0]] + sorted(p[1:], key=lambda v: (v[1] - p[0][1]) / dist(v, p[0]))
	conv = [p[0], p[1]]
	to = 2
	while to < n:
		while len(conv) >= 2:
			p1 = conv[-2]
			p2 = conv[-1]
			conv.pop()
			if ccw(p1, p2, p[to]) < 0:
				conv.append(p2)
				break
		conv.append(p[to])
		to += 1
	return conv
