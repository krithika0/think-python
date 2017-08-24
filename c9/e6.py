def is_abecedarian(word):
	prev=ord(word[0])
	for c in word:
		if ord(c)<prev:
			return False
		prev=ord(c)
	return True

def abecedarian_words():
	fin=open("words.txt")
	count=0
	for line in fin:
		word=line.strip()
		if is_abecedarian(word):
			print(word)
			count+=1
	return count
#print(is_abecedarian('abcde'))
print("Number of abecedarian words :",abecedarian_words())

