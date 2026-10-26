import pandas as pd
 
data = pd.read_csv("EnjoySport.csv")
hypothesis = None
 
for _, row in data.iterrows():
   x = row[:-1].tolist()
   y = row[-1]
   if str(y).lower() == "yes":
       if hypothesis is None:
           hypothesis = x
       else:
           for i in range(len(hypothesis)):
               if hypothesis[i] != x[i]:
                   hypothesis[i] = "?"
 
print("Most Specific Hypothesis:")
print(hypothesis)
SAMPLE CSV
Sky,AirTemp,Humidity,Wind,Water,Forecast,EnjoySport
Sunny,Warm,Normal,Strong,Warm,Same,Yes
Sunny,Warm,High,Strong,Warm,Same,Yes
Rainy,Cold,High,Strong,Warm,Change,No
Sunny,Warm,High,Strong,Cool,Change,Yes
