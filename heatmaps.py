import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import string

'''
Hold usage by grade
{
v3:[nxm], 
...
}
'''

inData = 'data/2016_v_mat.json'

grades = ['v3' ,'v4' ,'v5' ,'v6' ,'v7' ,'v8' ,'v9' ,'v10' ,'v11' ,'v12' ,'v13' ,'v14' ]

gradeMap = {}

for el in grades:
    gradeMap[el] = np.zeros((11, 18))

df = pd.read_json(inData)

n = len(df)

for i in range(n):
    el = df.loc[i, 'Mat']
    grade = df.loc[i, 'Grade']
    for el2 in el:
        gradeMap[grade][el2[0]-1][el2[1]-1] += 1

'''
#Pretty prints hold freq

for el in np.rot90(gradeMap['v10']):
    print(el)
    print()
'''

for el in gradeMap.keys():
    ax = sns.heatmap(np.rot90(gradeMap[el]),
                        linewidth=1,
                        yticklabels=range(18,0, -1),
                        xticklabels=list(string.ascii_uppercase)[:11], 
                        )
    plt.savefig('data/heatmaps/2016_'+el+'_heatmap')
    print(el)
    plt.clf()
