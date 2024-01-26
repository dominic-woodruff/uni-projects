# -*- coding: utf-8 -*-
# Dominic Woodruff

import numpy as np
import numpy.random as rg

#Code for exercise 1
print("\nExercise 1\n")
e1 = np.array([1, 2, 3, 4])
print("1-4:\n", e1)
print("\nArray Data Type:\n", e1.dtype)

#Code for exercise 2
print("\nExercise 2\n")
b = np.zeros((2, 7))
print("2x7 0's: \n", b)

#Code for exercise 3
print("\nExercise 3\n")
c = np.arange(1, 23, 2.5)
print("1-21 by 2.5: \n", c)

#Code for exercise 4
print("\nExercise 4\n")
d = np.reshape(np.arange(1, 41), (4,10))
d = np.reshape(d, (5, 8))
print("Element (5, 8) of 1-40 in 5x8: \n", d[4][7])

#Code for exercise 5
print("\nExercise 5\n")
arr = np.array(np.arange(0, 18), dtype='int32')
arr = np.reshape(arr, (3, 3, 2))
print("Array with params: \n", arr)

#Code for exercise 6
print("\nExercise 6\n")
m = rg.random((4, 4))
p = rg.random((4, 4))
print("Trig Function:\n", np.sin(m) @ np.cos(p) + m.sum(axis=0))

#Code for exercise 7
print("\nExercise 7\n")
f1 = rg.random((1,10))
f1 = np.sort(f1)
print("Max and Min of sorted array:\n", f1[0][0], "\n", f1[0][9])
f2 = np.reshape(f1, (2, 5))
f2 = np.concatenate((f2, f2))
print("Sorted array concat with self:\n", f2)

#Code for exercise 8
print("\nExercise 8\n")
A1 = np.arange(10)
print("First and Last:\n", A1[0], ", ", A1[9])
print("\nEven Indices\n", A1[0::2])
print("\nFirst Four\n", A1[0:4])
print("\nLast Three\n", A1[7:10])
print("\nFour to Eight\n", A1[3:7])
np.random.seed(42)
M1 = 100*np.random.rand(9,7).round(2)
print("\nFirst and Last\n", M1[1:9:7])
print("\nM1\n", M1)
temp = np.array(0)
for element in M1.flat:
    if element < 10: 
        temp = np.append(temp, element)
print("\n<10:\n", temp)
print("\nEven Row:\n", M1[::2])
print("\nOdd Column\n", np.transpose(M1)[1::2])
print("\nEven Row Odd Column\n", np.transpose(M1[::2])[1::2])
print("\nEven Indices\n", np.transpose(M1[::2])[::2])