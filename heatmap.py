from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
df=pd.read_csv('./CSVs/dataset_operativo.csv')
plt.figure(figsize = (24, 12))#creo la schermata per ospitare il grafico
corr = df.corr()#creo la matrice di correlazione  che riporta i punteggi di relazione tra ogni coppiadi variabili
sns.heatmap(corr, annot = True, linewidths = 1)#creo l'heatmap passandoli la matrice di correlazione, e mettendo annot=true per mostrare i valori di correlazione nelle celle e lineewidths per lo spessore delle linee
plt.show()

#creo il codice per mostrare la correlazione tra feature categoriche e feature target
categorical_features = df[['ID','Make','Model','Make_Year','Color','Body_Type','kilometers_run','No_of_Owners','Seating_Capacity','Fuel_Type','Fuel_Tank_Capacity(L)','CC_Displacement','Transmission','Transmission_Type','Power(BHP)','Torque(Nm)','kilometer_at_liter','consumption','Year_Category','sport_cars','drive_easy','travel','euro']]
categorical_features = categorical_features.copy()
categorical_features['Price'] = df.loc[:, 'Price']
plt.figure(figsize = (24, 12))
corr = categorical_features.corr()
sns.heatmap(corr, annot = True, linewidths = 1)
plt.show()
correlation = df.corr()['Price'].abs().sort_values(ascending = False)
with open("./Grafici/correlazione.txt", "w") as file:
    file.write(str(correlation))
