"""
Memoize the Ackermann function from Exercise 6.2 and see if memoization
makes it possible to evaluate the function with bigger arguments. Hint: no.
"""
known={}
def ack(m,n):
	if [m,n] in known:
		return known[m,n]
	if m==0:
		known[m,n]=n+1
	else:
		if m>0 and n==0:
			known[m,n]=ack(m-1,1)
		elif m>0 and n>0:
			known[m,n]=ack(m-1,ack(m,n-1))
	return known[m,n]

print(3,4,ack(3,4))
#print(30,40,ack(30,40))
#Maximum recursion depth reached
