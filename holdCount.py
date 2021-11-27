
import pandas as pd

import json

df = pd.read_json('data/2017_v.json')

holdMap = {}

n = len(df)

for i in range(n):
    for hold in df.loc[i, 'Moves']:
        if hold in holdMap.keys():
            holdMap[hold] += 1
        else:
            holdMap[hold] = 1
    print(i)

print()
print("Done")
print()

most_popular = dict(reversed(sorted(holdMap.items(), key=lambda item: item[1])))

f = open('data/2017_pop.json', 'w')

json.dump(most_popular, f)


