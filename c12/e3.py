"""
Two words form a “metathesis pair” if you can transform one into the other by
swapping two letters; for example, “converse” and “conserve”. Write a program that finds all of
the metathesis pairs in the dictionary. Hint: don’t test all pairs of words, and don’t test all possible
swaps.
"""
def different_letters_in(s1,s2):
	diff_count=0
	for a,b in zip(s1,s2):
		if a!=b:
			diff_count+=1;
	return diff_count

def make_dict_anagrams():
	d={}
	with open("../c9/words.txt") as fin:
		for line in fin:
			word=line.strip()
			d.setdefault((tuple(sorted(word))),[]).append(word)
	return d

def print_metathesis_pairs():
	d=make_dict_anagrams()
	for words in d.values():
		if len(words)>2:
			t=[(words[i],words[j]) for i in range(len(words)) for j in range(i+1, len(words))]
			for a,b in t:
				if different_letters_in(a,b)==2:
					print(a,b)

print_metathesis_pairs()
