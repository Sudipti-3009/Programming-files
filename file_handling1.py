#file handling in python : 16/06/2021

f = open("file.txt","r")

if f.mode=="r":
   contents=f.read()
   print(contents)
'''
'''
#append command
   
f=open("file.txt","r")

if f.mode=="r":
   contents=f.read()
   print(contents)


f=open("file.txt","a+")

f.write("I am doing my Btech in ECE course")
f=open("file.txt","r")
contents=f.read()
print(contents)
f.close()


f= open("file.txt","w")
if f.mode=="w":
   f.write("hey!")
f.close()   



