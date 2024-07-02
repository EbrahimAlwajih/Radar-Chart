import matplotlib.pyplot as plt
from math import pi
import os
import pandas as pd

class RadarChart:
    def __init__(self, categories, folder_path):
        self.categories = categories
        self.folder_path = folder_path
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)

    def make_radar_chart(self, values, group_name):
        N = len(self.categories)
        values += values[:1]
        angles = [n / float(N) * 2 * pi for n in range(N)]
        angles += angles[:1]

        plt.rcParams.update({'font.size': 12})
        plt.figure(dpi=100, figsize=(4.1, 3))
        ax = plt.subplot(111, polar=True)
        ax.plot(angles, values, linewidth=1, linestyle='solid', label=group_name)
        ax.set_rlabel_position(0)
        ax.fill(angles, values, 'b', alpha=0.1)

        plt.yticks([0.2, 0.4, 0.6, 0.8], ["0.2", "0.4", "0.6", "0.8"], color="grey", size=7)
        plt.ylim(0, 1)
        plt.xticks(angles[:-1], self.categories)
        plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1), fontsize='large', prop={'weight': 'bold'})

        svg_path = os.path.join(self.folder_path, group_name + '.svg')
        plt.savefig(svg_path)
        plt.close()

    def create_charts_from_csv(self, csv_file):
        df = pd.read_csv(csv_file)
        for index, row in df.iterrows():
            model_name = row['model']
            values = row[1:].tolist()
            self.make_radar_chart(values, model_name)


if __name__ == "__main__":
    categories = ['MAE', 'MSE', 'RMSE', 'R2', 'MedAE', 'EV', 'MBD', 'Adj_R2']
    results_file = 'data.csv'
    folder_path = './Figures/radar_chart'

    radar_chart = RadarChart(categories, folder_path)
    radar_chart.create_charts_from_csv(results_file)
