from utils import *

train = TrainingDataset('./data/train.csv')
ideal = IdealFunctions('./data/ideal.csv')
test = TestingDataset('./data/test.csv')
db = DataBase('results.db')
plotter = Plotter()

#Pushing Data to DB
db.push_df_to_db('train',train.df)
db.push_df_to_db('ideal',ideal.df)

#Finding Ideal Functions
ideal_functions = ideal.find_ideal_functions(train)

#Calculating Max Deviations
max_devs = ideal.max_deviations(train)

#Mapping Test Data to Ideal Functions
test_results = test.map_to_ideal_function(ideal, max_devs)

#Plotting
plotter.create_train_plot(train)
plotter.create_test_plot(test)
plotter.create_ideal_plot(ideal, ideal_functions)
plotter.save_and_show_plot()

#Pushing Test Results to DB
db.push_df_to_db('results', pd.DataFrame(test_results))

print('Done!')