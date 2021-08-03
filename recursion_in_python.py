#Recursion
#1. Factorial

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

print(fact(5))

#Task 1: recursive python function that returns the sum of the first n integers

def sum(n):
    if n<=1:
        return n
    else:
        return n+sum(n-1)

print(sum(10))

def sum(n):
    if n==0:
        return 0
    else:
        return n+sum(n-1)

print(sum(10))
    


    
  
