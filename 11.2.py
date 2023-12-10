import pandas as pd
import statsmodels.api as sm

data = {
    'state': ['Alabama', 'Arizona', 'Arkansas', 'California', 'Colorado'],
    'varroa_mites': [10.0, 26.9, 17.6, 24.7, 14.6],
    'other_pests_and_parasites': [5.4, 20.5, 11.4, 7.2, 0.9],
    'diseases': [0.0, 0.1, 1.5, 3.0, 1.8],
    'target_variable': [100, 150, 80, 120, 90]
}
df = pd.DataFrame(data)

X = df[['varroa_mites', 'other_pests_and_parasites', 'diseases']]
y = df['target_variable']

X = sm.add_constant(X)

poisson_model = sm.GLM(y, X, family=sm.families.Poisson()).fit()

print(poisson_model.summary())
