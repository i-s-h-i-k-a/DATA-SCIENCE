import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

data = {
    'state': ['Alabama', 'Arizona', 'Arkansas', 'California', 'Colorado'],
    'varroa_mites': [10.0, 26.9, 17.6, 24.7, 14.6],
    'other_pests_and_parasites': [5.4, 20.5, 11.4, 7.2, 0.9],
    'diseases': [0.0, 0.1, 1.5, 3.0, 1.8],
    'bee_product': ['Honey', 'Honey', 'Wax', 'Honey', 'Wax']
}
df = pd.DataFrame(data)

df_encoded = pd.get_dummies(df.drop(columns=['state']), columns=['bee_product'])

df_encoded = df_encoded.astype(bool)

frequent_itemsets = apriori(df_encoded, min_support=0.2, use_colnames=True)

rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)

print(rules)

