Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def form_hex(side): 

    for i in range(6): 

        my_pen.fd(side) 

        my_pen.left(300) 

        side -= 2 

  

  



tut = turtle.Screen() 

tut.bgcolor("green") 

tut.title("Turtle") 

  

my_pen = turtle.Turtle() 

my_pen.color("orange") 

  

tut = turtle.Screen() 

  



side = 120 

  

for i in range(5): 

    form_hex(side) 

    side -= 12