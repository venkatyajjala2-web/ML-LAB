from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
 
# Load Iris Dataset
iris = load_iris()
X = iris.data
y = iris.target
 
# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
   X, y, test_size=0.3, random_state=42)
 
# Train KNN Model
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
 
# Predictions
y_pred = knn.predict(X_test)
 
print("Actual  Predicted")
correct = 0
wrong = 0
 
for actual, pred in zip(y_test, y_pred):
   print(actual, "      ", pred)
   if actual == pred:
       correct += 1
   else:
       wrong += 1
 
print("\nCorrect Predictions :", correct)
print("Wrong Predictions  :", wrong)
print("Accuracy :", accuracy_score(y_test, y_pred))
