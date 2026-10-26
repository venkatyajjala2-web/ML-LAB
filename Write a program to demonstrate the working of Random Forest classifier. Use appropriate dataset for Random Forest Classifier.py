# Import required libraries
 
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
 
# Load dataset
iris = load_iris()
 
X = iris.data
y = iris.target
 
# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.3, random_state=42
)
 
# Create Random Forest model
rf = RandomForestClassifier(
   n_estimators=100,
   random_state=42
)
 
# Train model
rf.fit(X_train, y_train)
 
# Predict
y_pred = rf.predict(X_test)
 
# Accuracy
accuracy = accuracy_score(y_test, y_pred)
 
print("Accuracy:", accuracy)
 
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
 
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
 
# Feature Importance
print("\nFeature Importance:")
for feature, importance in zip(iris.feature_names, rf.feature_importances_):
   print(f"{feature}: {importance:.4f}")
