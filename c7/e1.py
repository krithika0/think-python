import math
def mysqrt(a):
	x=a
	epsilon=0.00000001
	while True:
		#print("x",x)
		y = (x + a/x) / 2
		#print("y",y)
		if -epsilon<x-y<epsilon:
			return y
		x=y
def test_square_root():
	print('a'+' '*2,'mysqrt(a)'+' '*5,'math.sqrt(a)'+' '*2,'diff')
	print('-'+' '*2,'-'*9+' '*5,'-'*12+' '*2,'-'*4)
	a=1.0
	while a<=9:
		m=round(mysqrt(a),11)
		n=round(math.sqrt(a),11)
		diff=abs(mysqrt(a)-math.sqrt(a))
		print(a,m,' '*(13-len(str(m))),n,' '*(13-len(str(n))),diff)
		a=a+1.0
test_square_root()
