def avoids(word,forbidden):
	for c in forbidden:
		if c in word:
			return False
	return True
def words_without(forbidden):
	fin=open("words.txt")
	count=0
	for line in fin:
		word=line.strip()
		if avoids(word,forbidden):
			print(word)
			count+=1
	return count
p=input('Forbidden letters? ')
print("Number of words without {!r} : {}".format(p,words_without(p)))

#xyzqw
