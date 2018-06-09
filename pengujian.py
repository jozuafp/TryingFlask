# Put your Dash code here
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="ticks")

dataPJoz = {
    '3': [89, 89, 90, 90, 88, 90, 85, 85],
    '5': [88, 89, 90, 90, 90, 90, 87, 91],
    '7': [88, 88, 90, 90, 90, 90, 89, 92],
    '9': [88, 87, 90, 89, 90, 90, 88, 88],
    '11': [88, 86, 89, 88, 90, 90, 87, 89],
    '13': [90, 87, 89, 88, 89, 90, 88, 89]
}

d = {'ndata': [], 'percentage': [], 'k': []}
for k in dataPJoz:
    for (ndata, percentage) in enumerate(dataPJoz[k]):
        d['ndata'].append(ndata)
        d['percentage'].append(percentage)
        d['k'].append(k)
df = pd.DataFrame(data=d)

print('Transformasi Data')
print(df.head())

# Initialize a grid of plots with an Axes for each walk
grid = sns.FacetGrid(df, col="k", hue="k", col_wrap=3, size=1.5)

# Draw a horizontal line to show the starting point
grid.map(plt.axhline, y=0, ls=":", c=".5")

# Draw a line plot to show the trajectory of each random walk
grid.map(plt.plot, "ndata", "percentage", marker="o", ms=4)

# Adjust the tick positions and labels
maxPosition = max(d['percentage'])
minPosition = min(d['percentage'])
grid.set(ylim=[minPosition, maxPosition])
'''
grid.set(xticks=np.arange(5), yticks=[-3, 3],
         xlim=(-.5, 4.5), ylim=(-3.5, 3.5))
'''

# Adjust the arrangement of the plots
grid.fig.tight_layout(w_pad=1)
plt.show()

sns.set(style="ticks")
