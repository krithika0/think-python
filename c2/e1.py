>>> # is 42 = n legal?
... 42=n
  File "<stdin>", line 2
SyntaxError: can't assign to literal
>>> #is x=y=1?
... x=y=1
>>> x
1
>>> y
1
>>> # ; at the end
... x=5;
>>> x
5
>>> # . at the end
... x=6.
>>> x
6.0
>>> x=y.
  File "<stdin>", line 1
    x=y.
       ^
SyntaxError: invalid syntax
>>> #xy for multiplication
... xy
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: name 'xy' is not defined
>>> x*y
6.0
>>> #volume of a sphere with radius 5
... 4*math.pi*5*5*5/3
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: name 'math' is not defined
>>> import math
>>> 4*math.pi*5*5*5/3
523.5987755982989
>>> # cover price is 24.95, 40% discount
... # shipping $3 for the first copy, 75c for each additional
... # total wholesale cost of 60 copies
... cover_price=24.95
>>> discounted_price=0.6*24.95
>>> total_cost=1*(discounted_price+3)+59*(discounted_price+0.75)
>>> total_cost
945.4499999999999
>>> discounted_price
14.969999999999999
>>> round(discounted_price,2)
14.97
>>> """
... leave house at 6:52
... run 1 mile at easy pace (8:15 per mile)
... run 3 miles at tempo (7:12 per mile)
... run 1 mile at easy pace
... """
'\nleave house at 6:52\nrun 1 mile at easy pace (8:15 per mile)\nrun 3 miles at tempo (7:15 per mile)\nrun 1 mile at easy pace\n'
>>> start_time=6*60+52 #converted to minutes
>>> start_time=start_time*60 #converted to seconds
>>> start_time
24720
>>> easy_pace=8*60+15 #seconds
>>> tempo=7*60+12 #seconds
>>> end_time=start_time + 2*easy_pace + 3*tempo
>>> end_time
27006
>>> end_time_sec=end_time%60
>>> end_time=end_time//60 #converted to minutes
>>> end_time_min=end_time%60
>>> end_time=end_time//60 #converted to hours
>>> end_time_hours=end_time
>>> print(end_time_hours,':',end_time_min,':',end_time_sec)
7 : 30 : 6
>>> 
