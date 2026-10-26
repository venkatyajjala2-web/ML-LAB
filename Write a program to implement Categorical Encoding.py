import pandas as pd
from sklearn.preprocessing import LabelEncoder
# Sample Dataset
data = {
   "Name": ["Ram", "Sita", "John", "Ravi"],
   "Department": ["CSE", "ECE", "EEE", "CSE"]
}
df = pd.DataFrame(data)
print("Original Dataset")
print(df)
 
# Label Encoding
encoder = LabelEncoder()
df["Department_Encoded"] = encoder.fit_transform(df["Department"])
print("\nEncoded Dataset")
print(df)
print("\nCategory Mapping")
for category, value in zip(encoder.classes_, encoder.transform(encoder.classes_)):
   print(category, "->", value)
