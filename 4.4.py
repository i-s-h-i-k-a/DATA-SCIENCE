import pandas as pd
from c50 import C5_0

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

model = C5_0()
model.fit(X, y)


print("Decision Tree Rules:")
print(model.tree_.to_rules())
