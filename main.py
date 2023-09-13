import numpy as np
import pandas as pd
from CSP import getsolution
from trasformazione import ricerca
from trasformazione import Make
from trasformazione import Model
from regressore import predizione

print("Cosa vuoi fare? Se vuoi predire il prezzo di una macchina inserita da te premi 0")
print("Se vuoi trovare macchine che rispettano le caratteristiche da te introdotte premi 1")
scelta=int(input())
while(scelta != 0 and scelta != 1):
    scelta=int(input('inserire una scelta valida'))
list=[]#questa contiene le colonne di interesse
list1=[]#questa contiene i valori di interesse
if scelta==1:
    valori={}
    carburante=0
    print("Seleziona le caratteristiche della macchina di cui hai bisogno tra queste: ")
    macchina=int(input("Che macchina vuoi? utilitaria(0) o sportiva(1)? Inserire il numero corrispondente: \n"))
    while(macchina != 0 and macchina != 1):
        macchina=int(input('inserire la tipologia corretta'))
    if(macchina == 1):
        valori['sport_cars']=1
    else:
        valori['sport_cars']=0
        
    carburante=int(input("Cosa preferisci come tipologia di carburante? Diesel(1),Benzina(2),Ibrida(3)\n"))
    while(carburante !=1 and carburante != 2 and carburante != 3):
        carburante=int(input("inserire una tipologia di carburante valida\n"))
    valori['Fuel_Type']=carburante
    age=-1
    travel=int(input("Ti interessa una macchina adatta a viaggiare? Si(1) o no(2): \n"))
    if travel==1:
        valori['travel']=1
    scelta1=int(input('ti interesssa una particolare fascia di uscita?Digita 1 per si 0 per no\n'))
    while(scelta1 != 0 and scelta1 != 1):
        scelta1=input('inserire un valore valido\n')
    if scelta1==1:
        while(age !=0 and age !=1 and age!=2):
         age=int(input("Digitare 0 per macchine uscite prima del 2014\ndigitare 1 per macchine uscite tra il 2014 e il 2019 \ndigitare 2 per macchine uscite più recentemente\n"))
        valori['Year_Category']=age
    fuel_consume=int(input("Hai bisogno di una macchina con consumi bassi? Si(1) o no(0) \n"))
    if fuel_consume ==1:
        valori['consumption']=0
    macchine_filtrate=getsolution(valori)
    print("questa è la lista di macchine che soddisfano i tuoi requisiti")
    print(macchine_filtrate)
