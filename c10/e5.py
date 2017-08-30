"""
Write a function called is_sorted that takes a list as a parameter and returns True
if the list is sorted in ascending order and False otherwise. For example:
>>> is_sorted([1, 2, 2])
True
>>> is_sorted(['b', 'a'])
False
"""
def is_sorted(t):
	for i in range(len(t)):
		if i>0:
			if(t[i]<t[i-1]):
				return False
	return True
t=[1,2,2]
print(t,is_sorted(t))
t2=['b','a']
print(t2,is_sorted(t2))
