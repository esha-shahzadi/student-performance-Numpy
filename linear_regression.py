# Linear Regression - Study Hours vs Exam Score
# Predicts a student's exam score from the hours studied using scikit-learn

# Step 1 - Import Libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# Step 2 - Dataset
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
y = np.array([35, 42, 50, 58, 65, 72, 78, 85, 90, 95])

# Step 3 - Create and Train Model
model = LinearRegression()
model.fit(X, y)

# Step 4 - Get Coefficients
slope = model.coef_[0]
intercept = model.intercept_
print("Slope (m)     :", round(slope, 2))
print("Intercept (b) :", round(intercept, 2))
print("Equation      : y =", round(slope, 2), "x +", round(intercept, 2))

# Step 5 - Predictions
y_pred = model.predict(X)
print("\nPredicted Scores:", y_pred.round(2))

# Step 6 - Model Evaluation
r2 = r2_score(y, y_pred)
mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)
print("\nR2 Score :", round(r2, 4))
print("MSE      :", round(mse, 4))
print("RMSE     :", round(rmse, 4))

# Step 7 - Predict New Value
hours = 6
predicted_score = model.predict([[hours]])
print(f"\nPrediction: {hours} hours study -> Score = {predicted_score[0]:.2f}")

# Step 8 - Plot Graph
plt.figure(figsize=(8, 5))
plt.scatter(X, y, color='blue', label='Actual Scores', zorder=5)
plt.plot(X, y_pred, color='red', linewidth=2, label='Regression Line')
plt.xlabel('Study Hours')
plt.ylabel('Exam Score')
plt.title('Linear Regression - Study Hours vs Exam Score')
plt.legend()
plt.grid(True)
plt.show()
