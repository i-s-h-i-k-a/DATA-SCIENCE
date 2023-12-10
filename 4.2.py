import pandas as pd
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import RandomOverSampler

data = {
    'state': ['Alabama', 'Arizona', 'Arkansas', 'California', 'Colorado'],
    'varroa_mites': [10.0, 26.9, 17.6, 24.7, 14.6],
    'other_pests_and_parasites': [5.4, 20.5, 11.4, 7.2, 0.9],
    'diseases': [0.0, 0.1, 1.5, 3.0, 1.8],
    'target_class': [0, 1, 0, 1, 1]
}
df = pd.DataFrame(data)

X = df[['other_pests_and_parasites', 'diseases']]
y = df['target_class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Class distribution before balancing:")
print(y_train.value_counts())

oversampler = RandomOverSampler(random_state=42)
X_train_resampled, y_train_resampled = oversampler.fit_resample(X_train, y_train)

print("\nClass distribution after balancing:")
print(pd.Series(y_train_resampled).value_counts())
