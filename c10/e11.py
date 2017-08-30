"""
Two words are a “reverse pair” if each is the reverse of the other. Write a program
that finds all the reverse pairs in the word list.
"""
import bisect
with open("../c9/words.txt") as fin:
	t=[i.strip() for i in fin]
	for i in t:
		r=i[::-1]
		a=bisect.bisect_left(t,r)
		if a!=len(t) and t[a]==r:
			print(a,i,r)
