import pandas as pd


file_path = 'bee_colonies.csv'

df = pd.read_csv("/content/save_the_bees.csv")

print("First few rows of the DataFrame:")
print(df.head())
