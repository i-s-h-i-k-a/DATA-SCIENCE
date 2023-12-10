
import pandas as pd
import matplotlib.pyplot as plt


data = {
    'state': ['Alabama', 'Arizona', 'Arkansas', 'California', 'Colorado'],
    'varroa_mites': [10.0, 26.9, 17.6, 24.7, 14.6],
    'other_pests_and_parasites': [5.4, 20.5, 11.4, 7.2, 0.9],
    'diseases': [0.0, 0.1, 1.5, 3.0, 1.8]
}
df = pd.DataFrame(data)

print("Dataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

plt.hist(df['varroa_mites'], bins=20, color='blue', edgecolor='black')
plt.xlabel('Varroa Mites (%)')
plt.ylabel('Frequency')
plt.title('Histogram of Varroa Mites Percentage')
plt.show()
