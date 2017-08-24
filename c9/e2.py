def has_no_e(word):
	if 'e' in word:
		return False
	else:
		return True
def print_words_without_e():
	fin=open("words.txt")
	count=0
	total=0
	for line in fin:
		word=line.strip()
		total+=1
		if has_no_e(word):
			print(word)
			count+=1
	print("Percentage of words without e: {:.2%}".format(count/total))
print_words_without_e()
