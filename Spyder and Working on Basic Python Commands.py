print("Welcome to Machine Learning Lab")
# Arithmetic
a=20
b=10
print(a+b)

# Loop
for i in range(1,6):
   print(i)

import math
print(math.sqrt(64))
 
#numpy
import numpy as np
arr=np.array([1,2,3,4,5])
print("array values",arr)
print('adding 5 to each element of the array',arr+5)
 
#pandas
import pandas as pd
a={'stuname':['raju','rama','sita'],'stuno':[1,2,3],'marks':[90,80,70]}
df=pd.DataFrame(a)
print("dataframe values\n",df)
 
#Data visualization
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]
 
plt.bar(x, y)
plt.title('Simple Bar Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis') 
plt.show() 
 
