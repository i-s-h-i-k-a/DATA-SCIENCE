import pandas as pd


data = {
    'state': ['Alabama', 'Arizona', 'Arkansas', 'California', 'Colorado'],
    'quarter': [1, 1, 1, 1, 1],
    'year': [2015, 2015, 2015, 2015, 2015]
}
df = pd.DataFrame(data)

contingency_table = pd.crosstab(df['quarter'], df['year'])

print("Contingency Table:")
print(contingency_table)

