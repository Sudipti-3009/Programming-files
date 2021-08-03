import turtle
cc=turtle.Turtle()
r=10
for i in range(10):
               cc.pensize(2)
               cc.circle(r*i)
               cc.up()
               cc.sety((r*i)*(-1))
               cc.down()
