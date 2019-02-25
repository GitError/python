'''
Diagnose data for cleaning code snippets
'''

import glob

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# --------------------------------
# Inspecting pandas DataFrame
# --------------------------------

df = pd.read_csv('http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv')

# top 5 and bottom 5 rows data sample
df.head()
df.tail()

# column names e.g. it clearly displays leading or tailing spaces
df.columns

# number of rows and columns in the dataset
df.shape

# index range, memory usage, column data types and number of missing values per column
df.info()

# --------------------------------
# Exploratory Data Analysis
# --------------------------------

# frequency count [syntax --- df.column.value_counts() or ds[col_index or name].value_counts(); dropna=False -- countmissing values]
print(df.city.value_counts(dropna=False))

# summary statistics
print(df.describe())

# --------------------------------------
# Visualizing Data - spotting outliers
# --------------------------------------

# Visualization 101
# 1. Bar plots for discrete data counts
# 2. Histograms for continuous data counts
# 3. Box plots - visualize basic summary statistics
# 4. Scatter plots - find relationship between 2 numeric variables

df.price.plot('hist')
plt.show()

# slicing data - using list comprehensions
df[df.price > 100000]

# box plot is for numeric value over some categories
# e.g. real estate price by city
df.boxplot(column="price", by="city")
plt.show()

# scatter plot are ideal for visualizing two numeric columns
df.plot(kind='scatter', x='initial_cost', y='total_est_fee', rot=70)
plt.show()

# --------------------------------
# Tidy Data
# --------------------------------

# formalizes thw way we describe the shape of data
# gives us a goal when formatting our data
# standard way to organize data values withing a dataset
#   1. columns represent separate variables
#   2. rows represent individual observations
#   3. observational units from tables
# tidy data makes it easier to fix common data problems
# pl.melt() - convert columns into variables -- make it untidy
# melting data is the process of turning columns into rows
# not always a good idea to do this...

pd.melt(df, id_vars=['Month', 'Day'],
        var_name='measurement', value_name='reading')

# pivoting - opposite to melting i.e. turning rows into columns
#            turning unique rows into columns dataset.pivot()
# pivot table - has a way to deal with duplicate data points as regular pivot would fail

# turn column measurement and value into pivot table [columns], multi-index;
pivot_dataset = df.pivot_table(
    index=['Month', 'Day'], columns='measurement', values='reading')

# pivoting gives hierarchical index aka multi index data frame; to turn it back to original df use reset_index()

# pivot with aggregate function - np.mean to get rid of duplicates
pivot_dataset2 = df.pivot_table(
    index=['Month', 'Day'], columns='measurement', values='reading', aggfunc=np.mean)

# extracting columns by slicing
pivot_dataset2['gender'] = pivot_dataset2.variable.str[0]
pivot_dataset2['age_group'] = pivot_dataset2.variable.str[1:]

# checking data types 
# df.dtypes then df[col].to_numeric() etc.

# combining/ concatinating data sets
# pandas concat i.e. pd.concat(set1, set 2) -- keep in mind that row index stays as per the original !!! multiple 0, 1,2,3 etc.
# use ignore_index = true to reset index of the new dataframe
# use axis=1 to concat columns of data, axis=0 for rows of data

# merging data - similar to SQL merge
# pd.merge(left=, right=, on=, left_on=, right_on=)   -- use on= or left_on= + right_on = to specify the keys
# merge types: one to one, one-to-many, many-to-many (duplicate keys)

site = pd.DataFrame()
visited = pd.DataFrame()
o2o = pd.merge(left=site, right=visited, left_on='name', right_on='site')

# column type casting; e.g. categorical column/ variables reduce the size of the dataframe
tips = pd.DataFrame()
tips.sex = tips.sex.astype('category')

# convert to numeric column
# the 'total_bill' and 'tip' columns in this DataFrame are stored as object types because the string 'missing' is used in these columns to encode missing values.
# by coercing the values into a numeric type, they become proper NaN values.
pd.to_numeric(tips['total_bill'], errors='coerce')

# applying functions to columns - pd.apply(function_name, axis=, pattern=)
def decode_gender(gender):
    if gender == 'Female':
        return 0   
    elif gender == 'Male':
        return 1 
    else:
        return np.nan

tips['decode'] = tips.sex.apply(decode_gender, )

# or using lambda
tips['decode-female'] = tips.sex.apply(lambda x: x.replace('Female', True) , )


# --------------------------------
# Missing Data
# --------------------------------

# df.into() -- gives basic info including missing values, data types etc.

# dropping duplicates - df.drop_duplicates() 
# NaN -- leave, drop or fill missing values
# drop missing values in entire data frame df.dropna() -- dropping rows (be careful)
# fill missing values by column - df[col].fillna('missing') --- can be applied to multiples col @ once 
# fill missing values with statistical data (instead of 0s) etc.

# testing with assert() -- takes a predicate and evaluates to a bool
# e.g. assert pd.notnull(ebola).all().all() -- the first .all() method will return a True or False for each column, 
#      while the second .all() method will return a single True or False.

