import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
 
# Load Dataset
data = pd.read_csv("HousePrice.csv")
 
# Independent Variable
X = data[['Area']]
 
# Dependent Variable
y = data['Price']
 
# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
   X,
   y,
   test_size=0.2,
   random_state=42
)
 
# Create Model
model = LinearRegression()
 
# Train Model
model.fit(X_train, y_train)
 
# Predict
y_pred = model.predict(X_test)
 
print("Actual Price\tPredicted Price")
 
for actual, predicted in zip(y_test, y_pred):
   print(actual, "\t", round(predicted,2))
 
print("\nMean Squared Error :", mean_squared_error(y_test, y_pred))
print("R2 Score :", r2_score(y_test, y_pred))
 
SAMPLE DATASET (HousePrice.csv)
| Area | Price   |
| ---- | ------- |
| 1000 | 2500000 |
| 1200 | 3000000 |
| 1500 | 3700000 |
| 1800 | 4500000 |
| 2000 | 5200000 |
| 2500 | 6500000 |
| 3000 | 7800000 |
