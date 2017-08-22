"""
1. In a print statement, what happens if you leave out one of the parentheses, or both?
2. If you are trying to print a string, what happens if you leave out one of the quotation marks,
or both?
"""
>>> print("Hello world!)
  File "<stdin>", line 1
    print("Hello world!)
                       ^
SyntaxError: EOL while scanning string literal
>>> print("Hello world!")
Hello world!
>>> print("Hello world!"
... 
... )
Hello world!
>>> print"Hello world!")
  File "<stdin>", line 1
    print"Hello world!")
                      ^
SyntaxError: invalid syntax
>>> print "Hello world!")
  File "<stdin>", line 1
    print "Hello world!")
                       ^
SyntaxError: Missing parentheses in call to 'print'
>>> print "Hello world!"
  File "<stdin>", line 1
    print "Hello world!"
                       ^
SyntaxError: Missing parentheses in call to 'print'
"""
3. You can use a minus sign to make a negative number like -2 . What happens if you put a plus
sign before a number? What about 2++2
"""
>>> 2++2
4
>>> 23+++44
67
>>> 2++++++++++9
11
>>> 2--9
11
>>> 2---9
-7
>>> 2-----9
-7
>>> 2------9
11
"""
4. In math notation, leading zeros are ok, as in 02 . What happens if you try this in Python?
"""
>>> 02+03
  File "<stdin>", line 1
    02+03
     ^
SyntaxError: invalid token
>>> 02
  File "<stdin>", line 1
    02
     ^
SyntaxError: invalid token
>>> 2+03
  File "<stdin>", line 1
    2+03
       ^
SyntaxError: invalid token
"""
5. What happens if you have two values with no operator between them?
"""
>>> 2 4
  File "<stdin>", line 1
    2 4
      ^
SyntaxError: invalid syntax
>>> #seconds in 42 minutes 42 seconds
... 42*60+42
2562
>>> #miles in 10km
... 1.61*10
16.1
>>> #run 10km in 42min 42 sec
... #avg pace (time per mile in minutes)
... (42+42/60)/(10*1.61)
2.652173913043478
>>> #avg pace (time per mile in seconds)
... (42*60+42)/(10*1.61)
159.1304347826087
>>> #avg speed (miles per hour)
... (10*1.61)/((42+42/60)/60)
22.622950819672134
>>> 

