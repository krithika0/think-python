import math
def estimate_pi():
	sum=0
	k=0
	while True:
		numerator=math.factorial(4*k)*(1103+26390*k)
		denominator=(math.factorial(k)**4)*(396**(4*k))
		term=numerator/denominator
		sum+=term
		if(term<1e-15):
			break
		k=k+1
	sum=sum*2*math.sqrt(2)/9801
	return sum
print('estimate of 1/pi:',estimate_pi())
print('1/math.pi:',1/math.pi)
print('difference:',abs(estimate_pi()-1/math.pi))
