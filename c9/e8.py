def is_palindrome(a):
	if a[::-1]==a:
		return True
	else:
		return False
def puzzle():
	i=0
	while i<1000000:
		if is_palindrome("{:0>4}".format(i%10000)) and is_palindrome("{:0>5}".format((i+1)%100000)) and is_palindrome("{:0>4}".format(((i+2)//10)%10000)) and is_palindrome("{:0>6}".format((i+3)%1000000)):
			print(i)
		i+=1
def puzzle1():
	i=100000
	while i<1000000:
		if is_palindrome(str(i)[2:6]) and is_palindrome(str(i+1)[1:6]) and is_palindrome(str(i+2)[1:5]) and is_palindrome(str(i+3)):
			print(i)
		i+=1
puzzle()
puzzle1()

