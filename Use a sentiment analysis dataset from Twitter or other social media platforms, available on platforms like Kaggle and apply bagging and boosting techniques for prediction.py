Dataset:  Download the Twitter Sentiment Analysis Dataset from Kaggle.
Example dataset:  Twitter Sentiment Analysis  (File: twitter_training.csv)
 
# Import libraries
import pandas as pd
 
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
 
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import AdaBoostClassifier
 
from sklearn.tree import DecisionTreeClassifier
 
from sklearn.metrics import accuracy_score, classification_report
 
# Load dataset
df = pd.read_csv("twitter_training.csv")
 
# Keep only required columns
df = df[['Tweet', 'Sentiment']]
 
# Remove missing values
df.dropna(inplace=True)
 
# Convert text into numerical features
vectorizer = TfidfVectorizer(stop_words='english')
 
X = vectorizer.fit_transform(df['Tweet'])
y = df['Sentiment']
 
# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
   X,
   y,
   test_size=0.2,
   random_state=42
)
 
##################################################
# Bagging Classifier
##################################################
 
bagging = BaggingClassifier(
   estimator=DecisionTreeClassifier(),
   n_estimators=100,
   random_state=42
)
 
bagging.fit(X_train, y_train)
 
bag_pred = bagging.predict(X_test)
 
print("Bagging Accuracy:")
print(accuracy_score(y_test, bag_pred))
 
print("\nBagging Classification Report")
print(classification_report(y_test, bag_pred))
 
##################################################
# Boosting (AdaBoost)
##################################################
 
boosting = AdaBoostClassifier(
   n_estimators=100,
   random_state=42
)
 
boosting.fit(X_train, y_train)
 
boost_pred = boosting.predict(X_test)
 
print("\nBoosting Accuracy:")
print(accuracy_score(y_test, boost_pred))
 
print("\nBoosting Classification Report")
print(classification_report(y_test, boost_pred))
