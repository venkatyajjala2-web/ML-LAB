import pandas as pd

df=pd.read_csv("student.csv")
df.head()
df.shape
df.info()
df.describe()
df.isnull().sum()
df.duplicated().sum()
df['age'].fillna(df['age'].median(), inplace=True)
or
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
from sklearn.preprocessing import LabelEncoder df['sex'] = LabelEncoder().fit_transform(df['sex']) df = pd.get_dummies(df, columns=['embarked'], drop_first=True)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
