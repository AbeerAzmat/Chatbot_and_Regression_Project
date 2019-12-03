# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 22:20:05 2019

@author: Abeer Azmat
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
mydataset = pd.read_csv('aids.csv')
X = mydataset.iloc[:, :-1].values
y = mydataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)
