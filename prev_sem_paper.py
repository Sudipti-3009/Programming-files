ch = input("Please Enter Your Own Character : ")

if(ch.isupper()):
    print("The Given Character ", ch, "is an Uppercase Alphabet")
elif(ch.islower()):
    print("The Given Character ", ch, "is a Lowercase Alphabet")
else:
    print("The Given Character ", ch, "is Not a Lower or Uppercase Alphabet")
