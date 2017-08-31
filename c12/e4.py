"""
What is the longest English word, that remains a valid English word, as you remove its letters one at a time?
Now, letters can be removed from either end, or the middle, but you can’t rearrange any of the letters. Every time you drop a letter, you wind up with another English word. If you do that, you’re eventually going to wind up with one letter and that too is going to be an English word—one that’s found in the dictionary. I want to know what’s the longest word and how many letters does it have?

Sprite->spite->spit->pit->it->I

Write a program to find all words that can be reduced in this way, and then find the longest one.

This exercise is a little more challenging than most, so here are some suggestions:
1. You might want to write a function that takes a word and computes a list of all the words that can be formed by removing one letter. These are the “children” of the word.
2. Recursively, a word is reducible if any of its children are reducible. As a base case, you can consider the empty string reducible.
3. The wordlist I provided, words.txt , doesn’t contain single letter words. So you might want to add “I”, “a”, and the empty string.
4. To improve the performance of your program, you might want to memoize the words that are known to be reducible.
"""

with open("../c9/words.txt") as fin:
	d={i.strip():1 for i in fin}
d['']=1
d['a']=1
d['i']=1

r={'':0}

def invert_dict(d):
	inverse={}
	for i in d:
		inverse.setdefault(d[i],[]).append(i)
	return inverse

def children(word):
	t=[]
	for i in range(len(word)):
		sub=word[:i]+word[i+1:]
		if sub in d:
			t.append(sub)
	return t

def is_reducible(word):
	if word in r:
		return True
	c=children(word)
	for i in c:
		if is_reducible(i):
			r[word]=len(word)	
			return True
	return False

def print_reduction(word):
	if word=='i' or word=='a':
		print(word)
		return
	c=children(word)
	print(word,end="->")
	for i in c:
		if i in r:
			print_reduction(i)
			return

def print_reducible_words():
	i=invert_dict(r)
	print(i)
	for num in sorted(i):
		for word in i[num]:
			print_reduction(word)

for word in d:
	is_reducible(word)
print_reducible_words()
