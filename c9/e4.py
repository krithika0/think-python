def uses_only(word,allowed):
	for c in word:
		if not c in allowed:
			return False
	return True

def words_containing(allowed):
	fin=open("words.txt")
	count=0
	for line in fin:
		word=line.strip()
		if uses_only(word,allowed):
			print(word)
			count+=1
	return count
p=input('Letters? ')
print("Number of words using only the letters {!r} : {}".format(p,words_containing(p)))

