# https://www.kaggle.com/unsdsn/world-happiness?select=2016.csv
# Plik csv z roku 2016
# Porównanie średniego wyniku zadowolenia w regionach i jego składowych.
# Chciałem porównać w jakich regionach średnie składowe zadowolenia są największe.
# Z wyników zaskoczyło mnie to, że Australia i Nowa Zelandia są najbardziej zadowolonym regionem mimo tego,
# że w Europie Zachodniej są państwa z większym zadowoleniem.

import csv
from dataclasses import dataclass

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('2016.csv')
print(df)
regions = df.groupby(['Region']).mean()
regions = regions.drop(['Happiness Rank', 'Lower Confidence Interval',
                        'Upper Confidence Interval', 'Dystopia Residual'], axis=1)

colors = {regions.index[i]: 'C' + str(i) for i in range(len(regions.index))}

for col in regions.columns:
    regions = regions.sort_values(col, ascending=False)
    plot = sns.barplot(x=col, y=regions.index, data=regions, orient='h', palette=colors)
    plt.show()
