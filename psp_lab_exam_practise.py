'''
Design a Python script to convert a Binary number to a Decimal number and verify if it is a Perfect number.

What are binary and decimal number?
Binary to decimal conversion is done to convert a number given in the binary system to its equivalent in the decimal number system.
The binary number system is used in computers andelectronic systems to represent data and it consists of only two digits which are 0 and 1.
The decimal number system is the most commonlyused number system around the world which is easily understandable to people.
It consists of digits from 0 to 9.
Binary to decimal conversion can be done in the simplest way by adding the products of each binary digit with its weight
(which is of the form - binary digit × 2 raised to a power of the position of the digit) starting from the right-most digit which has a weight of 2^0.

b_num = list(input("Input a binary number: "))
value = 0

for i in range(len(b_num)):
	digit = b_num.pop()
	if digit == '1':
		value = value + pow(2, i)
print("The decimal value of the number is", value)



'''

h1=int(input("Enter the first time's hour : "))
m1=int(input("Enter the first time's minutes : "))
s1=int(input("Enter the first time's seconds : "))
h2=int(input("Enter the first time's hour : "))
m2=int(input("Enter the first time's minutes : "))
s2=int(input("Enter the first time's seconds : "))

T1=((h1*60*60)+(m1*60)+s1)
print(T1)
T2=((h2*60*60)+(m2*60)+s2)
print(T2)
T=T1-T2
print(T)
Rs=T//3600
print(Rs)
Ms=T%3600
print(Ms)
MS=Ms//60
print(MS)
Ss=Ms%60
print(Ss)

