"""
Write a function that reads the words in words.txt and stores them as keys in a
dictionary. It doesn’t matter what the values are. Then you can use the in operator as a fast way to
check whether a string is in the dictionary.
If you did Exercise 10.10, you can compare the speed of this implementation with the list in operator
and the bisection search.
"""
import bisect
import time
def words_dict():
	d=dict()
	with open("../c9/words.txt") as fin:
		for line in fin:
			d[line.strip()]=1
	return d

def words_list():
	with open("../c9/words.txt") as fin:
		t=[i.strip() for i in fin]
		return t

def in_list_bisect(t,word):
	i=bisect.bisect_left(t,word)
	if i!=len(t) and t[i]==word:
		return True
	return False

t=words_list()
d=words_dict()
word="dinosaur"
print("using list in operator")
start=time.time()
if word in t:
	print("word found")
	print(time.time()-start)
print("using list bisection search")
start=time.time()
if in_list_bisect(t,word):
	print("word found")
	print(time.time()-start)
print("using dict in operator")
start=time.time()
if word in d:
	print("word found")
	print(time.time()-start)
