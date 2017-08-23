>>> fruit='banana'
>>> fruit[:3]
'ban'
>>> fruit[:-1]
'banan'
>>> fruit[:]
'banana'
>>> fruit.capitalize()
'Banana'
>>> fruit.center(23)
'         banana        '
>>> fruit.center(5)
'banana'
>>> fruit.center(7)
' banana'
>>> fruit.center(23,*)
  File "<stdin>", line 1
    fruit.center(23,*)
                     ^
SyntaxError: invalid syntax
>>> fruit.center(23,'*')
'*********banana********'
>>> fruit.encode()
b'banana'
>>> fruit.endswith('ana')
True
>>> fruit.endswith('ana',0,5)
False
>>> fruit.endswith('ana',0,6)
True
>>> fruit.endswith('ana',4)
False
>>> fruit.endswith('ana',3)
True
>>> fruit.find('a')
1
>>> fruit.find('a',2)
3
>>> fruit.find('an',2)
3
>>> fruit.find('ana',2)
3
>>> fruit.find('anan',2)
-1
>>> fruit.find('anan')
1
>>> 'anan' in fruit
True
>>> "the sum of {0} and {1} is {2}".format(4,7,11)
'the sum of 4 and 7 is 11'
>>> "the sum of {} and {} is {}".format(4,7,11)
'the sum of 4 and 7 is 11'
>>> "the sum of {} and {} is {}".format(4,7)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: tuple index out of range
>>> "the sum of {} and {} is {}".format(4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: tuple index out of range
>>> "the sum of {0} and {0} is {0}".format(4)
'the sum of 4 and 4 is 4'
>>> "the sum of {four} and {four} is {eight}".format(4,8)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'four'
>>> "the sum of {four} and {four} is {eight}".format(four=4,eight=8)
'the sum of 4 and 4 is 8'
>>> "the sum of {1} and {0} is {2}".format(4,7,11)
'the sum of 7 and 4 is 11'
>>> "the sum of {1} and {3} is {2}".format(4,7,11)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: tuple index out of range
>>> "the sum of {1} and {3} is {2}".format(4,7,11,8)
'the sum of 7 and 8 is 11'
>>> "the sum of {1} and {3} is {2}".format(*'aba')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: tuple index out of range
>>> "the sum of {1} and {3} is {2}".format(*'abaa')
'the sum of b and a is a'
>>> "the sum of {1!r} and {3} is {2}".format(*'abaa')
"the sum of 'b' and a is a"
>>> "int: {0:d}; hex:{0:x}; oct: {0.o}; bin: {0:b}".format(65)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'int' object has no attribute 'o'
>>> "int: {0:d}; hex:{0:x}; oct: {0.x}; bin: {0:b}".format(65)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'int' object has no attribute 'x'
>>> "int: {0:d}; hex:{0:x}; oct: {0:o}; bin: {0:b}".format(65)
'int: 65; hex:41; oct: 101; bin: 1000001'
>>> "int: {0:d}; hex:{0:x}; oct: {0:o}; bin: {0:b}".format(-10)
'int: -10; hex:-a; oct: -12; bin: -1010'
>>> "percentage: {:.2%}".format(34/55)
'percentage: 61.82%'
>>> "percentage: {:.3%}".format(34/55)
'percentage: 61.818%'
>>> "percentage: {:.3}".format(34/55)
'percentage: 0.618'
>>> "percentage: {:+f.3%}".format(34/55)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: Invalid format specifier
>>> "percentage: {:+f}".format(34/55)
'percentage: +0.618182'
>>> "percentage: {:+.3%f}".format(34/55)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: Invalid format specifier
>>> "percentage: {:+.3f}".format(34/55)
'percentage: +0.618'
>>> "percentage: {:+.3f%}".format(34/55)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: Invalid format specifier
>>> ascii(3)
'3'
>>> ascii(3%)
  File "<stdin>", line 1
    ascii(3%)
            ^
SyntaxError: invalid syntax
>>> ascii('3%')
"'3%'"
>>> ascii(abc)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'abc' is not defined
>>> ascii('abc')
"'abc'"
>>> fruit.isidentifier()
True
>>> 'fruit'.isidentifier()
True
>>> '0021'.isdigit()
True
>>> '0021a'.isdigit()
False
>>> '0021a'.isnumeric()
False
>>> '0021x'.isnumeric()
False
>>> '0021'.isnumeric()
True
>>> 'xxvii'.isnumeric()
False
>>> '\b'.isprintable()
False
>>> 'b'.isprintable()
True
>>> '\t'.isprintable()
False
>>> fruit.join('a','b')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: join() takes exactly one argument (2 given)
>>> fruit.join('a')
'a'
>>> fruit.join(['a','b'])
'abananab'
>>> fruit.join(['a','b','c'])
'abananabbananac'
>>> ''.join(['a','b','c'])
'abc'
>>> '*'.join(['a','b','c'])
'a*b*c'
>>> 'www.google.com'.lstrip()
'www.google.com'
>>> '           www.google.com'.lstrip()
'www.google.com'
>>> '           www.google.com'.lstrip('.')
'\t\twww.google.com'
>>> '           www.google.com'.lstrip('w.')
'\t\twww.google.com'
>>> '           www.google.com'.lstrip('\tw.')
'google.com'
>>> '           www.google.com'.lstrip('\tw.r')
'google.com'
>>> 'banana'.rfind('a')
5
>>> 'banana'.rfind('a',0,4)
3
>>> 'banana'.rjust(70)
'                                                                banana'
>>> 'banana'.rpartition('an')
('ban', 'an', 'a')
>>> 'banana'.rpartition('ant')
('', '', 'banana')
>>> 'banana'.rsplit('a')
['b', 'n', 'n', '']
>>> 'banana'.rsplit('a',3)
['b', 'n', 'n', '']
>>> 'banana'.rsplit('a',2)
['ban', 'n', '']
>>> 'banana is a fruit'.rsplit()
['banana', 'is', 'a', 'fruit']
>>> '33,44,-2'.rsplit(',')
['33', '44', '-2']
>>> '33,44,-2'.rsplit(',/')
['33,44,-2']
>>> '33,44,-2'.rsplit(',')
['33', '44', '-2']
>>> 'banana'.split('a',2)
['b', 'n', 'na']
>>> 'BanaNa'.swapcase()
'bANAnA'
>>> 'BanaNa'.swapcase().swapcase()
'BanaNa'
>>> 'BanaNa'.swapcase().swapcase()=='BanaNa'
True
>>> 'BanaNa '.swapcase().swapcase()=='BanaNa '
True
>>> 'BanaNa 2'.swapcase().swapcase()=='BanaNa 2'
True
>>> 

