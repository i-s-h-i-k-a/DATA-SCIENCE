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

output_file_path = 'modified_bee_colonies.csv'
df.to_csv(output_file_path, index=False)

print(f"\nDataFrame saved to: {output_file_path}")
