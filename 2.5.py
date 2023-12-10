import pandas as pd
import matplotlib.pyplot as plt

data = {
    'state': ['Alabama', 'Arizona', 'Arkansas', 'California', 'Colorado'],
    'varroa_mites': [10.0, 26.9, 17.6, 24.7, 14.6]
}
df = pd.DataFrame(data)

plt.boxplot(df['varroa_mites'])
plt.title('Boxplot of Varroa Mites Percentage')
plt.show()

Q1 = df['varroa_mites'].quantile(0.25)
Q3 = df['varroa_mites'].quantile(0.75)
IQR = Q3 - Q1


lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR


outliers = df[(df['varroa_mites'] < lower_bound) | (df['varroa_mites'] > upper_bound)]


print("Identified Outliers:")
print(outliers)


