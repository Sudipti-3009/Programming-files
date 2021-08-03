# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 09:10:11 2021

@author: LENOVO
"""

import pandas as pd
xls = pd.ExcelFile("yelp.xlsx")
print(xls)
df = xls.parse('yelp_data')
print(df)
print(df.columns)
print(df.describe)