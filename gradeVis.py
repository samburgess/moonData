import pandas as pd
import json
import matplotlib.pyplot as plt


inData = 'data/2017_grade_dist.json'

with open(inData) as f:
    data = json.load(f)

    plt.bar(data.keys(), data.values())

    plt.xlabel('Hueco Grade*')
    plt.ylabel('Number of problems')
    plt.title('2017 Set Grade Distribution')

    plt.show()