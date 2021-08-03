
#17-06-2021

# A Dictionary in python is the unordered and changeable collection of data values that holds key value pairs.
# A Dictionary in python is declared by enclosing a commoa-separated list of key value pairs using curly braces.
#Syntax:'Name':'Sudipti', name is key and sudipti is called value and both together is called element 
#Duplicating is not allowed
student1 ={'Name':'Sudipti','branch':'ECE','Section':' A','Roll_no':9}
print(type(student1))
print("before updating")
print(student1)
print(student1['Name'])
print(student1['Roll_no'])
#updating the dictionary
print("after updating")
student1.update({'Member':'NCC'})
print(student1)
#deleting from a dictionary

student1={'Name': 'Sudipti', 'branch': 'ECE', 'Section': ' A', 'Roll_no': 9, 'Member': 'NCC'}
print("before deleting")
print(student1)
del student1['Name']
print("after deleting")
print(student1)


print(student1.items())



#checking what are the keys in our dictionary.
student1={'Name': 'Sudipti', 'branch': 'ECE', 'Section': ' A', 'Roll_no': 9, 'Member': 'NCC'}

print("Keys of student1 are")
print(student1.keys())

print("Values of student1 are")
print(student1.values())

for i in student1.keys():
    print(student1[i])
     


























