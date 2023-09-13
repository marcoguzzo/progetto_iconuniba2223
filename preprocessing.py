import re
import pandas as pd

df=pd.read_csv('./CSVs/FINAL_SPINNY_900.csv')
#tolgo carname perchè contenente informazioni poco rilevanti
df = df.drop('Car_Name', axis=1)
#sostiuisco le miglia percorse con i kilometri
df['Mileage_Run'] = df['Mileage_Run'].apply(lambda x: re.sub(r'\D', '', x))
df['Mileage_Run'] = df['Mileage_Run'].astype(float)
df = df.rename(columns={'Mileage_Run': 'kilometers_run'})


#converto il prezzo in float e trasfiormo in euro perchè in ruple
df['Price'] = df['Price'].apply(lambda x: re.sub(r'\D', '', x)).astype(int)
df['Price'] = df['Price'] / 90
df['Price'] = df['Price'].astype(float)
df=df.drop('Engine_Type',axis=1)#cancello engine type poichè contiene informazioni irrilevanti o ridondanti
df=df.drop('Emission',axis=1)
df['No_of_Owners'] = df['No_of_Owners'].apply(lambda x: re.sub(r'\D', '', x)).astype(int)



righe_da_eliminare = df.loc[(df['Mileage(kmpl)'] == '105 bhp @ 4400 RPM')|(df['Mileage(kmpl)'] == 'BS IV')]

# Elimina le righe selezionate
df = df.drop(righe_da_eliminare.index)
#converto le miglia al litro in km al litro e cambio il nome della colonna in kilometers at liter
df['Mileage(kmpl)'] = df['Mileage(kmpl)'].astype(float)
df = df.rename(columns={'Mileage(kmpl)': 'kilometer_at_liter'})
df=df.dropna()
#creo la colonna id per identificare univocamente le macchine
df['ID'] = range(len(df))
#ruimuovo gli spazi vuoti
df['Make']=df['Make'].str.replace(" ","")
df['Model']=df['Model'].str.replace(" ","")

#metto id in prima posizione
new_order=['ID','Make','Model','Make_Year','Color','Body_Type','kilometers_run','No_of_Owners','Seating_Capacity','Fuel_Type','Fuel_Tank_Capacity(L)','CC_Displacement','Transmission','Transmission_Type','Power(BHP)','Torque(Nm)','kilometer_at_liter','Price']
df=df[new_order]
#elimino i valori nulli e salvo
df=df.dropna()
df.to_csv('./CSVs/datasetfiltrato.csv', index=False)
