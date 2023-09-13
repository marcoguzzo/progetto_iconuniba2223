
import csv
from numpy import nanvar

# leggo il file CSV dei clienti
# newline vuoto perchè rilevato automaticamente
with open('./CSVs/datasetnormalizzato.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    #salto la prima riga
    first_row = next(reader)
    
# Calcola il numero di colonne
    # creo un fatto Prolog per ogni riga del dataset
    facts = []
    for row in reader:
        # forma: nome_fatto(argomento1, argomento2, ...)
        fact = f"{'car'}({', '.join(row[0:])})."
        facts.append(fact)
# scrivo i fatti Prolog in un file .pl
with open('car.pl', 'w') as plfile:
    plfile.write('\n'.join(facts))
