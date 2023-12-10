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


misleading_values = {'Alabama': 'AL', 'Arizona': 'AZ', 'Arkansas': 'AR'}
df['state'].replace(misleading_values, inplace=True)

print("\nDataFrame after Replacing Misleading Values:")
print(df)
