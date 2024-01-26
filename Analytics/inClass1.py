#import pandas as pd
import numpy as np

from pandas import Series

scores = Series(np.random.randint(70,100,size=(10)), dtype=int, 
   index=["Sep", "Oct", "Nov", "Dec", "Jan", 
          "Feb", "Mar", "Apr", "May", "Jun"])

print(scores)

print("\nAverage Yearly Score: ", scores.mean())

first5 = scores[0:4].mean()
last5 = scores[-5:].mean()

print("\nMean of first 5 months: ", first5)

print("\nMean of last 5 months: ", last5)

print("\nDifference of first 5 and last 5 months: \n", abs(first5-last5))

print("\nStandard Deviation of year: \n", scores.std())