def has_three_double(word):
	if len(word)<6:
		return False
	i=0
	count=0
	while i<len(word)-1:
		if(word[i]==word[i+1]):
			count+=1
			if(count>=3):
				return True
			i+=2
		else:
			count=0
			i+=1
	return False
def has_three_double_words():
	fin=open("words.txt")
	count=0
	for line in fin:
		word=line.strip()
		if has_three_double(word):
			print(word)
			count+=1
	return count
print("Number of words with three consecutive double letters:",has_three_double_words())

