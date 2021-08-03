def add(x,y):
    return x+y

x=10
y=8

z=add(x,y)
print(add(x,y))

def mult(a,b):
    return a*b
a=7
b=9

c=add(a,b)
print(mult(a,b))

def div(p,q):
    return p/q

p=88
q=11
print(div(p,q))

def square(x):
    return x*x
print(square(10))

def sub(m,n):
    return m-n

m=56
n=34
print(sub(m,n))

#lamda function: it is an anonymous function or a function having no name. It is a small and restricted ffunction haveing no more than one line.
# syntax - lambda pi,pi,...expression
adder= lambda x,y:x+y
print(adder(1,2))


def exp(b,c):
    return b**c
b=2
c=6

print(exp(b,c))

import math
euclidian_distance = lambda x,y:math.sqrt( (x**2)+(y**2))
print(euclidian_distance(3,4))



# function map: map() - It is used to apply a particular operation to every element in a sequence.

even_list=[2,4,6,8,10,12,14,16,18,20]
#we want square of every number in the list

squared_even_list= map(lambda x: x*x, even_list) 


print(list(squared_even_list))


#temperature conversion from c to F using lambda function.

temperature_in_C=[39.2,36.5,37.3,38,37.8]

temperature_in_F=map(lambda x:((x * 9/5) + 32),temperature_in_C)
print(list(temperature_in_F))

#lambdas in reduces()
from functools import reduce
even_list=[2,4,6,8,10]
product=reduce(lambda x,y:x*y, even_list)
print(product)
add=reduce(lambda x,y:x+y, even_list)
print(add)
#result should be squares of each element in list and their sum

even_numbers=[0,2,4,6,8,10]
sqaured_list= reduce(lambda x,y:x+(y*y),even_numbers)
print(sqaured_list)




















