def recurse(n, s):
	"""
	Calculates sum of 1st n numbers recursively and prints sum+s

	n must be non-negative
	"""
	if n == 0:
		print(s)
	else:
		recurse(n-1, n+s)
for n in range(10):
	for s in range(10):
		print("n=",n,"s=",s)
		print(s+(n+1)*n/2,end=' ')
		recurse(n,s)
		
