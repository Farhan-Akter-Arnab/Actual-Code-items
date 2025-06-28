import pandas as pd
import numpy as np
employee_data = {
    'name': ['Pythagoras', 'Mehmed', 'Dawud', 'Lanthanum'],
    'role': ['CEO', np.nan, np.nan, np.nan],
    'salary': [18800, 24000, np.nan, np.nan]
}
labels = ['A', 'B', 'C', 'D']
employee_df = pd.DataFrame(employee_data, index=labels)
print(employee_df.loc[['A', 'B'], ['name', 'role', 'salary']])
print(employee_df.loc[['C', 'D'], ['name', 'role', 'salary']])
print("Total number of empty sets: ", employee_df.isna().sum().sum())
print(employee_df.info())
print(employee_df.isna().sum())
df_rowdrop = employee_df.dropna(axis=0)
print(df_rowdrop)
df_coldrop = employee_df.dropna(axis=1)
print(df_coldrop)
employee_df.fillna(value={'salary': 30000}, inplace=True)
print(employee_df)
employee_df.fillna(value={'role': 'CEO'}, inplace=True)
print(employee_df)
print("\nNew employee DataFrame info: \n")
print(employee_df.info())