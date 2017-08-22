import turtle
from polygon import arc
def petal(t,radius,angle):
  arc(t,radius,angle)
  t.lt(180-angle)
  arc(t,radius,angle)
def flower(t,radius,angle,n):
  for i in range(n):
    petal(t,radius,angle)
    t.rt(180+angle-360/n)
    
bob=turtle.Turtle()
"""
petal(bob,50,90)
petal(bob,50,100)
petal(bob,100,45)
petal(bob,300,30)
"""
#flower(bob,50,100,7)
bob.up()
bob.bk(150)
bob.down()
flower(bob,50,60,7)
bob.up()
bob.fd(150)
bob.down()
flower(bob,40,90,10)
bob.up()
bob.fd(150)
bob.down()
#-flower(bob,100,30,20)
flower(bob,150,20,20)
turtle.mainloop()
