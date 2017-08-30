"""
def histogram(s):
	d = dict()
	for c in s:
		if c not in d:
			d[c] = 1
		else:
			d[c] += 1
	return d
As an exercise, use get to write histogram more concisely. You should be able to eliminate
the if statement.
"""
def histogram(s):
	d=dict()
	for c in s:
		d[c]=d.get(c,0)+1
	return d
if __name__=='__main__':
	s="brontosaurus"
	print(s,histogram(s))
