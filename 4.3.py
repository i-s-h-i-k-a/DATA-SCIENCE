import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt


features = df.drop(['state', 'quarter', 'year'], axis=1)
target = df['year']

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)


tree_model = DecisionTreeClassifier(random_state=42)
tree_model.fit(X_train, y_train)

plt.figure(figsize=(20, 10))
plot_tree(tree_model, feature_names=features.columns, class_names=list(map(str, tree_model.classes_)), filled=True, rounded=True)
plt.show()

