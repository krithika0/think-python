"""
Two words are “rotate pairs” if you can rotate one of them and get the other (see
rotate_word in Exercise 8.5).
Write a program that reads a wordlist and finds all the rotate pairs.
"""
def rotate_word(s,n):
	r=''
	for c in s:
		if c.isupper():
			base=ord('A')
		else:
			base=ord('a')
		newchar=ord(c)+n
		if(newchar<base+0):
			newchar+=26
		elif(ord(c)+n>base+25):
			newchar-=26
		r+=chr(newchar)
	return r

def words_dict():
	with open("../c9/words.txt") as fin:
		d={line.strip():1 for line in fin}
		return d

d=words_dict()
for word in d:
	for i in range(1,14):
		if rotate_word(word,i) in d:
			print(word,i,rotate_word(word,i))
