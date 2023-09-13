import pandas as pd
from sklearn.ensemble import AdaBoostRegressor, GradientBoostingRegressor, RandomForestRegressor
from sklearn.feature_selection import f_regression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
import numpy as np
import statsmodels.api as sm
from statsmodels.formula.api import ols
df=pd.read_csv('./CSVs/dataset_operativo.csv')

#divido il dataset in features e target
X = df.drop('Price', axis=1)
y = df['Price']

#creo i set di addestramento e valutazione
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.50, random_state = 42)

#creo e addestro il KNN riportando i punteggi di valutazione sul set di test
knn = KNeighborsRegressor()
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)
mse = mean_squared_error(y_test, y_pred_knn)
mae=mean_absolute_error(y_test, y_pred_knn)
r2=r2_score(y_test, y_pred_knn )

# Calcolo la feature importance utilizzando ANOVA
print('importanza delle features per knn')
f, p_values = f_regression(X, y)
feature_importance = f / f.sum()

# Ottiene gli indici delle feature ordinati per importanza
sorted_indices = feature_importance.argsort()[::-1]

# Stampa le feature importance in ordine decrescente con il nome della feature

for i in sorted_indices:
    print(f"{df.columns[i]}: {feature_importance[i]}")

#scrivo i punteggi di un valutazione in un file txt    
with open("./Valutazioni/KNN.txt", "w") as file:
    file.write("KNN: \n",)
    file.write(f"Average MSE Score: {mse},\n ")
    file.write(f"Average MAE Score: {mae},\n")
    file.write(f"Average R^2 Score: {r2},\n")

#creo e addestro il decisiontree riportando i punteggi di valutazione sul set di test
dtc = DecisionTreeRegressor()
dtc.fit(X_train, y_train)
y_pred_dtc = dtc.predict(X_test)

mse = mean_squared_error(y_test, y_pred_dtc )
r2=r2_score(y_test, y_pred_dtc )
mae=mean_absolute_error(y_test,y_pred_dtc)

#mostro la feauture importance per dct tramite l'attributo feature_importance
importances = dtc.feature_importances_
feature_importance = pd.DataFrame({'feature': X.columns, 'importance': importances})
feature_importance = feature_importance.sort_values('importance', ascending=False)
print("Importanza delle feature per decisiontree:")
for index, row in feature_importance.iterrows():
    print(row['feature'], ":", row['importance'])

#salvo i punteggi di valutazione in un file txt
with open("./Valutazioni/decisiontree.txt", "w") as file:
    file.write("DECISION TREE: \n",)
    file.write(f"Average MSE Score: {mse},\n ")
    file.write(f"Average MAE Score: {mae},\n")
    file.write(f"Average R^2 Score: {r2},\n")

#creo e addestro il randomforest riportando i punteggi di valutazione sul set di test
rd_clf = RandomForestRegressor()
rd_clf.fit(X_train, y_train)
y_pred_rd_clf = rd_clf.predict(X_test)
mse = mean_squared_error(y_test, y_pred_rd_clf)
r2=r2_score(y_test, y_pred_rd_clf )
mae=mean_absolute_error(y_test,y_pred_rd_clf)

#mostro la feauture importance per randomforest tramite l'attributo feature_importance
importances = rd_clf.feature_importances_
feature_importance = pd.DataFrame({'feature': X.columns, 'importance': importances})
feature_importance = feature_importance.sort_values('importance', ascending=False)
print("Importanza delle feature per random forest:")
for index, row in feature_importance.iterrows():
    print(row['feature'], ":", row['importance'])

#salvo i punteggi di valutazione in un file txt
with open("./Valutazioni/randomforest.txt", "w") as file:
    file.write("RANDOM FOREST: \n",)
    file.write(f"Average MSE Score: {mse},\n ")
    file.write(f"Average MAE Score: {mae},\n")
    file.write(f"Average R^2 Score: {r2},\n")

#creo e addestro l'adaboost riportando i punteggi di valutazione sul set di test
ada = AdaBoostRegressor(estimator = dtc)
ada.fit(X_train, y_train)
y_pred_ada = ada.predict(X_test)
mse = mean_squared_error(y_test, y_pred_ada)
r2=r2_score(y_test, y_pred_rd_clf )
mae = mean_absolute_error(y_test, y_pred_ada)

#mostro la feauture importance per ada tramite l'attributo feature_importance
importances = ada.feature_importances_
feature_importance = pd.DataFrame({'feature': X.columns, 'importance': importances})
feature_importance = feature_importance.sort_values('importance', ascending=False)
print("Importanza delle feature per ada:")
for index, row in feature_importance.iterrows():
    print(row['feature'], ":", row['importance'])
with open("./Valutazioni/adaboost.txt", "w") as file:
    file.write("ADABOOST: \n",)
    file.write(f"Average MSE Score: {mse},\n ")
    file.write(f"Average MAE Score: {mae},\n")
    file.write(f"Average R^2 Score: {r2},\n")

#creo e addestro il gradientboosting riportando i punteggi di valutazione sul set di test
gb = GradientBoostingRegressor()
gb.fit(X_train, y_train)
y_pred_gb = gb.predict(X_test)
mse = mean_squared_error(y_test, y_pred_gb)
r2=r2_score(y_test, y_pred_gb )
mae=mean_absolute_error(y_test, y_pred_gb)

#mostro la feauture importance per gradientboostig tramite l'attributo feature_importance
importances = gb.feature_importances_
feature_importance = pd.DataFrame({'feature': X.columns, 'importance': importances})
feature_importance = feature_importance.sort_values('importance', ascending=False)
print("Importanza delle feature per gradient boosting:")
for index, row in feature_importance.iterrows():
    print(row['feature'], ":", row['importance'])
with open("./Valutazioni/gradientboosting.txt", "w") as file:
    file.write("GRADIENT BOOSTING: \n",)
    file.write(f"Average MSE Score: {mse},\n ")
    file.write(f"Average MAE Score: {mae},\n")
    file.write(f"Average R^2 Score: {r2},\n")

# Effettuiamo e stampiamo a video la predizione effettuata del prezzo della macchina
def predizione(esempio):
    df=pd.read_csv('./CSVs/dataset_operativo.csv')
    X_train=df.drop('Price',axis=1)
    Y_train=df['Price']
    regressor=DecisionTreeRegressor(max_depth=7)
    regressor.fit(X_train,Y_train)
    return regressor.predict(esempio)