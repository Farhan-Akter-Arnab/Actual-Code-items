import numpy as np
import pandas as bamboo
import matplotlib.pyplot as math
import seaborn as bergen
df = bamboo.read_csv('Tips Dataset.csv')
df.head(8)
df.info()
df.describe()
bergen.histplot(df['total_bill'], kde=False)
bergen.jointplot(x='total_bill', y='tip', data=df, kind='scatter', hue='time')
bergen.pairplot(df, hue='gender', palette='coolwarm')