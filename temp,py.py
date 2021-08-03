# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np 

data = np.random.randn(2,4)

print(data)
print(data.shape)

print(np.arange(15))
print(np.zeros(10))
print(np.zeros((3,6)))
print(np.empty((2,3,2)))
data2 =[[1,2,3,4],[5,6,7,8]]
arr2=np.array(data2)
print(arr2)
data_1 =[5 , 5.2 , 0 , 1 , 6.9]
arr1 = np.array(data_1)
print(arr1)
arr = np.array([[1, 2] , [ 4, 5]])
print(arr.shape)
print(type(arr))
print(arr[0,0])
print(arr[0,1])
print(arr[0,:])
print(arr[:,1])
print(np.zeros((4,4)))
import numpy as np
m= np.arange(1,17).reshape((4, 4))
print(m)

import numpy as np
arr4 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(arr4)   
print(arr4.shape)
 
                        
