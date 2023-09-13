import pickle

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import AdaBoostRegressor, GradientBoostingRegressor, RandomForestRegressor
from sklearn.feature_selection import f_regression

from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

from sklearn.model_selection import ( KFold, ParameterGrid,
                                     train_test_split)
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor

df = pd.read_csv('./CSVs/dataset_operativo.csv')
# Divido i dati in training e test set
X = df.drop('Price', axis=1)
y = df['Price']
features = ['Make','Model','Color','Body_Type','kilometers_run','No_of_Owners','Seating_Capacity','Fuel_Type,Fuel_Tank_Capacity(L)','CC_Displacement','Transmission','Transmission_Type','Torque(Nm)','consumption','Year_Category','sport_cars','drive_easy','travel','euro']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# Definisco il numero di folds 
k_folds = 10

# Creo il KFold object
kfold = KFold(n_splits=k_folds)

# Lista dei regressori
regressors = [
    ('KNN', KNeighborsRegressor(), {'n_neighbors': range(2, 11)}),
    ('Decision Tree', DecisionTreeRegressor(), {'max_depth': range(3, 21)}),
    ('Random Forest', RandomForestRegressor(), {'n_estimators': range(50, 301, 50), 'max_depth': range(5, 31, 5)}),
    ('Ada Boost Regressor', AdaBoostRegressor(estimator=DecisionTreeRegressor()), {'n_estimators': range(50, 301, 50), 'learning_rate': [0.01, 0.1, 1.0]}),
    ('Gradient Boosting Regressor', GradientBoostingRegressor(), {'n_estimators': range(50, 201, 50), 'learning_rate': [0.01, 0.1, 1.0]})
]

# Dizionario per memorizzare i modelli migliori
best_models = {}

with open("./Valutazioniconiperparametri/valutazione_k_fold_&_grid_search_2.txt", "w") as file:
    file.write("Valori medi ottenuti tramite kfold:\n\n")
    # K-fold cross-validation
    for regressor_name, regressor, param_grid in regressors:
        best_mse_score = float("inf")  # Miglior punteggio mse ottenuto
        best_params = None  # Migliori parametri trovati
        best_avg_mae_score= 0  # Migliori punteggi medi delle metriche
        best_avg_r2_score=0
        for params in ParameterGrid(param_grid):
            r2_scores = []
            mae_scores = []
            mse_scores = []

            for train_index, val_index in kfold.split(X_train):
                # Divido i dati in training e validation set per il fold
                X_train_fold, X_val_fold = X_train.iloc[train_index], X_train.iloc[val_index]
                y_train_fold, y_val_fold = y_train.iloc[train_index], y_train.iloc[val_index]

                # Creo il regressore con i parametri correnti
                clf = regressor.set_params(**params)
                clf.fit(X_train_fold, y_train_fold)

                # Ottengo le predizioni sul validation set
                y_pred = clf.predict(X_val_fold)

                # Calcolo le misure di valutazione
                r2_scores.append(r2_score(y_val_fold, y_pred))
                mae_scores.append(mean_absolute_error(y_val_fold, y_pred))
                mse_scores.append(mean_squared_error(y_val_fold, y_pred))

            # Calcolo i valori medi delle misure di valutazione per i parametri correnti
            avg_r2_score = sum(r2_scores) / len(r2_scores)
            avg_mae_score = sum(mae_scores) / len(mae_scores)
            avg_mse_score = sum(mse_scores) / len(mse_scores)

            # Stampo i valori medi delle misure di valutazione per i parametri correnti con la grid search
            file.write(str(regressor_name + "\n"))
            file.write("Parameters: {}\n".format(params))
            file.write("Average R2: {:.4f}, ".format(avg_r2_score))
            file.write("Average mae Score: {:.4f}, ".format(avg_mae_score))
            file.write("Average mse Score: {:.4f}.".format(avg_mse_score))
            file.write("\n")
            # Memorizzo il modello addestrato per i parametri correnti se ottengo un punteggio mse migliore
            if avg_mse_score < best_mse_score:
                best_mse_score = avg_mse_score
                best_params = params
                best_avg_mae_score=avg_mae_score
                best_avg_r2_score=avg_r2_score
        #calcolo l'importanza delle feature usando anova per knn e usando featureimportance pe gli altri
        if regressor_name != 'KNN':
            rg = regressor.set_params(**params)
            rg.fit(X[X.columns], df['Price'])
            importances = rg.feature_importances_
            feature_importance = pd.DataFrame({'feature': X.columns, 'importance': importances})
            feature_importance = feature_importance.sort_values('importance', ascending=False)
            print("Importanza delle feature per",rg,": ")
            for index, row in feature_importance.iterrows():
                print(row['feature'], ":", row['importance'])
            print()
        else:
            knn = regressor.set_params(**params)
            f, p_values = f_regression(df[X.columns], df['Price'])
            feature_importance = f / f.sum()
            # Ottiene gli indici delle feature ordinati per importanza
            sorted_indices = feature_importance.argsort()[::-1]
            # Stampa le feature importance in ordine decrescente con il nome della feature
            print("Importanza delle feature per knn:")
            for i in sorted_indices:
                print(f"{X.columns[i]}: {feature_importance[i]}")
            print()
        # Stampo i valori medi delle misure di valutazione per i parametri migliori con la grid search
        file.write(str(regressor_name + " best parameters: {}\n".format(best_params)))
        file.write("Average mae Score: {:.4f},".format(best_avg_mae_score))
        file.write(" Average  mse Score: {:.4f},".format(best_mse_score))
        file.write(" Average R2 Score: {:.4f}.\n".format(best_avg_r2_score))
        file.write("\n\n")
        # Addestramento del miglior modello con i parametri migliori
        clf = regressor.set_params(**best_params)
        clf.fit(X_train, y_train)
        best_models[regressor_name] = clf
#salvo i parametri migliori per ogni regressore in un file
for regressor_name, regressor in best_models.items():
    filename = f"best_model_{regressor_name}2.pkl"
    with open(filename, "wb") as file:
        pickle.dump(regressor, file)

with open("./Valutazioni/valutazione_test_set_2.txt", "w") as file:
    file.write("Valutazione dei modelli sul test set:\n\n") 
    # Valutazione dei migliori modelli sul test set
    for regressor_name, regressor in best_models.items():
        y_test_pred = regressor.predict(X_test)

        file.write(str(regressor_name) + "\n")
        file.write("R2: " + str(r2_score(y_test, y_test_pred)) + "\n")
        file.write("mse: " + str(mean_squared_error(y_test, y_test_pred))+"\n")
        file.write("mae: " + str(mean_absolute_error(y_test, y_test_pred))+"\n")
