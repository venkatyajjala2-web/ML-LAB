# Import libraries
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
 
# Load Dataset
iris = load_iris()
 
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["target"] = iris.target
 
# Create Duplicate Rows
df = pd.concat([df, df.iloc[:5]], ignore_index=True)
 
print("Dataset Shape Before Removing Duplicates:", df.shape)
 
# Remove duplicate rows
df = df.drop_duplicates()
 
print("Dataset Shape After Removing Duplicates:", df.shape)
 
# Split Dataset
 
X = df.iloc[:, :-1]
y = df.iloc[:, -1]
 
X_train, X_test, y_train, y_test = train_test_split(
   X, y, test_size=0.3, random_state=42
)
 
# Decision Tree Model
 
model = DecisionTreeClassifier(max_depth=3)
 
model.fit(X_train, y_train)
 
# Prediction
y_pred = model.predict(X_test)
 
accuracy = accuracy_score(y_test, y_pred)
 
print("\nModel Accuracy:", accuracy)
 
# Cross Validation
scores = cross_val_score(model, X, y, cv=5)
 
print("\nCross Validation Scores:", scores)
print("Average Cross Validation Accuracy:", scores.mean())
 
# -----------------------------
# Bias and Variance (Simple Explanation)
# -----------------------------
print("\nBias: Error due to overly simple assumptions.")
print("Variance: Error due to model sensitivity to training data.")
 
