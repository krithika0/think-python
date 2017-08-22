import turtle
from polygon import arc
def spiral(t):
  for i in range(1000):
    arc(t,i/4,2)

bob=turtle.Turtle()
spiral(bob)
turtle.mainloop()
