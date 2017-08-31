"""
Many of the built-in functions use variable-length argument tuples. For example, max and
min can take any number of arguments:
>>> max(1, 2, 3)
3
But sum does not.
>>> sum(1, 2, 3)
TypeError: sum expected at most 2 arguments, got 3
As an exercise, write a function called sumall that takes any number of arguments and
returns their sum.
"""
def sumall(*args):
	s=0
	for i in args:
		s+=i
	return s
print(sumall(3,4,5,6,7))
