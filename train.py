import pandas as pd
import numpy as np
import csv

# Load Training data
df = pd.read_csv('data/clean/Training.csv')

df.head()

X = df.iloc[:, :-1]
y = df['prognosis']

# Train, Test split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=20)

# Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier

rf_clf = RandomForestClassifier()

rf_clf.fit(X_train, y_train)

print("Accuracy on split test: ", rf_clf.score(X_test,y_test))

# Load real test data
df_test = pd.read_csv('data/clean/Testing.csv')

X_actual_test = df_test.iloc[:, :-1]
y_actual_test = df_test['prognosis']

print("Accuracy on actual test: ", rf_clf.score(X_actual_test, y_actual_test))

import pickle
filename = 'model.sav'
pickle.dump(rf_clf, open(filename, 'wb'))