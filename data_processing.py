# Data Preprocessing Script
# Author: Abeer Azmat

# -----------------------------
# 1. Import Required Libraries
# -----------------------------
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# -----------------------------
# 2. Load the Dataset
# -----------------------------
# Assumes 'aids.csv' is located in the 'data/' folder
data = pd.read_csv('data/aids.csv')

# Separate independent variable (Year) and dependent variable (Deaths)
X = data.iloc[:, :-1].values  # All rows, all columns except last
y = data.iloc[:, -1].values   # All rows, last column

# -----------------------------
# 3. Splitting the dataset into the Training set and Test set from sklearn.model_selection import train_test_split 
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=1/3, random_state=0
)

# Optional: Print shapes to verify
print("Training features shape:", X_train.shape)
print("Test features shape:", X_test.shape)
print("Training labels shape:", y_train.shape)
print("Test labels shape:", y_test.shape)

