import pandas as pd
import random
import numpy as np
data = {}
for i in range(3):
    v=[]
    for j in range(100):
        v.append(random.randint(1,100))
    data[i]=v
df = pd.DataFrame(data)
df.to_csv('example.csv', index=False)
df_read = pd.read_csv('example.csv')
data={}
for i in range(3):
    data[i]=list(df_read[str(i)])
data[4]=np.array(data[0])+np.array(data[2])
data.pop(1)
df = pd.DataFrame(data)
df.to_csv('example.csv', index=False)