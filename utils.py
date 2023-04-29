import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from sqlalchemy import create_engine
from bokeh.io import output_file, show
from bokeh.layouts import gridplot
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure


class Dataset:
    def __init__(self, filename):
        self.df = pd.read_csv(filename, index_col='x')

class TrainingDataset(Dataset):
    def __init__(self, filename):
        super().__init__(filename)

class IdealFunctions(Dataset):
    def __init__(self, filename):
        super().__init__(filename)

    def find_ideal_functions(self, training_dataset):
        # Find the ideal functions based on mean squared error (MSE) values.
        self.ideal_functions = {}
        for col in training_dataset.df.columns:
            mse_values = []
            for ideal_col in self.df.columns:
                mse_values.append(mean_squared_error(training_dataset.df[col], self.df[ideal_col]))
            min_mse = min(mse_values)
            min_mse_index = mse_values.index(min_mse)
            self.ideal_functions[col] = f'y{min_mse_index + 1}'
        return self.ideal_functions
    
    def max_deviations(self, training_dataset):
        # Calculate the maximum deviations between the training dataset and the ideal functions.
        max_devs = {}
        for train_col, ideal_col in self.ideal_functions.items():
            deviations = training_dataset.df[train_col] - self.df[ideal_col]
            max_devs[ideal_col] = max(abs(deviations))
        return max_devs

class TestingDataset(Dataset):
    def __init__(self, filename):
        super().__init__(filename)

    # Map the testing dataset values to ideal functions based on maximum deviations.
    def map_to_ideal_function(self, idealfunctions_dataset, max_deviations):
        test_array = np.array(self.df.reset_index())
        mappings = []
        for x,y in test_array:
            devs = {}
            for ideal_col, deviation in max_deviations.items():
                dev = abs(idealfunctions_dataset.df.loc[x, ideal_col] - y)
                if dev <= deviation:
                    devs[ideal_col] = dev
            if not devs:
                mappings.append({'X (test func)': x, 'Y (test func)': y, 'Delta Y (test func)': 'Too high', 'Ideal function': 'No ideal function'})
            else:
                min_dev =min(devs, key=devs.get)
                mappings.append({'X (test func)': x, 'Y (test func)': y, 'Delta Y (test func)': devs[min_dev], 'Ideal function': min_dev})
        return mappings

class DataBase:
    def __init__(self,db_name):
        self.engine = create_engine('sqlite:///' + db_name)

    # Push the dataframe to the specified table in the database.
    def push_df_to_db(self, table_name, dataframe):
        dataframe.to_sql(table_name, self.engine, if_exists='replace')

class Plotter:
    def __init__(self):
        self.output_file = 'visualization.html'
        self.train_plot = None
        self.test_plot = None
        self.ideal_plots = []
        self.gridplot = None

    # Plot the training dataset
    def create_train_plot(self, train_dataset):
        train_source = ColumnDataSource(train_dataset.df)
        self.train_plot = figure(title='Training Dataset', x_axis_label='x', y_axis_label='y')
        self.train_plot.circle('x', 'y1', color='red', legend_label='y1', source=train_source)
        self.train_plot.circle('x', 'y2', color='blue', legend_label='y2', source=train_source)
        self.train_plot.circle('x', 'y3', color='green', legend_label='y3', source=train_source)
        self.train_plot.circle('x', 'y4', color='yellow', legend_label='y4', source=train_source)

    # Plot the testing dataset
    def create_test_plot(self, test_dataset):
        test_source = ColumnDataSource(test_dataset.df)
        self.test_plot = figure(title='Testing Dataset', x_axis_label='x', y_axis_label='y')
        self.test_plot.circle('x', 'y', color='red', legend_label='y', source=test_source)

    # Plot the ideal functions
    def create_ideal_plot(self, ideal_dataset, ideal_functions):
        ideal_source = ColumnDataSource(ideal_dataset.df)
        self.ideal_plot = figure(title='Ideal Functions', x_axis_label='x', y_axis_label='y')
        for i in ideal_functions.values():
            self.ideal_plot.line('x', i, color='black', legend_label=i, source=ideal_source)

    # Save and show the plot
    def save_and_show_plot(self):
        output_file(self.output_file)
        grid = [[self.train_plot, self.test_plot, self.ideal_plot]]
        show(gridplot(grid))