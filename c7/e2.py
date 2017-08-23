import math
def eval_loop():
	while True:
		s=input("> ")
		if(s=='done'):
			break
		o=eval(s)
		print(o)
	return o
ret=eval_loop()
print("The value of the last expression evaluated is",ret) 
