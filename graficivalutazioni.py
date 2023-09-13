import pickle

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split

df = pd.read_csv('./CSVs/dataset_operativo.csv')

# Divido i dati in training e test set
X = df.drop('Price', axis=1)
y = df['Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# Carico i modelli salvati
model_filenames = [
    "best_model_KNN2.pkl",
    "best_model_Decision Tree2.pkl",
    "best_model_Random Forest2.pkl",
    "best_model_Ada Boost Regressor2.pkl",
    "best_model_Gradient Boosting Regressor2.pkl"
]
best_models = {}

for model_filename in model_filenames:
    with open(model_filename, "rb") as file:
        rg = pickle.load(file)
        regressor_name = model_filename.split("_")[2].split(".")[0]
        best_models[regressor_name] = rg

# Calcolo i punteggi R2, MAE e MSE sui dati di addestramento e di test
r2_scores_train = {}
r2_scores_test = {}
mae_scores_train = {}
mae_scores_test = {}
mse_scores_train = {}
mse_scores_test = {}


for regressor_name, regressor in best_models.items():
    y_train_pred = regressor.predict(X_train)
    y_test_pred = regressor.predict(X_test)

    train_r2 = r2_score(y_train, y_train_pred)
    test_r2 = r2_score(y_test, y_test_pred)

    train_mse = mean_squared_error(y_train, y_train_pred)
    test_mse = mean_squared_error(y_test, y_test_pred)

    train_mae = mean_absolute_error(y_train, y_train_pred)
    test_mae = mean_absolute_error(y_test, y_test_pred)


    r2_scores_train[regressor_name] = train_r2
    r2_scores_test[regressor_name] = test_r2

    mae_scores_train[regressor_name] = train_mae
    mae_scores_test[regressor_name] = test_mae

    mse_scores_train[regressor_name] = train_mse
    mse_scores_test[regressor_name] = test_mse



# Creo il grafico per i punteggi R2 dei migliori modelli
plt.figure(figsize=(10, 6))
plt.bar(range(len(r2_scores_test)), list(r2_scores_test.values()), align='center')
plt.xticks(range(len(r2_scores_test)), list(r2_scores_test.keys()), rotation=45)
plt.xlabel('Model')
plt.ylabel('r2 Score')
plt.title('r2 Score Comparison for Best Models')
plt.tight_layout()

for i, value in enumerate(r2_scores_test.values()):
    plt.text(i, value + 0.01, f'{value:.4f}', color='black', ha='center')

plt.show()

# Creo il grafico per i punteggi R2 dei migliori modelli su train e test
plt.figure(figsize=(12, 6))
bar_width = 0.35
index = np.arange(len(r2_scores_train))

plt.bar(index, list(r2_scores_train.values()), bar_width, label='Train r2 Score')
plt.bar(index + bar_width, list(r2_scores_test.values()), bar_width, label='Test r2 Score')

plt.xticks(index + bar_width / 2, list(r2_scores_train.keys()), rotation=45)
plt.xlabel('Model')
plt.ylabel('r2 Score')
plt.title('r2 Score Comparison for Best Models (Train vs Test)')
plt.legend(loc='upper left', bbox_to_anchor=(1.0, 1.0))
plt.tight_layout()

# Aggiungo le etichette per mae sopra le barre
for i, value in enumerate(r2_scores_train.values()):
    plt.text(i, value + 0.005, f'{value:.4f}', color='black', ha='center')
for i, value in enumerate(r2_scores_test.values()):
    plt.text(i + bar_width, value + 0.005, f'{value:.4f}', color='black', ha='center')

plt.show()

# Creo il grafico per MSE di test e training per ogni modello
plt.figure(figsize=(12, 6))
index = np.arange(len(mse_scores_train))
bar_width = 0.35

plt.bar(index, list(mse_scores_train.values()), bar_width, label='Train MSE')
plt.bar(index + bar_width, list(mse_scores_test.values()), bar_width, label='Test MSE')

plt.xticks(index + bar_width / 2, list(mse_scores_train.keys()), rotation=45)
plt.xlabel('Model')
plt.ylabel('MSE')
plt.title('MSE Comparison for Best Models (Train vs Test)')
plt.legend(loc='upper left', bbox_to_anchor=(1.0, 1.0))
plt.tight_layout()

# Aggiungo le etichette per MSE sopra le barre
for i, value in enumerate(mse_scores_train.values()):
    plt.text(i, value + 0.005, f'{value:.4f}', color='black', ha='center')
for i, value in enumerate(mse_scores_test.values()):
    plt.text(i + bar_width, value + 0.005, f'{value:.4f}', color='black', ha='center')

plt.show()




# Creo il grafico per la mae di test e training per ogni modello
plt.figure(figsize=(12, 6))
index = np.arange(len(mae_scores_train))
bar_width = 0.35

plt.bar(index, list(mae_scores_train.values()), bar_width, label='Train MAE')
plt.bar(index + bar_width, list(mae_scores_test.values()), bar_width, label='Test MAE')

plt.xticks(index + bar_width / 2, list(mae_scores_train.keys()), rotation=45)
plt.xlabel('Model')
plt.ylabel('MAE')
plt.title('MAE Comparison for Best Models (Train vs Test)')
plt.legend(loc='upper left', bbox_to_anchor=(1.0, 1.0))
plt.tight_layout()

# Aggiungo le etichette per MAE sopra le barre
for i, value in enumerate(mae_scores_train.values()):
    plt.text(i - 0.12, value + 0.005, f'{value:.4f}', color='black')
for i, value in enumerate(mae_scores_test.values()):
    plt.text(i + bar_width - 0.12, value + 0.005, f'{value:.4f}', color='black')

plt.show()
