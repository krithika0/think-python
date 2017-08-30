"""
Two words “interlock” if taking alternating letters from each forms a new
word. For example, “shoe” and “cold” interlock to form “schooled”. 

1. Write a program that finds all pairs of words that interlock. Hint: don’t enumerate all pairs!
2. Can you find any words that are three-way interlocked; that is, every third letter forms a
word, starting from the first, second or third?
"""
import bisect
def in_list(t,word):
	a=bisect.bisect_left(t,word)
	if a!=len(t) and t[a]==word:
		return True
	else:
		return False
def print_interlocked(t):
	for word in t:
		word1=word[::2]
		word2=word[1::2]
		if in_list(t,word1) and in_list(t,word2):
			print(word1,word2,word)
def print_interlocked3(t):
	for word in t:
		if len(word)>2:
			word1=word[::3]
			word2=word[1::3]
			word3=word[2::3]
			if in_list(t,word1) and in_list(t,word2) and in_list(t,word3):
				print(word1,word2,word3,word)
with open("../c9/words.txt") as fin:
	t=[i.strip() for i in fin]
	print_interlocked(t)
	print_interlocked3(t)
