import pandas as pd
import json

inData = 'data/2016_v.json'

outData = 'data/2016_grade_dist.json'

df = pd.read_json(inData)

n = len(df)

dist = {"v3":0,"v4":0,"v5":0,"v6":0,"v7":0,"v8":0,"v9":0,"v10":0,"v11":0,"v12":0,"v13":0,"v14":0}


for i in range(n):
    
    dist[df.loc[i, 'Grade']] += 1

f = open(outData, 'a+')

json.dump(dist, f)
