#using if statement to find the largest among two numbers

x=int(input("Enter first number"))
print ("x=",x)
print(type(x))
y=int(input("Enter second number"))
print ("y=",y)
print(type(x))
if x>y:
    print("x is greater than y")
elif x==y:
    print("x is equal to y") 
else:
    print ("y is greater than x ")
    
