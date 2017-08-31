"""
1. Write a program that reads a word list from a file (see Section 9.1) and prints all the sets of
words that are anagrams.
Here is an example of what the output might look like:
['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
['retainers', 'ternaries']
['generating', 'greatening']
['resmelts', 'smelters', 'termless']
Hint: you might want to build a dictionary that maps from a collection of letters to a list
of words that can be spelled with those letters. The question is, how can you represent the
collection of letters in a way that can be used as a key?
2. Modify the previous program so that it prints the longest list of anagrams first, followed by
the second longest, and so on.
3. In Scrabble a “bingo” is when you play all seven tiles in your rack, along with a letter on
the board, to form an eight-letter word. What collection of 8 letters forms the most possible
bingos? Hint: there are seven.
"""
def make_dict_anagrams():
	d={}
	with open("../c9/words.txt") as fin:
		for line in fin:
			word=line.strip()
			d.setdefault((tuple(sorted(word))),[]).append(word)
	return d

def print_anagrams():
	d=make_dict_anagrams()
	for chars in d:
		if len(d[chars])>1:
			print(d[chars])

def print_anagrams_sorted():
	d=make_dict_anagrams()
	t=[]
	for words in d.values():
		if len(words)>1:
			t.append((len(words),words))
	for i in reversed(sorted(t)):
		print(i)

def print_bingo():
	d=make_dict_anagrams()
	t=[]
	for chars,words in d.items():
		if len(words)>1 and len(chars)==8:
			t.append((len(words),words))
	for i in reversed(sorted(t)):
		print(i)

#print_anagrams_sorted()
print_bingo()
