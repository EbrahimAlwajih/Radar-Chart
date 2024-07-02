import numpy as np
import matplotlib.pyplot as plt
from math import pi
import os

def make_radar_chart(categories, values, group_name, folder_path):
  
    N = len(categories)
    values += values[:1]
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]
    plt.rcParams.update({'font.size': 12})
    plt.figure(dpi=100, figsize=(4.1,3))
    ax = plt.subplot(111, polar=True)
    ax.plot(angles, values, linewidth=1, linestyle='solid', label=group_name)
    ax.set_rlabel_position(0)
    ax.fill(angles, values, 'b', alpha=0.1)
    plt.yticks([0.2, 0.4, 0.6, 0.8], ["0.2", "0.4", "0.6", "0.8"], color="grey", size=7)
    plt.ylim(0, 1)
    plt.xticks(angles[:-1], categories)
    plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1),fontsize='large', prop={'weight': 'bold'})
    # plt.show()
    
    svg_path = os.path.join(folder_path, group_name + '.svg')
    plt.savefig(svg_path)#, dpi=100, figsize=(4.1,3))
    
categories = ['MAE',	'MSE',	        'RMSE',	        'R2',		 'MedAE', 	    'EV',	        'MBD',	        'Adj_R2']

# dic = {
# 'Ext':	[0.4,0.2,0.32,0.19,0.46,0.09,0.19,0.1],
# 'KNN':	[0.45,0.27,0.41,0.27,0.52,0.19,0.27,0.19],
# 'RF':	[0.7,0.44,0.58,0.44,0.73,0.38,0.44,0.4],
# 'Bag':	[0.89,0.55,0.67,0.54,0.9,0.4,0.54,0.42],
# 'CAT':	[0.66,0.57,0.69,0.57,0.69,0.52,0.57,0.53],
# 'SVR':	[0.73,0.7,0.79,0.7,0.79,0.79,0.7,0.89],
# 'Grd':	[0.8,0.75,0.83,0.75,0.8,0.8,0.75,0.75],
# 'AdaBt':[1,1,1,1,1,1,1,1],
# 'Model1':[0,0,0,0,0,0,0,0],
# 'Model2':[0.25,0.07,0.14,0.06,0.38,0.09,0.06,0.11],
# 'Model3':[0.26,0.12,0.22,0.11,0.38,0.15,0.11,0.18],
# 'Model4':[0.21,0.13,0.23,0.12,0.19,0.15,0.12,0.18],
# 'Model5':[0.26,0.14,0.25,0.14,0.38,0.19,0.14,0.21],
# }

import pandas as pd
import os
results_file = os.path.join('data.csv')
folder_path = os.path.join('.\\Figures\\radar_chart')
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

df = pd.read_csv(results_file)
models = {}

for index, row in df.iterrows():
    key = row['model']
    # models[key] = row[1:].values
    values = row[1:].tolist()
    models[key] = values

for name, values in models.items():
    make_radar_chart(categories, values, name, folder_path)
