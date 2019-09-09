# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
df = pd.read_csv(r"C:\Users\S533718\Desktop\Data analysis Datasets\datasets\Stock.csv",parse_dates= ["Date"])
df['year'],df['month'],df['day'] = df.Date.dt.year, df.Date.dt.month, df.Date.dt.day
df.describe()
df.count().isnull
df.set_index("Date")
df['Tesla'].plot()
all = ["Tesla","Apple","CocaCola"]
axes = df[all].plot()
ax = df.loc['Date', 'CocaCola'].plot()
ax.set_ylabel('Daily Consumption (GWh)');