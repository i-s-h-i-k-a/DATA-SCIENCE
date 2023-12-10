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

row_index = 0
row_data = df.iloc[row_index]
print(f"\nRecord at index {row_index}:\n{row_data}")

sliced_rows = df.iloc[1:3]
print("\nSliced Rows:\n", sliced_rows)

condition = df['varroa_mites'] > 20
filtered_rows = df[condition]
print("\nFiltered Rows:\n", filtered_rows)

column_name = 'varroa_mites'
column_data = df[column_name]
print(f"\nVariable '{column_name}':\n{column_data}")

selected_columns = df[['state', 'varroa_mites']]
print("\nSelected Columns:\n", selected_columns)

numeric_columns = df.select_dtypes(include='number')
print("\nNumeric Columns:\n", numeric_columns)

