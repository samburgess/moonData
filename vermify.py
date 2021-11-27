import pandas as pd

fr = pd.read_json('data/2017_font.json')


'''

NOTE****

I am not sure this mapping is correct. Need to find out how the
app converts. Taken from https://www.99boulders.com/bouldering-grades

'''

gradeMap = {

    "6A":"v3",
    "6A+":"v3",
    "6B":"v4",
    "6B+":"v4",
    "6C":"v5",
    "6C+":"v5",
    "7A":"v6",
    "7A+":"v7",
    "7B":"v8",
    "7B+":"v9",
    "7C":"v9",
    "7C+":"v10",
    "8A":"v11",
    "8A+":"v12",
    "8B":"v13",
    "8B+":"v14",
    "8C":"v15",
    "8C+":"v16",
    "9A":"v17",


}

for i in range(len(fr)):
    fr.loc[i, 'Grade'] = gradeMap[fr.loc[i, 'Grade']]
    print(i)

print()
print()
print('done')


fr.to_json(r'data/2017_v.json')