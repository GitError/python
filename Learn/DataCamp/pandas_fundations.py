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

# resampling data and applying rolling window calculations

august = df['Temperature']['2010-08']
daily_highs = august.resample('D').max()
daily_highs_smoothed = daily_highs.rolling(window=7).mean()
print(daily_highs_smoothed)


# indexing
# .loc - by label       e.g. df.loc[row_label, column_label]
# .ilock - by index     e.g. df.loc[row_index, column_index]
 
election = pd.DataFrame(columns=['State', 'Total', 'Obama', 'Romney', 'Winner', 'Voters'])

#          state   total      Obama     Romney  winner  voters    turnout     margin
# county                                                                             
# Adams        PA   41973  35.482334  63.112001  Romney   61156  68.632677  27.629667
# Allegheny    PA  614671  56.640219  42.185820   Obama  924351  66.497575  14.454399
# Armstrong    PA   28322  30.696985  67.901278  Romney   42147  67.198140  37.204293
# Beaver       PA   80015  46.032619  52.637630  Romney  115157  69.483401   6.605012
# Bedford      PA   21444  22.057452  76.986570  Romney   32189  66.619031  54.929118

left_columns = election.loc[:, : 'Obama']
print(left_columns.head())
middle_columns = election.loc[:, 'Obama' : 'winner']
print(middle_columns.head())
right_columns = election.loc[:, 'Romney' : ]
print(right_columns.head())


