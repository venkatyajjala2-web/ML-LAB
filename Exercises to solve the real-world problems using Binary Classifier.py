import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
 
# Load Dataset
data = pd.read_csv("Social_Network_Ads.csv")
 
# Select Features
X = data[['Age', 'EstimatedSalary']]
 
# Target Variable
y = data['Purchased']
 
# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
   X,
   y,
   test_size=0.25,
   random_state=42
)
 
# Create Model
model = LogisticRegression()
 
# Train Model
model.fit(X_train, y_train)
 
# Predict
y_pred = model.predict(X_test)
 
# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))
 
# Confusion Matrix
print("\nConfusion Matrix")
print(confusion_matrix(y_test, y_pred))
