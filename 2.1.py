import pandas as pd

data = {
    'state': ['Alabama', 'Arizona', 'Arkansas', 'California', 'Colorado'],
    'varroa_mites': [10.0, 26.9, 17.6, 24.7, 14.6],
    'other_pests_and_parasites': [5.4, 20.5, 11.4, 7.2, 0.9],
    'diseases': [0.0, 0.1, 1.5, 3.0, 1.8]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

df_reset_index = df.reset_index()
print("\nDataFrame with Reset Index:")
print(df_reset_index)
df['new_index'] = range(1, len(df) + 1)
print("\nDataFrame with New Index:")
print(df)

