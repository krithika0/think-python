"""
Two words are anagrams if you can rearrange the letters from one to spell the other.
Write a function called is_anagram that takes two strings and returns True if they are anagrams.
"""
def is_anagram(s1,s2):
	if len(s1)!=len(s2):
		return False
	t1=list(s1)
	t2=list(s2)
	t1.sort()
	t2.sort()
	if(t1==t2):
		return True
	else:
		return False
print("eastern","nearest",is_anagram("eastern","nearest"))
