import csv
from pyswip import Prolog
import pandas as pd
import numpy as np

df=pd.read_csv('./CSVs/datasetfiltrato.csv')
print(df.columns)
prolog=Prolog()
prolog.consult('car.pl')
#definisco tute le proprietà delle macchine, accedendo tramite il campo id al valore della proprietà di interesse
prolog.assertz('make(ID, M) :- car(ID, M, _, _, _, _, _, _,_,_,_,_,_,_,_,_,_,_)')
prolog.assertz('model(ID, M) :- car(ID, _, M, _, _, _, _, _,_,_,_,_,_,_,_,_,_,_)')
prolog.assertz('make_year(ID, Y) :- car(ID, _, _, Y, _, _, _, _,_,_,_,_,_,_,_,_,_,_)')
prolog.assertz('color(ID, C) :- car(ID, _, _, _, C, _, _, _,_,_,_,_,_,_,_,_,_,_)')
prolog.assertz('body_type(ID, B) :- car(ID, _, _, _, _, B, _, _,_,_,_,_,_,_,_,_,_,_)')
prolog.assertz('kilometers_run(ID, K) :- car(ID, _, _, _, _, _, K, _,_,_,_,_,_,_,_,_,_,_)')
prolog.assertz('no_of_owners(ID, N) :- car(ID, _, _, _, _, _, _, N,_,_,_,_,_,_,_,_,_,_)')
prolog.assertz('seating_capacity(ID, S) :- car(ID, _, _, _, _, _, _, _,S,_,_,_,_,_,_,_,_,_)')
prolog.assertz('fuel_type(ID, T) :- car(ID, _, _, _, _, _, _, _,_,T,_,_,_,_,_,_,_,_)')
prolog.assertz('fuel_tank_capacity(ID, C) :- car(ID, _, _, _, _, _, _, _,_,_,C,_,_,_,_,_,_,_)')
prolog.assertz('cc_displacement(ID, C) :- car(ID, _, _, _, _, _, _, _,_,_,_,C,_,_,_,_,_,_)')
prolog.assertz('transmission(ID, T) :- car(ID, _, _, _, _, _, _, _,_,_,_,_,T,_,_,_,_,_)')
prolog.assertz('transmission_type(ID, T) :- car(ID, _, _, _, _, _, _, _,_,_,_,_,_,T,_,_,_,_)')
prolog.assertz('power(ID, P) :- car(ID, _, _, _, _, _, _, _,_,_,_,_,_,_,P,_,_,_)')
prolog.assertz('torque(ID, T) :- car(ID, _, _, _, _, _, _, _,_,_,_,_,_,_,_,T,_,_)')
prolog.assertz('kilometer_at_liter(ID, K) :- car(ID, _, _, _, _, _, _, _,_,_,_,_,_,_,_,_,K,_)')
prolog.assertz('price(ID, P) :- car(ID, M, _, _, _, _, _, _,_,_,_,_,_,_,_,_,_,P)')

#creo un dizionario avente come chiave id e valori le proprietà
car=[]
with open('./CSVs/datasetfiltrato.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        id = row['ID']
        car.append(id)
#stampo tutte le proprietà
for id in car:
    for result in prolog.query("make({},M)".format(id)):
        print("Make:", result["M"])
    for result in prolog.query("model({},M)".format(id)):
        print("Model:", result["M"])
    for result in prolog.query("make_year({},Y)".format(id)):
        print("Make year:", result["Y"])
    for result in prolog.query("color({},C)".format(id)):
        print("Color:", result["C"])
    for result in prolog.query("body_type({},B)".format(id)):
        print("Body type:", result["B"])
    for result in prolog.query("kilometers_run({},K)".format(id)):
        print("Kilometers run:", result["K"])
    for result in prolog.query("no_of_owners({},N)".format(id)):
        print("Number of owners:", result["N"])
    for result in prolog.query("seating_capacity({},C)".format(id)):
        print("Seating capacity:", result["C"])
    for result in prolog.query("fuel_type({},T)".format(id)):
        print("Fuel type:", result["T"])
    for result in prolog.query("fuel_tank_capacity({},C)".format(id)):
        print("Fuel tank capacity:", result["C"])
    for result in prolog.query("cc_displacement({},C)".format(id)):
        print("Cc_displacement:", result["C"])
    for result in prolog.query("transmission({},T)".format(id)):
        print("Transmission:", result["T"])
    for result in prolog.query("transmission_type({},T)".format(id)):
        print("Transmission type:", result["T"])
    for result in prolog.query("power({},P)".format(id)):
        print("Power:", result["P"])
    for result in prolog.query("torque({},T)".format(id)):
        print("Torque:", result["T"])
    for result in prolog.query("kilometer_at_liter({},K)".format(id)):
        print("kilometer at liter:", result["K"])
    for result in prolog.query("price({},P)".format(id)):
        print("Price:", result["P"])
  