
#1.(a)
def fibonacci(n):
    x = 0
    y = 1
    for i in range(n):
        print (x)
        t = y
        y = x + y
        x = t
print(fibonacci(5))
#(b)
def fibonacci(n):
    x, y = 0, 1
    for i in range(n):
        print (x)
        x, y = y, x + y
print(fibonacci(5))
#2.(a)

for i in [0, 1, 2, 3, 4, 5]:
    print (i**2)
#(b)
for i in range(6):
    print (i**2)
    
#3.(a)
Colors = ["red","orange","blue","yellow","green","caramine","violet"]

for i in range(len(Colors)):
    print (Colors[i])
#(b)
for Color in Colors:
    print(Color)


#4.(a)     
x=5
y=10

temp=x
x=y
y=temp
print('The value of x after swapping: {}' .format(x))

print('The value ofyx after swapping: {}' .format(y))


#(b)
x=5
y=10
x,y=y,x
print("x = ",x)
print("y = ",y)

#5.(a)
my_list = []
for i in range(10):
    my_list.append(i*2)

#(b)
my_list = [i*2 for i in range(10)]

#6.(a)
a=[2,5,6]
b=[]
for i in a:
     if i>4:
         b.append(i)
print(b)         

#(b)
a=[2,5,6]
b=[i for i in a if i > 4]
print(b)


#7.(a)
f = open('file.txt')
a = f.read()
print (a)
f.close()
#(b)
with open('file.txt') as f:
    for line in f:
        print (line)


#8.(a)

age = 20
if age > 18 and age < 60:
    print("young man")

#(b)
if 18 < age < 60:
    print("young man")

#9.(a)
s1 = "puppy.net"
s2 = "puppies"
s3 = "welcome to %s and following %s" % (s1, s2)
print(s3)
#(b)
s3 = "welcome to {blog} and following {wechat}".format(blog="puppy.net", wechat="puppies")
print(s3)

#10.(a)
a=3
if a > 2:
    b = 2
else:
    b = 1
    print(b)

    
#(b)
a = 3   
b = 2 if a > 2 else 1
print(b)

#11.(a).
data = ["one", "two", "three"]
for i in range(0, len(data)):
    print(data[i])

    
#(b)

data = ["one", "two", "three"]
for val in data:
    print(val)
 
#12.(a)
list_number =[]
for i in range(10):
    list_number.append(i)
print(list_number)
  
#(b)
list_number = [idx for idx in range(10)]
print(list_number)

#13.(a)

colors = ["red", "green", "blue", "green", "red", "green"]

d = {}
for color in colors:
    if color not in d:
       d[color] = 0
    d[color] += 1
print(d)
 
#(b)
d = {}
for color in colors:
    d[color] = d.get(color, 0) + 1
    print(d)
#14.(a)
colors = ["red", "green", "blue", "black", "white"]
for idx in range(len(colors)-1, -1, -1):
    print(f"{colors[idx]}")

   
#(b)
colors = ["red", "green", "blue", "black", "white"]
for color in reversed(colors):
    print(f"{color}")

#15.(a)
x=[1, 2, 3, 4, 5, 6]

result = []

for idx in range(len(x)):
    result.append(x[idx] * 2)

print(result)
#(b)

x=[1, 2, 3, 4, 5, 6]

print([(element * 2) for element in x])

#16.(a)
x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = []

for idx in range(len(x)):
    if x[idx] % 2 == 0:
        result.append(x[idx] * 2)

else:
    result.append(x[idx])

print(result)
#(b)

x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print([element * 2 for element in x if element % 2 == 0])



#18.(a)
scores = [90,85,75,87,98,77]
above_90 = 0
below_90 = 0
for i in scores:
    if i>=90:
        above_90 = above_90 + 1
    if not i>=90:
        below_90 = below_90 +1
print(above_90)
print(below_90)


#(b)

above_90 = 0
below_90 = 0
for i in scores:
    if i>=90:
        above_90 += 1
    else:
        below_90 += 1
print(above_90)
print(below_90)

#19.(a)
print("Hello Everyone!")
print("How are you?")

#(b)

print("Hello Everyone! \n How are you?")


#20.(a)
colours = ['red','green','blue','yellow']

for i in range(len(colours)):
    print (colours[i])
#(b)
for i,item in enumerate(colours):
    print(i, "-",item)

#21.(a)
list1 = [5, 4, 3, 2, 1]
list2 = list1
list1 += [1, 2, 3, 4]
  
print(list1)
print(list2)


#(b)
list1 = [5, 4, 3, 2, 1]
list1 = list1 + [1, 2, 3, 4]
list2 = list1

print(list1)
print(list2)








    

