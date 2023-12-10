import pandas as pd
import statsmodels.api as sm

data = {
    'state': ['Alabama', 'Arizona', 'Arkansas', 'California', 'Colorado'],
    'varroa_mites': [10.0, 26.9, 17.6, 24.7, 14.6],
    'other_pests_and_parasites': [5.4, 20.5, 11.4, 7.2, 0.9],
    'diseases': [0.0, 0.1, 1.5, 3.0, 1.8],
    'target_variable': [15.2, 30.5, 20.1, 25.8, 18.4]
}
df = pd.DataFrame(data)

X = df[['varroa_mites', 'other_pests_and_parasites', 'diseases']]
y = df['target_variable']

X = sm.add_constant(X)

def stepwise_selection(X, y,
                       initial_list=[],
                       threshold_in=0.01,
                       threshold_out=0.05,
                       verbose=True):
    included = list(initial_list)
    while True:
        changed = False

        excluded = list(set(X.columns) - set(included))
        new_pval = pd.Series(index=excluded, dtype=float)
        for new_column in excluded:
            model = sm.OLS(y, sm.add_constant(pd.DataFrame(X[included + [new_column]]))).fit()
            new_pval[new_column] = model.pvalues[new_column]
        best_pval = new_pval.min()
        if best_pval < threshold_in:
            best_feature = new_pval.idxmin()
            included.append(best_feature)
            changed = True
            if verbose:
                print(f'Add  :30 with p-value best_pval:.6f')


        model = sm.OLS(y, sm.add_constant(pd.DataFrame(X[included]))).fit()

        pvalues = model.pvalues.iloc[1:]
        worst_pval = pvalues.max()
        if worst_pval > threshold_out:
            changed = True
            worst_feature = pvalues.idxmax()
            included.remove(worst_feature)
            if verbose:
                print(f'Drop :30 with p-value worst_pval:.6f')
        if not changed:
            break
    return included

selected_features = stepwise_selection(X, y)

print("Selected Features:", selected_features)

final_model = sm.OLS(y, sm.add_constant(X[selected_features])).fit()

print(final_model.summary())
