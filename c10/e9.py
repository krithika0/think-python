"""
Write a function that reads the file words.txt and builds a list with one element per word. Write two versions of this function, one using the append method and the other using the idiom t = t + [x] . Which one takes longer to run? Why?
"""
def make_list1():
	t=[]
	with open("../c9/words.txt") as fin:
		for line in fin:
			t.append(line)
	return t
def make_list2():
	t=[]
	with open("../c9/words.txt") as fin:
		for line in fin:
			t=t+[line]
	return t
t1=make_list1()
print("Made list 1")
print(t1)
t2=make_list2()
print("Made list 2")
"""
make_list2 takes much longer to run, because a new list is created whenever an element is added.
"""
