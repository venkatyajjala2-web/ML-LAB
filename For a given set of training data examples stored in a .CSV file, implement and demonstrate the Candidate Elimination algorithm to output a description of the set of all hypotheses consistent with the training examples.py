import pandas as pd
 
data = pd.read_csv("EnjoySport.csv")
 
concepts = data.iloc[:, :-1].values
target = data.iloc[:, -1].values
 
specific = concepts[0].copy()
general = [["?" for _ in range(len(specific))] for _ in range(len(specific))]
 
for i, h in enumerate(concepts):
   if target[i].lower() == "yes":
       for x in range(len(specific)):
           if h[x] != specific[x]:
               specific[x] = "?"
               general[x][x] = "?"
   else:
       for x in range(len(specific)):
           if h[x] != specific[x]:
               general[x][x] = specific[x]
           else:
               general[x][x] = "?"
 
general = [g for g in general if g != ["?"]*len(specific)]
 
print("Specific Boundary:")
print(specific)
print("\nGeneral Boundary:")
for g in general:
   print(g)
 
SAMPLE CSV (EnjoySport.csv)
Sky,AirTemp,Humidity,Wind,Water,Forecast,EnjoySport
Sunny,Warm,Normal,Strong,Warm,Same,Yes
Sunny,Warm,High,Strong,Warm,Same,Yes
Rainy,Cold,High,Strong,Warm,Change,No
Sunny,Warm,High,Strong,Cool,Change,Yes
