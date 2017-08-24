def uses_all(word,required):
	for c in required:
		if not c in word:
			return False
	return True

def words_using_all(required):
	fin=open("words.txt")
	count=0
	for line in fin:
		word=line.strip()
		if uses_all(word,required):
			print(word)
			count+=1
	return count
p=input('Required letters? ')
print("Number of words using all the letters {!r} : {}".format(p,words_using_all(p)))

