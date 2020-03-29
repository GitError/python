import pandas as pd
import matplotlib.pyplot as plt


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