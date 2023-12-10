import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

data = {
    'state': ['Alabama', 'Arizona', 'Arkansas', 'California', 'Colorado'],
    'varroa_mites': [10.0, 26.9, 17.6, 24.7, 14.6],
    'other_pests_and_parasites': [5.4, 20.5, 11.4, 7.2, 0.9],
    'diseases': [0.0, 0.1, 1.5, 3.0, 1.8],
    'target_variable': [15.2, 30.5, 20.1, 25.8, 18.4]
}
df = pd.DataFrame(data)

X = df[['varroa_mites', 'other_pests_and_parasites', 'diseases']]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

pca = PCA()
X_pca = pca.fit_transform(X_scaled)

explained_var_ratio = pca.explained_variance_ratio_

plt.bar(range(1, len(explained_var_ratio) + 1), explained_var_ratio, alpha=0.5, align='center')
plt.step(range(1, len(explained_var_ratio) + 1), explained_var_ratio.cumsum(), where='mid')
plt.xlabel('Principal Components')
plt.ylabel('Explained Variance Ratio')
plt.title('Explained Variance Ratio by Principal Components')
plt.show()

principal_components = pd.DataFrame(pca.components_, columns=X.columns)
print("Principal Components:")
print(principal_components)
