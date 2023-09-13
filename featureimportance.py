import pickle
import pandas as pd

from sklearn.ensemble import AdaBoostRegressor, GradientBoostingRegressor, RandomForestRegressor
from sklearn.feature_selection import f_regression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor

#divido il dataset in due parti una variabili di input e l'altra variabile target
df=pd.read_csv('./CSVs/dataset_operativo.csv')
X=df.drop('Price',axis=1)
y=df['Price']

#addestro il regressore randomforest e calcolo l'importanza per ogni feature attraverso l'attributo feature_importances_ riportandole all'interno di un dataframe
randomforest=RandomForestRegressor()
randomforest.fit(X,y)
importances = randomforest.feature_importances_
feature_importance = pd.DataFrame({'feature': X.columns, 'importance': importances})
feature_importance = feature_importance.sort_values('importance', ascending=False)
print("Importanza delle feature per randomforest:")
for index, row in feature_importance.iterrows():
     print(row['feature'], ":", row['importance'])
print()

#addestro il regressore adaboost e calcolo l'importanza per ogni feature attraverso l'attributo feature_importances_riportandole all'interno di un dataframe
adaboost=AdaBoostRegressor()
adaboost.fit(X,y)
importances = adaboost.feature_importances_
feature_importance = pd.DataFrame({'feature': X.columns, 'importance': importances})
feature_importance = feature_importance.sort_values('importance', ascending=False)
print("Importanza delle feature per adaboost:")
for index, row in feature_importance.iterrows():
     print(row['feature'], ":", row['importance'])
print()

#addestro il regressore knn e calcolo il test anova per l'importanza delle feature riportandole all'interno di un dataframe
knn = KNeighborsRegressor()
f, p_values = f_regression(df[X.columns], df['Price'])
feature_importance = f / f.sum()

# Ottiene gli indici delle feature ordinati per importanza
sorted_indices = feature_importance.argsort()[::-1]

# Stampa le feature importance in ordine decrescente con il nome della feature
print("Importanza delle feature per knn:")
for i in sorted_indices:
    print(f"{X.columns[i]}: {feature_importance[i]}")
print()

#addestro il regressore decisiontree e calcolo l'importanza per ogni feature attraverso l'attributo feature_importances_ riportandole all'interno di un dataframe
decision=DecisionTreeRegressor()
decision.fit(X,y)
importances = decision.feature_importances_
feature_importance = pd.DataFrame({'feature': X.columns, 'importance': importances})
feature_importance = feature_importance.sort_values('importance', ascending=False)
print("Importanza delle feature per decisiontree:")
for index, row in feature_importance.iterrows():
     print(row['feature'], ":", row['importance'])
print()

#addestro il regressore GradientBoosting e calcolo l'importanza per ogni feature attraverso l'attributo feature_importances_ riportandole all'interno di un dataframe
gradient=GradientBoostingRegressor()
gradient.fit(X,y)
importances = gradient.feature_importances_
feature_importance = pd.DataFrame({'feature': X.columns, 'importance': importances})
feature_importance = feature_importance.sort_values('importance', ascending=False)
print("Importanza delle feature per gradientboosting:")
for index, row in feature_importance.iterrows():
     print(row['feature'], ":", row['importance'])
