import turtle
import math
def square(t,length):
  for i in range(4):
    t.fd(length)
    t.lt(90)
def polygon(t,length,n):
  for i in range(n):
    t.fd(length)
    t.lt(360/n)   
def circle(t,r):
  c=2*math.pi*r
  n=360
  polygon(t,c/n,n)
def arc(t,r,angle):
  c=2*math.pi*r
  for i in range(angle):
    t.fd(c/360)
    t.lt(1)
bob=turtle.Turtle()
"""
square(bob,100)
polygon(bob,40,8)
polygon(bob,70,3)
polygon(bob,20,5)

circle(bob,20)
circle(bob,100)
circle(bob,200)
"""
arc(bob,20,360)
arc(bob,100,180)
arc(bob,200,45)

#bob.fd(100)
#print(bob)
turtle.mainloop()
