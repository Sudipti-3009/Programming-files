# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 11:52:18 2021

@author: LENOVO
"""

import pandas as pd
import xlrd
import openpyxl
xls = pd.ExcelFile('Experiment_23.xlsx')
print(xls)
df = xls.parse('Sheet1')
print(df)
print(df['Grade'].value_counts())
A = df['Grade'] == 'A'
print(df[A])
x=df[A]
print(x)
First_class=len(x)
print(First_class)
B = df['Grade'] == 'B'
print(df[B])
y=df[B]
print(y)
Second_class=len(y)
print(Second_class)
C = df['Grade'] == 'C'
print(df[C])
z=df[C]
print(z)
Third_class=len(z)
print(Third_class)
D = df['Grade'] == 'D'
print(df[D])
u=df[D]
print(u)
Fourth_class=len(u)
print(Fourth_class)
import turtle

def drawBar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()              
    t.left(90)
    t.forward(height)
    t.write(str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()                 


Grades = [First_class, Second_class, Third_class, Fourth_class]
  
maxheight = max(Grades)
numbars = len(Grades)
border = 10

wn = turtle.Screen()             
wn.setworldcoordinates(0-border, 0-border, 40*numbars+border, maxheight+border)
wn.bgcolor("black")

tess = turtle.Turtle()           
tess.color("white")
tess.fillcolor("red")
tess.pensize(3)

for a in Grades:
    drawBar(tess, a)
    
tess.write("X- axis is for the various distinctions")
tess.penup()
tess.goto(165,5)
tess.pendown()
tess.write("y represents the number of students")
tess.penup()
tess.goto(165,4)
tess.pendown()
tess.write("the first bar-the first divison")
tess.penup()
tess.goto(165,3)
tess.pendown()
tess.write("followed by second-division")
tess.penup()
tess.goto(165,2)
tess.pendown()
tess.write("followed by third division")
tess.penup()
tess.goto(165,1)
tess.pendown()
tess.write("followed by fourth")
tess.penup()

             

wn.exitonclick()
