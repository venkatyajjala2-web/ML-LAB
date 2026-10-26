import pandas as pd
 
# Sample Dataset
data = {
   "Name": ["Ram", "Sita", "John", "Ravi"],
   "Gender": ["Male", "Female", "Male", "Male"],
   "City": ["Delhi", "Mumbai", "Delhi", "Chennai"]
}
 
df = pd.DataFrame(data)
 
print("Original Dataset")
print(df)
 
# One-Hot Encoding
encoded_df = pd.get_dummies(df, columns=["Gender", "City"])
 
print("\nOne-Hot Encoded Dataset")
print(encoded_df)
 
Sample Dataset:
 
Original Dataset
 
  Name Gender     City
0   Ram   Male    Delhi
1  Sita Female   Mumbai
2  John   Male    Delhi
3  Ravi   Male  Chennai
 
One-Hot Encoded Dataset
 
  Name  Gender_Female  Gender_Male  City_Chennai  City_Delhi  City_Mumbai
0   Ram              0            1             0           1            0
1  Sita              1            0             0           0            1
2  John              0            1             0           1            0
3 Ravi              0            1             1           0            0