else:
        list=[]
        print("Inserisci le caratteristiche di cui vuoi trovare macchine simili\n")
        marca=""
        df=pd.read_csv('./CSVs/datasetfiltrato.csv')
        listmodel=np.unique(df['Make'])
        while not marca in listmodel:
            marca=input("Mettere il nome della macchina di cui si vuole sapere il prezzo. \nChevrolet,\nDatsun,\nFord,\nHonda,\nHyundai,\nJeep,\nKia,\nMG Motors,\nMahindra,\nMaluti Suzuki,\nNissan,\nRenault,\nSkoda,\nTata,\nToyota,\nVolkswagen\n")
        list.append(Make(marca))
        lista_modelli=ricerca(marca)
        for modello in lista_modelli:
            print('modello',modello)
        trovato=False
          
        while trovato == False:
            modello=input('digitare il modello\n')
            for model in lista_modelli:
                if model == modello:
                    trovato=True  

        listcolor=np.unique(df['Color'])
        color=''
        print('scegliere tra i colori disponibili\n',listcolor)
        while not color in listcolor:
            print(listcolor)
            color=input('scegliere un colore tra quelli disponibili\n')
        list.append(color)
        listbodytype=np.unique(df['Body_Type'])
        bodytype=''
        while not bodytype in bodytype:
            print(listbodytype)
            bodytype=input('scegliere una tipologia tra quelli disponibili')
        list.append(bodytype)
        km=int(input("Inserire la quantità di km percorsi\n"))
        while(km<1116):
            km=int(input("Inserire la quantità di km percorsi(deve essere maggiore di 1116)\n"))    
        list.append(km)
        while(owners<=0):
            owners=int(input("Inserire il numero di proprietari\n"))
        list.append(owners)
        
        seatingcapacity=0
        while(seatingcapacity<4 and seatingcapacity>8):
            seatingcapacity=input('scegliere il numero di posti a sedere compreso tra 4 e 8')
        list.append(seatingcapacity)

        fuel_type=''
        while(fuel_type!='petrol' and fuel_type!='diesel' and fuel_type!='petrol+cng' ):
            fuel_type('scegliere il carburante desiderato tra benzina diesel e petrol+cng')
        if fuel_type=='petrol':
            list.append(2)
        elif fuel_type=='diesel':
            list.append(1)
        else:
            list.append(0)

        fuel_tank_capacity=0
        while fuel_tank_capacity<15 and fuel_tank_capacity>70:
            fuel_tank_capacity=int(input('inserire la capienza del bagaliaglio compresa tra 15 e 70'))
        list.append(fuel_tank_capacity)
        cc=0
        while(cc>623 or cc<2180):
            cc=int(input('inserire la cilindrata compresa tra 624 e 2179'))
        list.append(cc)
        transmission=''
        listtransmission=np.unique(df['Transmission'])
        while(not transmission in listtransmission):
            print(listtransmission)
            transmission=input('Inserire un tipo di trasmissione valida:')
        if transmission=='4-Speed':
            list.append(4)
        elif transmission=='5-Speed':
            list.append(5)
        elif transmission=='6-Speed':
            list.append(6)
        elif transmission=='7-Speed':
            list.append(7)
        else:
            list.append(1)

        transmissiontype='' 
        while(transmissiontype != 'Manual' and transmissiontype!= 'Automatic'):
            transmissiontype=input('Inserire tipo di cambio(Manuale o Automatico) della vettura:')
        if transmissiontype=='Manual':
            list.append(1)
        else:
            list.append(2)

        power=0
        while(power<34 and power>167):
            power=input('Scegliere il numero di cavalli della vettura ( da 34 a 167 ): ')
        list.append(power)

        torque=0
        while(torque<48 and torque>380):
            torque=input('Scegliere la coppia della vettura ( tra 48 e 380 ): ')
        list.append(torque)

        consumption=''
        while consumption != 'Bassi' and consumption !='Medi':
            consumption=input('Inserire il tipo di consumi della macchina ( Bassi o Medi ):')
        if consumption=='Bassi':
            list.append(0)
        else:
            list.append(1)

        Year_Category=0
        while(Year_Category <2011 and Year_Category>2021 ):
            Year_Category=input('Inserire anno di uscita della vettura ( dal 2011 al 2021 )')
        if Year_Category<2014:
            list.append(0)
        elif Year_Category>2013 and Year_Category<2020:
            list.append(1)
        else: 
            list.append(2)

        sport=''
        while(sport !='sport' and sport!='utilitaria'):
            sport=input("Ti interessa una macchina sportiva o utilitaria? sport o utilitaria\n")
        if sport=='sport':
            list.append(1)
        else:
            list.append(0)

        drive_easy=''
        while(drive_easy !='si' and drive_easy!='no'):
            drive_easy=input("Ti interessa una macchina semplice da portare?si o no\n")
        if drive_easy=='si':
            list.append(1)
        else:
            list.append(0)
        
        travel=''
        while(travel !='si' and travel!='no'):
            travel=input("Ti interessa una macchina adatta per viaggiare?si o no\n")
        if travel=='si':
            list.append(1)
        else:
            list.append(0)
        
        euro=0
        while(euro != 5 and euro != 6):
            euro=input("Ti interessa una macchina adatta euro 5 o euro 6? Digitare il numero corrispondente\n")
        if euro==5:
            list.append(5)
        else:
            list.append(6)
        print("Il prezzo della macchina è il seguente")
        print(predizione(list))