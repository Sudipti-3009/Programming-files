#09-06-2021
students=["Sushma","Sudipti","Anuradha","Avani","Deepti"]
student_info=["Sudipti",[9,9.84],["ECE"],["chem","psp","maths"]]
print(type(students))
print(students)
print(type(student_info))
print(student_info)


#List Slicing

print(students[0:4])

print(students[:4])

print(students[3:])

print(students[2:-1])

print(students[2:-4])

print(student_info)
print(student_info[-1])
#we need to print psp so, we will write like this: it is like nested list . we need to pick one element from one list and from that list we need to pick another element.
print(student_info[-1][1])

#to add elements in a given list: Appending list elements
students.append("Nitya")
print(students)


#Modifying of a list:if in place of avani i need to add another name...like replacing one element of the given list
students[4]="Chitti"
print(students)

#length of a list(len)
print(len(students))

#to remove a element from a list
students.pop(5)
print(students)

#to find the index of an element
print(students[1])

 #another way
Sudipti_index=students.index("Sudipti")
print(Sudipti_index)

#to print index of all element in the list
for element in students:
    print(element)





















