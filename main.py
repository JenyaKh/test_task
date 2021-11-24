import pandas as pd
import matplotlib.pyplot as plt
import os


class DrawingPlots:

    file_name = 'deviation.json'
    data_frame = None

    def draw_plots(self):
        result_path = []
        plt.rcParams.update({'figure.max_open_warning': 0})
        all_models = set()
        self.data_frame = pd.read_json(self.file_name)
        for model in self.data_frame.iterrows():
            file_name = model[1][0]
            if file_name not in all_models:
                all_models.add(file_name)
                data_model = self.data_frame[self.data_frame['name'] == file_name]
                data_model.plot(kind='bar', figsize=(12, 8), title=file_name)
                file_name = file_name.replace('/', '')
                path = f'plots/{file_name}.png'
                plt.savefig(path)
                result_path.append(os.path.abspath(path))
                plt.close()

        return result_path
