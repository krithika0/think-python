"""
Read the documentation of the dictionary method setdefault and use it to write a
more concise version of invert_dict .
"""
from histogram import histogram
def invert_dict(d):
	inverse=dict()
	for i in d:
		inverse.setdefault(d[i],[]).append(i)
	return inverse

s="brontosaurus"
h=histogram(s)
print(h)
i=invert_dict(h)
print(i)
