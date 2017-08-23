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
print('cubed',10,rotate_word('cubed',10))
print('abcde',-3,rotate_word('abcde',-3))
