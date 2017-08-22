import turtle
import math
def pie_unit(t,radius,angle):
  edge=abs(math.cos((90-angle/2)*math.pi/180)*radius*2)
  t.fd(radius)
  t.lt(90+angle/2)
  t.fd(edge)
  t.lt(90+angle/2)
  t.fd(radius)

def pie(t,radius,n):
  angle=360/n
  t.rt(angle/2)
  for i in range(n):
    pie_unit(t,radius,angle)
    t.lt(180)
bob=turtle.Turtle()
#bob.rt(20)
#pie_unit(bob,100,7)
pie(bob,100,7)
