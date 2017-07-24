import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

fruits = pd.read_table('fruit_data_with_colors.txt')

# print fruits.head()
lookup_fruit_name = dict(zip(fruits.fruit_label.unique(), fruits.fruit_name.unique()))
# print lookup_fruit_name

# create train-test split
# This function randomly shuffles the dataset and splits off a certain percentage of the input samples for use as a training set, and then puts the remaining samples into a different variable for use as a test set. 
x = fruits[['mass','width','height']]
y = fruits['fruit_label']

# capital X means two dimensional array or data frame, y means one dimensional array
X_train, X_test, y_train, y_test = train_test_split(X,y, random_state = 0) 
print X_train, X_test, y_train, y_test 