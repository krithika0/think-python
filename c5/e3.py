def is_triangle(a,b,c):
	if a>b+c or b>a+c or c>a+b:
		print("No")
	else:
		print("Yes")
def take_input():
	a=int(input("Enter the length of the first stick: "))
	b=int(input("Enter the length of the second stick: "))
	c=int(input("Enter the length of the third stick: "))
	is_triangle(a,b,c)
take_input()
