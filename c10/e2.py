"""
Write a function called cumsum that takes a list of numbers and returns the cumu-
lative sum; that is, a new list where the ith element is the sum of the first i + 1 elements from the
original list. For example:
>>> t = [1, 2, 3]
>>> cumsum(t)
[1, 3, 6]
"""
def cumsum(t):
	for i in range(len(t)):
		if i>0:
			t[i]+=t[i-1]
	return t
t = [1,2,3]
print(t)
print(cumsum(t))
		
