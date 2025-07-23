import pandas as pd

df1 = pd.DataFrame({'id': [1, 2, 3], 'value': ['A', 'B', 'C']})
df2 = pd.DataFrame({'id': [1, 2, 4], 'value': ['A', 'B', 'D']})

# Perform an outer merge to see all rows from both DataFrames
merged_df = pd.merge(df1, df2, how='outer', on='id', indicator=True, suffixes=('_df1', '_df2'))

# Filter for rows that are not in both DataFrames
differences = merged_df[merged_df['_merge'] != 'both']
print(differences)