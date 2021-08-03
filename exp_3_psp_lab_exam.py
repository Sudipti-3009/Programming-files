with open('numbers.txt', 'r') as f:
    data = sorted(map(int, f.readline().split(',')))


print(data)    


data = []
with open('numbers.txt','r') as myfile:
    for line in myfile:
        data.extend(map(int, line.split(',')))
x =sorted(data)
print(x)
