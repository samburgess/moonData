import pandas as pd
import json


'''
Replace hold array with 2d matrix

'''


inData = 'data/2017_v.json'
outData = 'data/2017_v_mat.json'

df = pd.read_json(inData)


#1 indexed

mats = []

for i in range(len(df)):
    
    holds = df.loc[i, 'Moves']
    mat = []
    for hold in holds:
        row = ord(hold[0].lower()) - 96
        mat.append([row, int(hold[1:])])
    mats.append(mat)

df['Mat'] = mats

print()
print('**Done**')

df.to_json(outData)




