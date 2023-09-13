import csv
import os
import re
from pyswip import Prolog
from pyswip.easy import *
from datetime import datetime
import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

# eseguo il file .pl con pyswip
prolog = Prolog()

prolog.consult('car.pl'),
prolog.consult('regole.pl')

#ottengo gli id presenti nel file filename
def ottieni_ids(file_name):
    with open(file_name, 'r') as file:
        ids = np.array([line.strip() for line in file])
        vettore_di_interi = [int(val) for val in ids]
        return vettore_di_interi

#ottengo gli id e per ogni id il costo del bollo presenti nel file filename
def ottieni_ids_bollo(file_name):
    if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
        with open(file_name, 'r') as file:
          ids=[]
          taxs=[]
          for line in file:
              parts = line.strip().split(" ")
              if len(parts) == 2:
               ids.append(int(parts[0]))
               taxs.append(float(parts[1]))
          return ids,taxs
    else:
        return [],[]#restiutisco 0 e 0.0 se il file è vuoto
# carico il dataset CSV
df= pd.read_csv('./CSVs/datasetnormalizzato.csv')


# procedo inserendo la nuova conoscenza
# definisco la lista dei file cui accedere
file_names = ['./regole/sport_cars.pl','./regole/drive_easy.pl','./regole/travel.pl']

# ciclo per ciascun file/caratteristica
for file_name in file_names:
    # estraggo il nome della caratteristica dal percorso del file
    caratteristica = os.path.basename(file_name).split('.')[0]
    
    # aggiungo la colonna corrispondente al df con il nome della caratteristica
    df[caratteristica] = 0

    # ottieni gli ID che soddisfano la caratteristica dal file
    ids_caratteristica = ottieni_ids(file_name)
    # imposto 1 nelle colonne corrispondenti per gli ID della caratteristica
    for id_caratteristica in ids_caratteristica:
        # ottengo gli indici delle righe corrispondenti all'ID nella colonna 'ID' del df
        indici_righe = df.index[df['ID'] == id_caratteristica].tolist()
        # imposto 1 nelle colonne corrispondenti alla caratteristica per gli indici delle righe
        df.loc[indici_righe, caratteristica] = 1
        #creo la caratteristica euro inizializzandola a 0
df['euro']='0'
#definisco la lista dei file a cui accedere
filenames=['./regole/euro1.pl','./regole/euro2.pl','./regole/euro3.pl','./regole/euro4.pl','./regole/euro5.pl','./regole/euro6.pl']

for file_name in filenames:
    idscaratteristica = ottieni_ids(file_name)
    # imposto 1 nelle colonne corrispondenti per gli ID della caratteristica
    for idcaratteristica in idscaratteristica:
        # ottengo gli indici delle righe corrispondenti all'ID nella colonna 'ID' del df
        indici_righe = df.index[df['ID'] == idcaratteristica].tolist()
        df.loc[indici_righe, 'euro'] = os.path.basename(file_name).split('.')[0]


#prendo solo la parte intera di euro e la converto effettivamente in intero
df['euro'] = df['euro'].apply(lambda x: re.sub(r'\D', '', x))
df['euro'] = df['euro'].astype(int)

#definisco la lista dei file a cui accedere
filenames=['./regole/recent_years_car.pl','./regole/old_years_car.pl','./regole/new_years_car.pl']
df['Year_Category']=0#inizializzo a 0 lasciando 0 per le macchine meno recenti
for file_name in filenames:
    idscaratteristica = ottieni_ids(file_name)
    for idcaratteristica in idscaratteristica:
        # ottengo gli indici delle righe corrispondenti all'ID nella colonna 'ID' del df
        indici_righe = df.index[df['ID'] == idcaratteristica].tolist()
        #imposto 1 per le macchine recenti e 2 per le machcine nuove
        if 'recent' in file_name:
            df.loc[indici_righe, 'Year_Category'] = 1
        elif 'new' in file_name:
            df.loc[indici_righe, 'Year_Category'] = 2

#definisco la lista dei file a cui accedere
filenames=['./regole/low_fuel_consumption.pl','./regole/medium_fuel_consumption.pl','./regole/high_fuel_consumption.pl']
df['consumption']=0#inizializzo a 0 lasciando 0 per le macchine che consumano poco
for file_name in filenames:
    idscaratteristica = ottieni_ids(file_name)
    for idcaratteristica in idscaratteristica:
        # ottengo gli indici delle righe corrispondenti all'ID nella colonna 'ID' del df
        indici_righe = df.index[df['ID'] == idcaratteristica].tolist()
        #imposto 1 per le macchine a medi consumi
        if 'medium' in file_name:
            df.loc[indici_righe, 'consumption'] = 1
        #imposto 2 per le macchine ad alti consumi
        elif 'high' in file_name:
            df.loc[indici_righe, 'consumption'] = 2

# definisco la lista dei file a cui accedere
file_names = ['./regole/bollo_euro0.pl','./regole/bollo_euro1.pl','./regole/bollo_euro2.pl','./regole/bollo_euro3.pl','./regole/bollo_euro4.pl','./regole/bollo_euro5.pl','./regole/bollo_euro6.pl']
df['Car_Tax']=0.0#creo la colonna che ocnterrà il costo del bollo
for filename in file_names:
    #ottengo tutti gli indici e i bolli dai file
    ids_caratteristica,taxs=ottieni_ids_bollo(filename)
    for id_caratteristica,tax in zip(ids_caratteristica,taxs):
       if ids_caratteristica !=[] and taxs != []:#controllo se diverso da 0 per evitare di considerare file vuoti
        indici_righe = df.index[df['ID'] == idcaratteristica].tolist()#ottengo tutti gli indici delle righe del file
        df.loc[indici_righe, 'Car_Tax'] = tax#imposto il bollo
#cancello tutte le feaeture che sono state sostiuite dalla nuova conoscenza
df=df.drop('Make_Year',axis=1)
df=df.drop('Power(BHP)',axis=1)
df=df.drop('kilometer_at_liter',axis=1)
df=df.drop('ID',axis=1)

features_bool=df[['sport_cars','drive_easy','travel']]# le feature booleane non sono da normalizzare
features_to_normalize = df[['Make','Model','Color','Body_Type','kilometers_run','No_of_Owners','Seating_Capacity','Fuel_Type','Fuel_Tank_Capacity(L)','CC_Displacement','Transmission','Transmission_Type','Torque(Nm)','consumption','Year_Category','euro','Car_Tax','Price']]

# normalizzo tramite MinMaxScaler
column_names = features_to_normalize.columns

scaler = MinMaxScaler()
df_normalized = scaler.fit_transform(features_to_normalize)
#creo il dataframe contenente le feature normalizzate e le feature booleane e lo salvo
df_normalized = pd.DataFrame(df_normalized, columns=column_names)
df = pd.concat([df_normalized, features_bool], axis=1)
new_order=['Make','Model','Color','Body_Type','kilometers_run','No_of_Owners','Seating_Capacity','Fuel_Type','Fuel_Tank_Capacity(L)','CC_Displacement','Transmission','Transmission_Type','Torque(Nm)','consumption','Year_Category','sport_cars','drive_easy','travel','euro','Car_Tax','Price']
df=df[new_order]
df.to_csv('./CSVs/dataset_operativo.csv', index = False)
