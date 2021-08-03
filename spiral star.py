import turtle 

spiral = turtle.Turtle()
list0 = ["blue","red","black"]
for i in range(20):
    spiral.color(list0[i%3])
    spiral.forward(i * 10)
    spiral.right(144)
