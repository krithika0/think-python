"""
This was sent in by a fellow named Dan O’Leary. He came upon a common one-syllable,
five-letter word recently that has the following unique property. When you remove the
first letter, the remaining letters form a homophone of the original word, that is a word
that sounds exactly the same. Replace the first letter, that is, put it back and remove
the second letter and the result is yet another homophone of the original word. And the
question is, what’s the word?

But there is, however, at least one word that Dan and we know of, which will yield two
homophones if you remove either of the first two letters to make two, new four-letter
words. The question is, what’s the word?

You can use the dictionary from Exercise 11.1 to check whether a string is in the word list.
To check whether two words are homophones, you can use the CMU Pronouncing Dictionary. You
can download it from http: // www. speech. cs. cmu. edu/ cgi-bin/ cmudict or from http:
// thinkpython2. com/ code/ c06d and you can also download http: // thinkpython2.
com/ code/ pronounce. py , which provides a function named read_dictionary that reads the
pronouncing dictionary and returns a Python dictionary that maps from each word to a string that
describes its primary pronunciation.

Write a program that lists all the words that solve the Puzzler
"""
from pronounce import read_dictionary

pron_dict=read_dictionary()

for word in pron_dict:
	if len(word)==5:
		word1=word[1:]
		word2=word[0]+word[2:]
		if word1 in pron_dict and word2 in pron_dict and pron_dict[word]==pron_dict[word1]==pron_dict[word2]:
			print(word,word1,word2)
