from matplotlib import colors
from matplotlib.colors import to_rgba
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data= pd.read_csv("data/data_clean.csv")

fig, ax= plt.subplots()
year= ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
emissions= [84150.23, 82007.46, 79309.94, 79772.02, 76235.15, 78486.74, 79468.30, 81792.16, 78558.03, 79740.74, 73592.02]
bar_labels= ['b', 'g', 'b', 'c', 'r', 'g', 'r', 'b', 'r', 'g', 'b']
bar_colors= ['tab:blue', 'tab:green', 'tab:blue', 'tab:cyan', 'tab:red', 'tab:green', 'tab:red', 'tab:blue', 'tab:red', 'tab:green', 'tab:blue']
ax.bar(year, emissions, label=bar_labels, color=bar_colors)
plt.title('Austria')
fig.set_size_inches(10,5)
plt.show()

fig, ax= plt.subplots()
year= ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
emissions= [133645.77, 123133.69, 120361.60, 120458.32, 114768.44, 118955.47, 117417.88, 117097.88, 117594.04, 116448.19, 106433.26]
bar_labels= ['b', 'g', 'b', 'c', 'r', 'g', 'r', 'b', 'r', 'g', 'b']
bar_colors= ['tab:blue', 'tab:green', 'tab:blue', 'tab:cyan', 'tab:red', 'tab:green', 'tab:red', 'tab:blue', 'tab:red', 'tab:green', 'tab:blue']
ax.bar(year, emissions, label=bar_labels, color=bar_colors)
plt.title('Belgium')
fig.set_size_inches(10,5)
plt.show()

fig, ax= plt.subplots()
year= ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
emissions= [512753.49, 488753.45, 490256.23, 491335.79, 461189.49, 464491.27, 466376.98, 469718.63, 450787.08, 441488.01, 399412.67]
bar_labels= ['b', 'g', 'b', 'c', 'r', 'g', 'r', 'b', 'r', 'g', 'b']
bar_colors= ['tab:blue', 'tab:green', 'tab:blue', 'tab:cyan', 'tab:red', 'tab:green', 'tab:red', 'tab:blue', 'tab:red', 'tab:green', 'tab:blue']
ax.bar(year, emissions, label=bar_labels, color=bar_colors)
plt.title('France')
fig.set_size_inches(10,5)
plt.show()

fig, ax= plt.subplots()
year= ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
emissions= [61948.12, 57742.79, 58764.94, 58550.21, 58006.16, 60477.26, 62714.61, 62066.84, 62351.96, 59855.48, 57716.09]
bar_labels= ['b', 'g', 'b', 'c', 'r', 'g', 'r', 'b', 'r', 'g', 'b']
bar_colors= ['tab:blue', 'tab:green', 'tab:blue', 'tab:cyan', 'tab:red', 'tab:green', 'tab:red', 'tab:blue', 'tab:red', 'tab:green', 'tab:blue']
ax.bar(year, emissions, label=bar_labels, color=bar_colors)
plt.title('Ireland')
fig.set_size_inches(10,5)
plt.show()

fig, ax= plt.subplots()
year= ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
emissions= [12168.53, 12052.28, 11809.92, 11276.75, 10797.43, 10317.72, 10078.73, 10261.75, 10561.47, 10732.70, 9064.90]
bar_labels= ['b', 'g', 'b', 'c', 'r', 'g', 'r', 'b', 'r', 'g', 'b']
bar_colors= ['tab:blue', 'tab:green', 'tab:blue', 'tab:cyan', 'tab:red', 'tab:green', 'tab:red', 'tab:blue', 'tab:red', 'tab:green', 'tab:blue']
ax.bar(year, emissions, label=bar_labels, color=bar_colors)
plt.title('Luxembourg')
fig.set_size_inches(10,5)
plt.show()

fig, ax= plt.subplots()
year= ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
emissions= [211583.23, 197244.08, 193009.40, 193342.44, 185548.93, 192648.93, 193058.39, 190568.24, 185596.91, 179837.65, 163915.18]
bar_labels= ['b', 'g', 'b', 'c', 'r', 'g', 'r', 'b', 'r', 'g', 'b']
bar_colors= ['tab:blue', 'tab:green', 'tab:blue', 'tab:cyan', 'tab:red', 'tab:green', 'tab:red', 'tab:blue', 'tab:red', 'tab:green', 'tab:blue']
ax.bar(year, emissions, label=bar_labels, color=bar_colors)
plt.title('Netherlands')
fig.set_size_inches(10,5)
plt.show()

fig, ax= plt.subplots()
year= ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
emissions= [54669.67, 50552.38, 51901.42, 52785.70, 48845.03, 48355.48, 48631.38, 47754.08, 46256.93, 45973.87, 43290.99]
bar_labels= ['b', 'g', 'b', 'c', 'r', 'g', 'r', 'b', 'r', 'g', 'b']
bar_colors= ['tab:blue', 'tab:green', 'tab:blue', 'tab:cyan', 'tab:red', 'tab:green', 'tab:red', 'tab:blue', 'tab:red', 'tab:green', 'tab:blue']
ax.bar(year, emissions, label=bar_labels, color=bar_colors)
plt.title('Switzerland')
fig.set_size_inches(10,5)
plt.show()