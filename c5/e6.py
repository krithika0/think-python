import turtle
def koch(t,length):
  if length<=3:
    t.fd(length)
  else:
    koch(t,length/3)
    t.lt(60)
    koch(t,length/3)
    t.rt(120)
    koch(t,length/3)
    t.lt(60)
    koch(t,length/3)
def snowflake(t,length):
  for i in range(3):
    koch(t,length)
    t.rt(120)
def quadratic(t,length):
  if length<=4:
    t.fd(length)
  else:
    quadratic(t,length/4)
    t.lt(90)
    quadratic(t,length/4)
    t.rt(90)
    quadratic(t,length/4)
    t.rt(90)
    quadratic(t,length/4)
    quadratic(t,length/4)
    t.lt(90)
    quadratic(t,length/4)
    t.lt(90)
    quadratic(t,length/4)
    t.rt(90)
    quadratic(t,length/4)
  
bob=turtle.Turtle()
bob.up()
bob.bk(100)
bob.lt(90)
bob.fd(100)
bob.rt(90)
bob.down()
quadratic(bob,200)
#snowflake(bob,50)
turtle.mainloop()
