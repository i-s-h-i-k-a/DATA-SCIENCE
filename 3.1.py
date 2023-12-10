
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/content/save_the_bees.csv')


plt.figure(figsize=(12, 6))


bar_plot = plt.bar(df['state'], df['num_colonies'], color='blue', label='Number of Colonies')


plt.errorbar(df['state'], df['num_colonies'], yerr=(df['lost_colonies'], df['added_colonies']),
             fmt='none', color='red', capsize=5, label='Lost and Added Colonies')


plt.title('Bee Colonies with Overlay')
plt.xlabel('State')
plt.ylabel('Number of Colonies')


plt.legend()


plt.xticks(rotation=45, ha='right')


plt.tight_layout()
plt.show()
