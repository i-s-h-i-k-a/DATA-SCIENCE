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


bins = [0, 10, 20, 30]

bin_labels = ['Low', 'Medium', 'High']

df['varroa_mites_bin'] = pd.cut(df['varroa_mites'], bins=bins, labels=bin_labels, include_lowest=True)

print("\nDataFrame with Binning:")
print(df[['state', 'varroa_mites', 'varroa_mites_bin']])
