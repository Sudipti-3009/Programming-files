# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 08:27:04 2021

@author: LENOVO
"""

lst1 = [] 
lst2 = []
lst3 = []
 
lst1 = [int(item) for item in input("Enter the list1 items (press space for next item): ").split()]
lst2 = [int(item) for item in input("Enter the list2 items (press space for next item): ").split()]

print(lst1)
print(lst2)

list(set(lst1) & set(lst2))
print(set(lst1) & set(lst2))

new = set(lst1) - set(lst2)

l = lst1 + list(new)
print(l)

def unique(l):
 
    unique_list = []

    for x in l:
        if x not in unique_list:
            unique_list.append(x)
    for x in unique_list:
        print(x)

print(unique(l))
