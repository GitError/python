""" pandas Foundations """

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# pandas ia a library for data analysis
# the power of pandas is its data frame

# slicing data frames
# same as np arrays e.g. df.iloc[:5,:]

# renaming columns 
# df = pd.DataFrame(data)
# list_labels = ['year', 'artist', 'song', 'chart weeks']
# df.columns = list_labels

# broadcasting - setting a value to an entire column 
cities = ['Toronto', 'Ottawa']
counts = [662,458]
counts2 = [115,458]
data = {'state':'ON', 'city':cities, 'stat': counts, 'stat2': counts2}
df = pd.DataFrame(data) 
print(df.head())

# eda - expoloratory data analysis 

# plotting data 
# line plot -- default value on x axis -- not too useful 
df.plot(color='red') 
plt.title('title')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# plotting DataFrame can use the following syntax
# df.plot(kind='hist') or df.plt.hist() or df.hist() -- same for other plot types

cols = ['weight' , 'mpg']
df[cols].plot(kind='box', subplots=True)
plt.show()

# pdf - probability density function 
# cdf - cumulative density functions 

# This formats the plots such that they appear on separate rows
fig, axes = plt.subplots(nrows=2, ncols=1)

# Plot the PDF
df.fraction.plot(ax=axes[0], kind='hist', bins=30, normed=True, range=(0,.3))
plt.show()

# Plot the CDF
df.fraction.plot(ax=axes[1], kind='hist', bins=30, cumulative=True, normed=True, range=(0,.3))
plt.show()

# summarizing with describe()
df.describe()  # summary statistics, counts mean, std, min, max, 25/75/100

# Quantiles(q) -- check range q (percentail)
# Print the 5th and 95th percentiles
df.quantile([0.05, 0.95])

# extracting categorical data from a column -- .unique()

# using pandas to read datetime objects; .loc[] - slicing data frame
# ISO 86o1 format when reading CSV (parse_date=True)
# partial datetime string selection : df.loc['date'] or df.loc['data-range']
# --> pandas suports selection of entire months and years e.g. [2015-5] is may-2015

# re-indexing + fillinf missing values
# df.reindex(index=, method=) -- ffill forward fill OR bfill - backwards fill 

