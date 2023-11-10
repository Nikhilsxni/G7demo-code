# -*- coding: utf-8 -*-
"""
@author: NIKHIL SONI 
student Id : 22045846
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv(r"C:\assigment 1, ADS\supercars.csv")

name = df['Car Model'].head(8)
price = df['Price (in USD)'].head(8)

# Figure Size
fig, ax = plt.subplots(figsize =(16, 9))

# Horizontal Bar Plot
ax.barh(name, price)

# Add Plot Title
plt.title('SPORTS CAR PRICES', fontweight = 'heavy', fontsize = 15, color='red')
plt.xticks(np.arange(0, 8, step=1)
plt.xlabel("(in USD)",fontweight = 'bold', fontsize = 12)
# Show Plot
plt.show()

