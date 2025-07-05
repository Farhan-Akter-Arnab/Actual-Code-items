import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('USA_Housing.csv')
df.head(10)
df.info()
df.describe()
df.columns
sns.pairplot(df)