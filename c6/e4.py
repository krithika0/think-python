def is_power(a,b):
	if a==0 or a==b:
		return True
	elif b==1 or a%b!=0:
		return False
	else:
		return is_power(a/b,b)
print(4,2,is_power(4,2))
print(64,3,is_power(64,3))
print(72,3,is_power(72,3))
print(81,3,is_power(81,3))
print(-8,-2,is_power(-8,-2))
print(-8,2,is_power(-8,2))
print(8,-2,is_power(8,-2))
print(8,1,is_power(8,1))
