def any_lowercase1(s):
	"""
	Returns True if starting character is lowercase
	"""
	for c in s:
		if c.islower():
			return True
		else:
			return False
def any_lowercase2(s):
	"""
	Returns True if the character 'c' is lowercase 
	Always returns True
	"""
	for c in s:
		if 'c'.islower():
			return 'True'
		else:
			return 'False'
def any_lowercase3(s):
	"""
	Returns True if ending character is lowercase
	"""
	for c in s:
		flag = c.islower()
	return flag
def any_lowercase4(s):
	"""
	Returns True if at least one character is lowercase
	"""
	flag = False
	for c in s:
		flag = flag or c.islower()
	return flag
def any_lowercase5(s):
	"""
	Returns True if at least all characters are lowercase
	"""
	for c in s:
		if not c.islower():
			return False
	return True
print('bANANA',1,any_lowercase1('bANANA'))
print('BaNANA',1,any_lowercase1('BaNANA'))
print('BANANA',2,any_lowercase2('BANANA'))
print('bANANA',3,any_lowercase3('bANANA'))
print('BANANa',3,any_lowercase3('BANANa'))
print('bANANA',4,any_lowercase4('bANANA'))
print('BANANa',4,any_lowercase4('BANANa'))
print('BaNANA',4,any_lowercase4('BaNANA'))
print('bANANA',5,any_lowercase5('bANANA'))
print('BANANa',5,any_lowercase5('BANANa'))
print('BaNANA',5,any_lowercase5('BaNANA'))
print('banana',5,any_lowercase5('banana'))
