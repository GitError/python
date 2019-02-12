""" DataCamp - Diagnose data for cleaning code snippets """

import matplotlib.pyplot as plt
import pandas as pd

# --------------------------------
# Inspecting pandas DataFrame
# --------------------------------

df = pd.read_csv(
    'http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv')

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

# Basics
# 1. Bar plots for discrete data counts
# 2. Histograms for continuous data counts

df.price.plot('hist')
plt.show()