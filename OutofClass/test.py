#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 13:49:34 2023

@author: domin
"""

import numpy as np


##2nd element of arrays in first row
nums = np.array([[1, 11, 2], 
                [2, 3, 2], 
                [3, 4, 2], 
                [4, 5, 2]])
arr = [nums, ["first", "second", "third", "fourth"], 2]
print(arr[0][:,1])