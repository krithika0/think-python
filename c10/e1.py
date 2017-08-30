"""
Write a function called nested_sum that takes a list of lists of integers and adds up
the elements from all of the nested lists. For example:
>>> t = [[1, 2], [3], [4, 5, 6]]
>>> nested_sum(t)
21
"""
def nested_sum(t):
	s=0
	for t1 in t:
		s+=sum(t1)
	return s
t = [[1, 2], [3], [4, 5, 6]]
print(t)
print(nested_sum(t))
