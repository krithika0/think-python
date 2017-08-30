"""
If you did Exercise 10.7, you already have a function named has_duplicates that
takes a list as a parameter and returns True if there is any object that appears more than once in the
list.
Use a dictionary to write a faster, simpler version of has_duplicates .
"""
def has_duplicates(t):
	d={}
	for i in t:
		d[i]=d.get(i,0)+1
		if d[i]>1:
			return True
	return False

t=[8,4,5,8,1]
print(t,has_duplicates(t))
