# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 21:07:18 2021

@author: LENOVO
"""
'''
import csv
with open('MOOC.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    
    '''
  '''  
import pandas as pd
xls = pd.ExcelFile('yelp.xlsx')
df = xls.parse('yelp_data')
print(type(df))    
'''
import numpy as np
xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()