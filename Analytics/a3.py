import pandas as pd
import numpy as np
from pandas import Series, DataFrame
import plotly.express as px
import matplotlib.pyplot as plt
#%pylab inline
import warnings
import datetime as dt

warnings.filterwarnings("ignore") # suppress pandas warnings

# read in cav red_sea_shipping_data.csv in the data files folder

df = pd.read_csv("red_sea_shipping_data.csv")

print(dt.datetime.now().toordinal())
print(dt.datetime(2023, 10, 1))

# examine data and data types

# set appropriate data types

df['datetime'] = pd.to_datetime(df['datetime'])
df['location'] = df['location'].astype('category')
df["number_of_cargo_ships"] = df["number_of_cargo_ships"].astype(np.int8)
df["number_of_tanker_ships"] = df["number_of_tanker_ships"].astype(np.int8)


df_month = df
locations = df_month["location"].cat.categories
store = dict()

df_month['datetime'] = pd.to_datetime(df['datetime'] + pd.offsets.MonthBegin(-1))

#group by month
months = df_month['datetime'].unique()


#filter by month
for location in locations:
  for month in months:
    cat_count = sum(np.where((df["location"] == location) & (df['datetime'] == month), df["number_of_cargo_ships"], 0))
    store.update({month : cat_count})
  plt.plot(store.keys(), store.values(), label=location)
  plt.legend()
  #px.line(store)

#graph month/count

#copy above, change cargo to tanker, month to week, start sept 2023

#groupby day, sum of tanker and cargo