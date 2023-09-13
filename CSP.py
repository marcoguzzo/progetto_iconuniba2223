from constraint import Problem
import numpy as np
import pandas as pd
import time

#funzione per definire se è una macchina dai ocnsumi bassi
def consumption(consumi):
    return consumi == 0

#funzione per definire se è una macchina uscita prima del 2014
def oldyear(uscita):
    return uscita == 0

#funzione per definire se è una macchina uscita tra il 2014 e il 2019
def recentyear(uscita):
    return uscita == 1

#funzione per definire se è una macchina uscita dopo il 2019
def newyear(uscita):
    return uscita == 2

#funzione per definire se è una macchina adatta a percorrere molti kilometri
def travel(travel):
    return travel == 1

#funzione per definire se è una macchina diesel
def diesel(carburante):
    return carburante == 1

#funzione per definire se è una macchina a benzina
def benzina(carburante):
    return carburante == 2

#funzione per definire se è una macchina ibrida
def ibrida(carburante):
    return carburante == 3

#funzione per definire se è una macchina sportiva
def sport(sport):
    return sport == 1

#funzione per definire se è una macchina utilitaria
def utilitaria(util):
    return util == 0

#funzione per creare il csp e restituire le soluzioni
def getsolution(valori):
    df=pd.read_csv('./CSVs/dataset_operativo.csv')
    problem=Problem()
    #aggiungo le variabili al csp in base a quali siano gli interessi dell'utente e aggiungo i vincoli in base alle variabili aggiunte
    problem.addVariable('sport_cars', [0, 1])
    problem.addVariable('Fuel_Type', [1, 2, 3])
    soluzioni={}
    if valori['sport_cars'] == 1:
        problem.addConstraint(sport, ('sport_cars',))
    else:
        problem.addConstraint(utilitaria, ('sport_cars',))

    if valori['Fuel_Type'] == 1:
        problem.addConstraint(diesel, ('Fuel_Type',))
    elif valori['Fuel_Type'] == 2:
        problem.addConstraint(benzina, ('Fuel_Type',))
    else:
        problem.addConstraint(ibrida, ('Fuel_Type',))
    
    if 'travel' in valori:
        problem.addVariable('travel', [0, 1])
        problem.addConstraint(travel, ('travel',))

    if 'Year_Category' in valori:
        problem.addVariable('Year_Category', [0, 1, 2])
        if valori['Year_Category'] == 0:
            problem.addConstraint(oldyear, ('Year_Category',))
        elif valori['Year_Category'] == 1:
            problem.addConstraint(recentyear, ('Year_Category',))
        else:
            problem.addConstraint(newyear, ('Year_Category',))
   
    if 'consumption' in valori:
        problem.addVariable('consumption', [0, 1, 2])
        problem.addConstraint(consumption, ('consumption',))
    #misuro le prestazioni tramite tempo impiegato, numero di vincoli e numero di variabili
    start_time = time.time()
    solution=problem.getSolution()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Tempo impiegato:", elapsed_time, "secondi")  
    print('numero di vincoli: ',len(problem._constraints()))
    print('numero di variabili: ',(problem._variables()))

    #filtro le macchine del dataset che hanno i valori che sono soluzioni del csp
    machine_filtered=[]
    for index,rows in df.iterrows():
        condizione=True
        for soluzione,variabile in zip(solution.values(),solution.keys()):
            if rows[variabile]!=soluzione:
                condizione=False
        if condizione==True:
            machine_filtered.append(str(rows['Make'])+' '+str(rows['Model'])+' '+str(rows['Make_Year']))
    return np.unique(machine_filtered)
