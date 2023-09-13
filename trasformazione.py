import pandas as pd
import numpy as np

# Definiamo qual e la corrispondenza numerica per i valori della feature make e riportiamo make + corrispondente valore numerico nel file di testo corrispondenza
def Make(Make):
        with open('corrispondenza.txt', 'r') as file:
    # Legge e stampa il contenuto del file linea per linea
         for line in file:
                s=line.strip()
                s=s.split()
                if s[0]==Make:
                      return int(s[1])

# Definiamo qual e la corrispondenza numerica per i valori della feature model e riportiamo model + corrispondente valore numerico nel file di testo corrispondenza
def Model(Model):
        with open('corrispondenza.txt', 'r') as file:
    # Legge e stampa il contenuto del file linea per linea
         for line in file:
                s=line.strip()
                s=s.split()
                if s[2]==Model:
                      return int(s[3])

# Restituisce i modelli associati alla specifica marca
def ricerca(Make):
    df=pd.read_csv('./CSVs/datasetfiltrato.csv')
    modelli_associati = df[df['Make'] == Make]['Model'].tolist()
    return np.unique(modelli_associati)

# Assegno ad ogni possibile valore delle varie feature un valore numerico, leggendo i vari valori da datasetfiltrato
df=pd.read_csv('./CSVs/datasetfiltrato.csv')

mapping = {'beige': '1', 'black': '2', 'blue': '3', 'bronze': '4', 'brown': '5', 'golden': '6', 'grey': '7', 'maroon': '8', 'orange': '9', 'purple': '10', 'red': '11', 'silver': '12', 'white':'13', 'yellow': '14', 'green': '15' }
df['Color'] = df['Color'].map(mapping)

mapping={'sedan': '1', 'suv': '2', 'muv': '3', 'hatchback': '4', 'crossover': '5'}
df['Body_Type']=df['Body_Type'].map(mapping)

mapping={'diesel':'1', 'petrol': '2', 'petrol+cng': '3'}
df['Fuel_Type']=df['Fuel_Type'].map(mapping)

mapping={'4-Speed':'4', '5-Speed': '5', '6-Speed': '6', '7-Speed': '7', 'CVT': '1'}
df['Transmission']=df['Transmission'].map(mapping)

mapping={'Manual':'1', 'Automatic': '2'}
df['Transmission_Type']=df['Transmission_Type'].map(mapping)

cont=0
cont1=0
unique_make = {}
unique_model = {}

# Assegnano un identificativo alle macchine e lo salviamo nel file corrispondenza.txt
with open('corrispondenza.txt', 'w') as file:
        for company in np.unique(df['Make']):
                unique_make[company] = cont
                models=ricerca(company)
                for model in models:
                       unique_model[model]=cont1
                       file.write(company+' '+str(cont)+' '+model+' '+str(cont1)+'\n')
                       cont1+=1
                cont+= 1
# Applico le espressione lambda per convertire i valori di make e model in interi, prendendo i valori da unique model e uniquemake, cosi da avere un identificativo unico per ogni marca< e per gni modello
df['Make'] = df.apply(lambda row: unique_make[row['Make']], axis=1)
df['Model'] = df.apply(lambda row: unique_model[row['Model']], axis=1)
df.to_csv('./CSVs/datasetnormalizzato.csv', index=False)

