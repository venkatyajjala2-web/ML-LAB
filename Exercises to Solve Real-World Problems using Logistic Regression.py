import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
 
# Load Dataset
data = pd.read_csv("Social_Network_Ads.csv")
 
# Independent Variables
X = data[['Age', 'EstimatedSalary']]
 
# Dependent Variable
y = data['Purchased']
 
# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
   X,
   y,
   test_size=0.25,
   random_state=42
)
 
# Feature Scaling
scaler = StandardScaler()
 
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
 
# Train Logistic Regression Model
model = LogisticRegression(random_state=42)
 
model.fit(X_train, y_train)
 
# Prediction
y_pred = model.predict(X_test)
 
# Display Actual and Predicted Values
print("Actual\tPredicted")
 
for actual, predicted in zip(y_test, y_pred):
   print(actual, "\t", predicted)
 
# Accuracy
print("\nAccuracy Score")
print(accuracy_score(y_test, y_pred))
 
# Confusion Matrix
print("\nConfusion Matrix")
print(confusion_matrix(y_test, y_pred))
 
# Classification Report
print("\nClassification Report")
print(classification_report(y_test, y_pred))
 
SAMPLE DATASET (Social_Network_Ads.csv)
 
