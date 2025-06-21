# Simple Linear Regression Model
# Author: Abeer Azmat

# -----------------------------
# 1. Import Required Libraries
# -----------------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# -----------------------------
# 2. Load the Dataset
# -----------------------------
# Make sure 'aids.csv' is placed inside the 'data/' folder
data = pd.read_csv('data/aids.csv')  # Adjust path if needed

# Assuming the dataset has two columns: [Year, Deaths]
# X → feature (Year), y → target (Death count)
X = data.iloc[:, :-1].values  # All rows, all columns except last
y = data.iloc[:, -1].values   # All rows, last column (Deaths)

# -----------------------------
# 3. Split into Train and Test Sets
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=1/3, random_state=0
)

# -----------------------------
# 4. Train the Linear Regression Model
# -----------------------------
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# -----------------------------
# 5. Predict on the Test Set
# -----------------------------
y_pred = regressor.predict(X_test)

# -----------------------------
# 6. Visualize Training Set Results
# -----------------------------
plt.figure(figsize=(8, 5))
plt.scatter(X_train, y_train, color='orange', label='Training Data')
plt.plot(X_train, regressor.predict(X_train), color='blue', label='Model Prediction')
plt.title('Deaths vs Years (Training Set)')
plt.xlabel('Year')
plt.ylabel('Deaths')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# -----------------------------
# 7. Visualize Test Set Results
# -----------------------------
plt.figure(figsize=(8, 5))
plt.scatter(X_test, y_test, color='green', label='Test Data')
plt.plot(X_train, regressor.predict(X_train), color='red', label='Trained Model')
plt.title('Deaths vs Years (Test Set)')
plt.xlabel('Year')
plt.ylabel('Deaths')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
