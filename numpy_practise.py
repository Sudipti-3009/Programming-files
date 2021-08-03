# -*- coding: utf-8 -*-
"""

Arthematic operations
@author: LENOVO
"""

import numpy as np
'''
arr = np.array([[10, 20, 30], [40, 50, 60]])
print(arr*arr)
print(arr-arr)
print(1/arr)
print(arr*0.5)
##3D arrray
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]],[[13,14,15],[16,17,18]]])
print(arr3d)
array= ([ 0, 1, 4, 9, 16, 25, 36, 49, 64, 81])
print(array[1:6])
print(arr[:2])
arr3d[:2, 1:] =0
print(arr3d)
names = np.array(['sudipti', 'anushka', 'sultan', 'radha', 'aarfa', 'akira', 'taani'])
print(names)
print(names == 'Bob')
print(names=='taani')
print(names[4]== 'meera')
arr1 = np.arange(16).reshape((2, 2, 4))
print(arr1)
arr_1 = np.arange(27).reshape((3, 3, 3))

print(arr_1)

array_2=arr_1.transpose((1, 0, 2))
print(array_2)

import numpy as np
  
in_array1 = np.array([[2, -7, 5], [-6, 2, 0]])
in_array2 = np.array([[0, -7, 8], [5, -2, 9]])
   
print ("1st array : ", in_array1)
print ("2nd array : ", in_array2)
   
    
out_array = np.multiply(in_array1, in_array2) 
print ("Resultant output array: ", out_array) 

print(np.sqrt(arr))
print(np.exp(arr))

arr_3 = np.empty((8, 4))
for i in range(8):
    arr_3[i] = i

print(arr_3)
old_values = arr3d[0].copy()
arr3d[0] = 42
print(arr3d)

arr_slice = names[1:4]
print(arr_slice)

print(names.dtype)

x = np.random.randn(8)
print(x)
y =np.random.randn(8)
print(y)

print(np.maximum(x,y))

array_5=np.random.randn(7)*5
print(array_5)
remainder, whole_part =np.modf(array_5)
print(remainder)
print(whole_part)
print(np.sqrt(whole_part))

points = np.arange(-5,5,0.01)
print(points)
xs,ys = np.meshgrid(points,points)
print(ys)

z = np.sqrt(xs**2+ys**2)
print (z)

import matplotlib.pyplot as plt
plt.imshow(z, cmap=plt.cm.gray); plt.colorbar()

plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")


xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])
result = [(x if c else y)
          for x, y, c in zip(xarr, yarr, cond)]
print(result)

result = np.where(cond, xarr, yarr)
print(result)
arr_1 = np.random.randn(4, 4)
print(arr_1)
print(arr_1 > 0)
np.where(arr_1 > 0, 2, -2)

parr = np.array([0, 1, 2, 3, 4, 5, 6, 7])
print(parr)
print(parr.cumsum())

zarr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print(zarr)
print(zarr.cumsum(axis=0))
print(zarr.cumprod(axis=1))

jarr = np.random.randn(100)
print(jarr)
print((jarr > 0).sum())
bools = np.array([False, False, True, False])
print(bools.any())
print(bools.all())



arr_a = np.random.randn(6)
print(arr_a)
print(arr_a.sort())

arr = np.random.randn(5, 3)
print(arr.sort(1))

large_arr = np.random.randn(1000)
large_arr.sort()
print(large_arr[int(0.05 * len(large_arr))])

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
print(np.unique(names))

ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])
print(np.unique(ints))
print(sorted(set(names)))

values = np.array([6, 0, 0, 3, 2, 5, 6])
print(np.in1d(values, [2, 3, 6]))

arr = np.arange(10)
np.save('some_array', arr)
print(np.load('some_array.npy'))

np.savez('array_archive.npz', a=arr, b=arr)
arch = np.load('array_archive.npz')
print(arch['b'])
np.savez_compressed('arrays_compressed.npz', a=arr, b=arr)

x = np.array([[1., 2., 3.], [4., 5., 6.]])
y = np.array([[6., 23.], [-1, 7], [8, 9]])
print(x)
print(y)
print(x.dot(y))
print(np.dot(x, y))
print(np.dot(x, np.ones(3)))
print(x @ np.ones(3))

from numpy.linalg import inv, qr
X = np.random.randn(5, 5)
mat = X.T.dot(X)
print(inv(mat))
print(mat.dot(inv(mat)))

q, r = qr(mat)
print(r)

import random
import matplotlib as plt
position = 0
walk = [position]
steps = 1000
for i in range(steps):
    step = 1 if random.randint(0, 1) else -1
    position += step
    walk.append(position)

plt.plot(walk[:100])



nsteps = 1000
draws = np.random.randint(0, 2, size=nsteps)
steps = np.where(draws > 0, 1, -1)
print(walk = steps.cumsum())


nwalks = 5000
draws = np.random.randint(0, 2, size=(nwalks, nsteps)) # 0 or 1
steps = np.where(draws > 0, 1, -1)
walks = steps.cumsum(1)
print(walks)


samples = np.random.normal(size=(4, 4))

print(samples)


'''

import numpy as np
print(np.__version__)


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 2, -1)
print(newarr)
import numpy
arr = numpy.array([1, 6, 4, 8, 3, 7])  
print(numpy.max(arr))
import numpy as np

arr = np.array([[1, 2, 3],[4,5,6]])

for x in arr:

    for i in x:

         print(i)
         
         
arr = np.array([[6, 5, 3], [4, 9, 3]])

newarr_1 = arr.reshape(-1)  
print(newarr_1)       
import pandas as pd

a = [9, 7, 2, 1]

myvar = pd.Series(a)

print(myvar[0])
import pandas as pd

a = [5, 9, 10]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)
import pandas as pd

fruits = {"fruit1": "apple", "fruit2": "banana", "fruit3": "pears"}

myvar = pd.Series(fruits)

print(myvar)
import pandas as pd

import numpy as np

fruits = np.array([["apple", "banana", "pears"], ["pomgranate", "papaya", "grapes"]])

myvar = pd.DataFrame(fruits, index = ["fruit1", "fruit2"])

print(myvar)


employee = {

"employees":[

    {"firstName":"John", "lastName":"Doe"},

    {"firstName":"Anna", "lastName":"Smith"},

    {"firstName":"Peter", "lastName":"Jones"}

]

}

print(employee["employees"][0])

import matplotlib.pyplot as plt

X = range(1, 50)

Y = [value * 2 for value in X]

print("Values of X:")

print(*range(1,50)) 

print("Values of Y (twice of X):")

print(Y)

# Plot lines and/or markers to the Axes.

plt.plot(X, Y)

# Set the x axis label of the current axis.

plt.xlabel('x - axis')

# Set the y axis label of the current axis.

plt.ylabel('y - axis')

# Set a title 

plt.title('Plot of (X,Y).')

# Display the figure.

plt.show()


X = range(1, 50)

Y = [value * 3 for value in X]
print(Y)

