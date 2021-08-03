'''
#Write a python code for inserting a text file, from that text calculate
1. number of characters
2. number of words
3. number of lines
4. number of repeated words
5. number of times the words have been repeated
'''

file = open("Sudipti.txt","r")

#1.Number of letters
content = file.read()
num_of_characters=len(content)
print(num_of_characters)


#2.Number of lines
num_of_lines = content.split("\n")
print(len(num_of_lines))


#3.Number of words
content_split = content.split()
print(content_split)
num_of_words= len(content_split)
print(num_of_words)


#4.Repeated words and number of times they have occured :
# :::::method using dictionary command::::

# Open the file in read mode
file = open("Sudipti.txt", "r")

#read content of file to string
data = file.read()
def word_count(str):
    # Create an empty dictionary
    counts = dict()
    words = str.split()

    # Loop through each line of the file
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts



# Print the number of occurrences of word
print( word_count(data))


file = open("Sudipti.txt", "r")
time = file.read()

def times(str):

    str = str.split()         
    str2 = []
  
    # loop till string values present in list str
    for i in str:             
  
        # checking for the duplicacy
        if i not in str2:
  
            # insert value in str2
            str2.append(i) 
              
    for i in range(0, len(str2)):
  
        # count the frequency of each word(present 
        # in str2) in str and print
        print('Times of', str2[i], 'is :', str.count(str2[i]))

print(times(time))        


        

file = open("Sudipti.txt", "r")
Repeated_times = file.read()
print(Repeated_times)

list_of_contents=Repeated_times.split()
print (list_of_contents)


#letters repeatation

f=open("Sudipti.txt","r")
data = f.read()
#creating an empty dictionary
d = dict() 
data = data.lower()
for line in data:
    line = line.strip() #seperating lines
    words = line.split(" ") #spliting words
    #print(line)
    #print(words)
    for word in line:
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1
for key in list(d.keys()):
    print(key, ":", d[key])










'''
count=0
for element in list_of_contents :
    if list_of_contents[]==list_of_contents[]:
       count=count+1

    else:
        count = 1


        
print (element)
'''



























    
