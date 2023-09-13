import pandas as pd
from sklearn.ensemble import AdaBoostRegressor, GradientBoostingRegressor, RandomForestRegressor
from sklearn.feature_selection import f_regression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
import numpy as np
from sklearn.model_selection import GridSearchCV, KFold
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
df=pd.read_csv('./CSVs/dataset_operativo.csv')

X = df.drop('Price', axis=1)
y = df['Price']

# Definisci una lista di possibili valori di fold
possible_folds = list(range(5, 11))

best_mse = float('inf')  # Inizializzo il miglior MSE con un valore molto grande
best_num_folds = None

#eseguo l'ottimizzazione del numero di fold, tramite un oggetto kfold con un numerio di fold preso dalla lista
for num_folds in possible_folds:
    kf = KFold(n_splits=num_folds, shuffle=True, random_state=0)
    mse_scores = []

    for train_index, val_index in kf.split(X):
        X_train, X_val = X.iloc[train_index], X.iloc[val_index]
        y_train, y_val = y.iloc[train_index], y.iloc[val_index]

        knn = KNeighborsRegressor()
        knn.fit(X_train, y_train)
        y_pred = knn.predict(X_val)
        mse = mean_squared_error(y_val, y_pred)
        mse_scores.append(mse)

    avg_mse = np.mean(mse_scores)
#aggiorno il numero di fold se il punteggio mse è migliore
    if avg_mse < best_mse:
        best_mse = avg_mse
        best_num_folds = num_folds

#da qui inizia la kfold per la valutazione dei regressori
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)
kfold = KFold(n_splits=best_num_folds)
#inizializzo le liste che conterranno i valori della valutazione per ogni fold
knnmse=[]
knnr2=[]
knnmae=[]
ada_r2=[]
adamse=[]
adamae=[]
gradientmse=[]
gradientr2=[]
gradientmae=[]
decisionr2=[]
decisionmae=[]
decisionmse=[]
randomforestmse=[]
randomforestr2=[]
randomforestmae=[]

#prendo una fold e calcolo i punteggi di valutazione per ogni regressore dopo averlo addestrato
for train_index, val_index in kfold.split(X_train):
    # divido i dati in training e validation set per fold
    X_train_fold, X_val_fold = X_train.iloc[train_index], X_train.iloc[val_index]
    y_train_fold,y_val_fold=y_train.iloc[train_index],y_train.iloc[val_index]
    knn = KNeighborsRegressor()
    knn.fit(X_train_fold, y_train_fold)
    y_pred_knn = knn.predict(X_val_fold)

    mse = mean_squared_error(y_val_fold, y_pred_knn)
    knnmse.append(mse)
    r2 = r2_score(y_val_fold, y_pred_knn)
    knnr2.append(r2)
    mae=mean_absolute_error(y_val_fold,y_pred_knn)
    knnmae.append(mae)

    randomforest=RandomForestRegressor(random_state=0)
    randomforest.fit(X_train, y_train)
    randomforestpred=randomforest.predict(X_val_fold)
    mse = mean_squared_error(y_val_fold, randomforestpred)
    randomforestmse.append(mse)
    r2 = r2_score(y_val_fold, randomforestpred)
    randomforestr2.append(r2)
    mae=mean_absolute_error(y_val_fold,randomforestpred)
    randomforestmae.append(mae)

    gb = GradientBoostingRegressor(random_state=0)
    gb.fit(X_train,y_train)
    gbpred=gb.predict(X_val_fold)
    mse = mean_squared_error(y_val_fold, gbpred)
    gradientmse.append(mse)
    r2 = r2_score(y_val_fold, gbpred)
    gradientr2.append(r2)
    mae=mean_absolute_error(y_val_fold,gbpred)
    gradientmae.append(mae)

    dct=DecisionTreeRegressor(random_state=0)
    dct.fit(X_train,y_train)
    dctpred=dct.predict(X_val_fold)
    mse = mean_squared_error(y_val_fold, dctpred)
    decisionmse.append(mse)
    r2 = r2_score(y_val_fold, dctpred)
    decisionr2.append(r2)
    mae=mean_absolute_error(y_val_fold,dctpred)
    decisionmae.append(mae)


    adaBoost_Regressor=AdaBoostRegressor(estimator=dct, n_estimators=50, random_state=0)
    adaBoost_Regressor.fit(X_train,y_train)
    adaboostpred=adaBoost_Regressor.predict(X_val_fold)
    mse = mean_squared_error(y_val_fold, adaboostpred)
    adamse.append(mse)
    adar2 = r2_score(y_val_fold, adaboostpred)
    ada_r2.append(adar2)
    mae=mean_absolute_error(y_val_fold,adaboostpred)
    adamae.append(mae)

#eseguo la media dei punteggi di valutazione(media dei punteggi ottenuti per ogni fold)
mean_knn_mse=sum(knnmse)/len(knnmse)
mean_knn_r2=sum(knnr2)/len(knnr2)
mean_knn_mae=sum(knnmae)/len(knnmae)

mean_dct_mse=sum(decisionmse)/len(decisionmse)
mean_dct_r2=sum(decisionr2)/len(decisionr2)
mean_dct_mae=sum(decisionmae)/len(decisionmae)

mean_randomforestmse=sum(randomforestmse)/len(randomforestmse)
mean_randomforestr2=sum(randomforestr2)/len(randomforestr2)
mean_randomforestmae=sum(randomforestmae)/len(randomforestmae)

mean_ada_mse=sum(adamse)/len(adamse)
mean_ada_r2=sum(ada_r2)/len(ada_r2)
mean_ada_mae=sum(adamae)/len(adamae)

mean_gdt_mse=sum(gradientmse)/len(gradientmse)
mean_gdt_r2=sum(gradientr2)/len(gradientr2)
mean_gdt_mae=sum(gradientmae)/len(gradientmae)

#salvo i punteggi in un file di testo per ogni regressore
with open("./ValutazioniKfold/KNN.txt", "w") as file:
    file.write("KNN: \n",)
    file.write(f"Average MSE Score: {mean_knn_mse},\n ")
    file.write(f"Average MAE Score: {mean_knn_mae},\n")
    file.write(f"Average R2 Score: {mean_knn_r2},\n")

with open("./ValutazioniKfold/randomforest.txt", "w") as file:
    file.write("RANDOM FOREST: \n")
    file.write(f"Average MSE Score: {mean_randomforestmse},\n ")
    file.write(f"Average MAE Score: {mean_randomforestmae},\n")
    file.write(f"Average R2 Score: {mean_randomforestr2},\n")

with open("./ValutazioniKfold/gradientBoostingRegressor.txt", "w") as file:
    file.write("Gradient Boosting Regressor: \n")
    file.write(f"Average MSE Score: {mean_gdt_mse},\n ")
    file.write(f"Average MAE Score: {mean_gdt_mae},\n")
    file.write(f"Average R2 Score: {mean_gdt_r2},\n")

with open("./ValutazioniKfold/decision.txt", "w") as file:
    file.write("DECISION TREE: \n")
    file.write(f"Average MSE Score: {mean_dct_mse},\n ")
    file.write(f"Average MAE Score: {mean_dct_mae},\n")
    file.write(f"Average R2 Score: {mean_dct_r2},\n")

with open("./ValutazioniKfold/ada.txt", "w") as file:
    file.write("ADA: \n")
    file.write(f"Average MSE Score: {mean_ada_mse},\n ")
    file.write(f"Average MAE Score: {mean_ada_mae},\n")
    file.write(f"Average R2 Score: {mean_ada_r2},\n")
