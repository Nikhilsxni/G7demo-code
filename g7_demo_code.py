# -*- coding: utf-8 -*-
"""
@author: NIKHIL SONI 
student Id : 22045846
"""
import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset into a Pandas DataFrame
df = pd.read_csv("g7_demo.csv")

# Extract the  Total population and life Expectancy columns
countries = df['Countries']
life_exp = df['Life Expectancy']

# adding title and labels
plt.title('LIFE EXPECTANCY OF G7 COUNTRIES', fontweight = 'heavy', fontsize = 15, color='red')
plt.xlabel('Countries', fontweight = 'bold', fontsize = 12, style = 'italic')
plt.ylabel('Life Expectancy', fontweight = 'bold', fontsize = 15)

# Create a line plot
plt.plot(countries, life_exp, color='green', linestyle = 'solid', marker = 'o', 
         markerfacecolor = 'red', markersize = 12)

# Show the plot
plt.show()
