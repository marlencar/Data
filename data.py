import numpy as np
import pandas as pd
my_data = np.random.randint(101, size=(3,4))
my_columns_names = ['Eleanor', 'Chidi', 'Tahani', 'Jason']
my_dataframe = pd.DataFrame(data=my_data, columns=my_columns_names)
print(my_dataframe)
print('Second row of Eleanor column: ', my_dataframe['Eleanor'][1])
my_dataframe['Janet'] = my_dataframe ['Tahani'] + my_dataframe['Jason']
print(my_dataframe)