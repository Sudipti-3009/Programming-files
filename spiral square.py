import turtle
spiral = turtle.Turtle()
distance = 50
for i  in range(20):
    spiral.forward(distance)
    spiral.right(90)
    distance = distance+10
