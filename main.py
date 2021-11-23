import pandas as pd
import matplotlib.pyplot as plt


class DrawingPlots:

    file_name = 'deviation.json'
    data_frame = None

    def __init__(self, file_name=None):
        if file_name:
            self.file_name = file_name

    def draw_plots(self):
        plots = []
        self.data_frame = pd.read_json(self.file_name)
        plt.bar(self.data_frame["name"], self.data_frame["rb_corners"], color='blue')
        plt.bar(self.data_frame["name"], self.data_frame["gt_corners"], color='red')
        first_plot = 'plots/first.png'
        plt.savefig('plots/first.png')
        plots.append(first_plot)

        return plots







