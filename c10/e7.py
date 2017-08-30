"""
Write a function called has_duplicates that takes a list and returns True if there
is any element that appears more than once. It should not modify the original list.
"""
def has_duplicates(t):
	t1=t
	t1.sort()
	for i in range(len(t1)):
		if i>0:
			if t1[i]==t1[i-1]:
				return True
	return False
t=[8,9,4,8,1]
print(t)
print(has_duplicates(t))
