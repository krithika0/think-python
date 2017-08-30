"""
If there are 23 students in your class, what are the chances that two of you have the same birthday?
You can estimate this probability by generating random samples of 23 birthdays and checking for matches. Hint: you can generate random birthdays with the randint function in the random
module.
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
