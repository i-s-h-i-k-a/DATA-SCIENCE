import pandas as pd

file_path = 'bee_colonies.csv'

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv("/content/save_the_bees.csv")

# Display the first few rows of the DataFrame to verify the import
print("First few rows of the DataFrame:")
print(df.head())

# Re-express the 'state' column by mapping old values to new values
state_mapping = {'Alabama': 'AL', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO'}
df['state'] = df['state'].map(state_mapping)

# Display the DataFrame after re-expressing 'state' values
print("\nDataFrame after Re-expressing 'state' values:")
print(df)


