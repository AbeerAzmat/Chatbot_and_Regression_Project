# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 22:22:04 2019

@author: Abeer Azmat
"""

# Simple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
mydataset = pd.read_csv('aids.csv')
X = mydataset.iloc[:, :-1].values
y = mydataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)
regressor.predict(X_test)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

# Visualising the Training set results
plt.scatter(X_train, y_train,color = 'yellow')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Death vs Years (Training set)')
plt.xlabel('Years')
plt.ylabel('Death')
plt.show()

# Visualising the Test set results
plt.scatter(X_test, y_test, color = 'green')
plt.plot(X_train, regressor.predict(X_train), color = 'red')
plt.title('Death vs Years (Test set)')
plt.xlabel('Years')
plt.ylabel('Death')
plt.show()