import pandas as pd
import matplotlib.pyplot as plt

data = {
    'state': ['Alabama', 'Arizona', 'Arkansas', 'California', 'Colorado'],
    'varroa_mites': [10.0, 26.9, 17.6, 24.7, 14.6]
}
df = pd.DataFrame(data)


plt.hist(df['varroa_mites'], bins=10, alpha=0.5, color='blue', label='Varroa Mites')


plt.xlabel('Varroa Mites (%)')
plt.ylabel('Frequency')
plt.title('Histogram of Varroa Mites Percentage in Different States')

plt.legend()


plt.show()
