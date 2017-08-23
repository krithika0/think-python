def first(word):
	return word[0]
def last(word):
	return word[-1]
def middle(word):
	return word[1:-1]
def is_palindrome(word):
	if len(word)==0 or len(word)==1:
		return True
	elif first(word)==last(word):
		return is_palindrome(middle(word))
	else:
		return False

print(middle('abc'))
#prints b
print(middle('df'))
#prints empty string
print(middle('g'))
#prints empty string
print(middle(''))
#prints empty string
print(is_palindrome('kayak'))
print(is_palindrome(''))
print(is_palindrome('noon'))
print(is_palindrome('aa'))
print(is_palindrome('b'))
print(is_palindrome('apple'))
print(is_palindrome('ab'))
