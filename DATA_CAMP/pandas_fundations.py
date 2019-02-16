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
data = {'state':'ON', 'city':cities}
df = pd.DataFrame(data) 
print(df.head())