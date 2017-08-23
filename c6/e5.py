def gcd(a,b):
	if(b==0):
		return a
	else:
		r=a%b
		return gcd(b,r)
print(3,2,gcd(3,2))
print(9,6,gcd(9,6))
print(42,28,gcd(42,28))
print(19*5,19*4,gcd(19*5,19*4))
