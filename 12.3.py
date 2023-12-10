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

threshold_varroa_mites = 15.0
threshold_other_pests = 10.0
threshold_diseases = 1.0

df['varroa_mites'] = pd.cut(df['varroa_mites'], bins=[-float('inf'), threshold_varroa_mites, float('inf')], labels=[0, 1])
df['other_pests_and_parasites'] = pd.cut(df['other_pests_and_parasites'], bins=[-float('inf'), threshold_other_pests, float('inf')], labels=[0, 1])
df['diseases'] = pd.cut(df['diseases'], bins=[-float('inf'), threshold_diseases, float('inf')], labels=[0, 1])

df_encoded = pd.get_dummies(df.drop(columns=['state']), columns=['bee_product', 'varroa_mites', 'other_pests_and_parasites', 'diseases'])

frequent_itemsets = apriori(df_encoded, min_support=0.2, use_colnames=True)

rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)

average_confidence = rules.groupby('antecedents')['confidence'].mean().reset_index()

rules = pd.merge(rules, average_confidence, on='antecedents', how='left', suffixes=('', '_average'))

confidence_quotient_threshold = 0.8
filtered_rules = rules[rules['confidence'] / rules['confidence_average'] > confidence_quotient_threshold]

print(filtered_rules)

