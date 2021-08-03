#file handling in python : 16/06/2021

f = open("E:\BTECH. SEM 2\PSP\Raptor\file.txt","r")

if f.mode=="r":
   contents=f.read()
   print(contents)

