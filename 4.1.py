import pandas as pd
from sklearn.model_selection import train_test_split

data = {
    'state': ['Alabama', 'Arizona', 'Arkansas', 'California', 'Colorado'],
    'varroa_mites': [10.0, 26.9, 17.6, 24.7, 14.6],
    'other_pests_and_parasites': [5.4, 20.5, 11.4, 7.2, 0.9],
    'diseases': [0.0, 0.1, 1.5, 3.0, 1.8]
}
df = pd.DataFrame(data)


X = df[['other_pests_and_parasites', 'diseases']]
y = df['varroa_mites']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training Features:")
print(X_train)
print("\nTesting Features:")
print(X_test)
print("\nTraining Target:")
print(y_train)
print("\nTesting Target:")
print(y_test)
