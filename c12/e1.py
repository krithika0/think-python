"""
Write a function called most_frequent that takes a string and prints the let-
ters in decreasing order of frequency. Find text samples from several different languages and see
how letter frequency varies between languages. Compare your results with the tables at http:
// en. wikipedia. org/ wiki/ Letter_ frequencies .
"""
import string
def histogram(s):
	d={}
	for i in s.strip().lower():
		if i in string.ascii_lowercase:
			d[i]=(d.get(i,0)+1)
	return d

def invert_dict(d):
	inverse=dict()
	for i in d:
		inverse.setdefault(d[i],[]).append(i)
	return inverse

def most_frequent(s):
	d=invert_dict(histogram(s))
	for i in reversed(sorted(d)):
		print(d[i],i)

with open("les-miserables.txt") as fin:
	s=fin.read()
	most_frequent(s)
