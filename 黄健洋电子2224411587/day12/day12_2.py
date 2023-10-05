import argparse
import pandas as pd
import random
import numpy as np
#input:  python3 day12/day12_2.py -number 2 --path example1.csv
parser = argparse.ArgumentParser(description='Demo of argparse')
parser.add_argument('--path', type=str)
parser.add_argument('-number', type=int)
args = parser.parse_args()
path=args.path
number=args.number

data = {}
for i in range(3):
    v=[]
    for j in range(100):
        v.append(random.randint(1,100))
    data[i]=v
df = pd.DataFrame(data)
df.to_csv(path, index=False)
df_read = pd.read_csv(path)
data={}
for i in range(3):
    data[i]=list(df_read[str(i)])
data.pop(number)
df = pd.DataFrame(data)
df.to_csv(path, index=False)