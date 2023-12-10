import pandas as pd
from sklearn.preprocessing import StandardScaler

data = {
    'state': ['Alabama', 'Arizona', 'Arkansas', 'California', 'Colorado'],
    'varroa_mites': [10.0, 26.9, 17.6, 24.7, 14.6],
    'other_pests_and_parasites': [5.4, 20.5, 11.4, 7.2, 0.9],
    'diseases': [0.0, 0.1, 1.5, 3.0, 1.8]
}
df = pd.DataFrame(data)
numeric_fields = df.select_dtypes(include='number').columns


scaler = StandardScaler()
df[numeric_fields] = scaler.fit_transform(df[numeric_fields])
print("DataFrame after Standardization:")
print(df)

