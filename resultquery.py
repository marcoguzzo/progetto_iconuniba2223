import numpy as np
import pandas as pd
from pyswip import *
from pyswip.easy import *

prolog = Prolog()

prolog.consult('car.pl'),
prolog.consult('regole.pl')


# Apro il file .pl in modalita scrittura e scrivo le asserzioni derivate nel file .pl utilizzando il metodo write()
with open('./regole/euro0.pl', 'w') as file:
    for result in prolog.query("euro0(ID)"):
        file.write('{}\n'.format(str(result["ID"])))

with open('./regole/euro1.pl', 'w') as file:
    for result in prolog.query("euro1(ID)"):
        file.write('{}\n'.format(str(result["ID"])))
with open('./regole/euro2.pl', 'w') as file:
    for result in prolog.query("euro2(ID)"):
        file.write('{}\n'.format(str(result["ID"])))

with open('./regole/euro3.pl', 'w') as file:
    for result in prolog.query("euro3(ID)"):
        file.write('{}\n'.format(str(result["ID"])))

with open('./regole/euro4.pl', 'w') as file:
    for result in prolog.query("euro4(ID)"):
        file.write('{}\n'.format(str(result["ID"])))

with open('./regole/euro5.pl', 'w') as file:
    for result in prolog.query("euro5(ID)"):
        file.write('{}\n'.format(str(result["ID"])))

with open('./regole/euro6.pl', 'w') as file:
    for result in prolog.query("euro6(ID)"):
        file.write('{}\n'.format(str(result["ID"])))

with open('./regole/low_fuel_consumption.pl', 'w') as file:
    for result in prolog.query("low_fuel_consumption(ID)"):
        file.write('{}\n'.format(str(result["ID"])))

with open('./regole/medium_fuel_consumption.pl', 'w') as file:
    for result in prolog.query("medium_fuel_consumption(ID)"):
        file.write('{}\n'.format(str(result["ID"])))

with open('./regole/high_fuel_consumption.pl', 'w') as file:
    for result in prolog.query("high_fuel_consumption(ID)"):
        file.write('{}\n'.format(str(result["ID"])))

with open('./regole/travel.pl', 'w') as file:
    for result in prolog.query("travel(ID)"):
        file.write('{}\n'.format(str(result["ID"])))

with open('./regole/not_travel.pl', 'w') as file:
    for result in prolog.query("not_travel(ID)"):
        file.write('{}\n'.format(str(result["ID"])))

with open('./regole/drive_easy.pl', 'w') as file:
    for result in prolog.query("drive_easy(ID)"):
        file.write('{}\n'.format(str(result["ID"])))

with open('./regole/utilitarian_cars.pl', 'w') as file:
    for result in prolog.query("utilitarian_cars(ID)"):
        file.write('{}\n'.format(str(result["ID"])))

with open('./regole/sport_cars.pl', 'w') as file:
    for result in prolog.query("sport_cars(ID)"):
        file.write('{}\n'.format(str(result["ID"])))

with open('./regole/old_years_car.pl', 'w') as file:
    for result in prolog.query("old_years_car(ID)"):
        file.write('{}\n'.format(str(result["ID"])))

with open('./regole/recent_years_car.pl', 'w') as file:
    for result in prolog.query("recent_years_car(ID)"):
        file.write('{}\n'.format(str(result["ID"])))

with open('./regole/new_years_car.pl', 'w') as file:
    for result in prolog.query("new_years_car(ID)"):
        file.write('{}\n'.format(str(result["ID"])))

with open('./regole/drive_not_easy.pl', 'w') as file:
    for result in prolog.query("drive_not_easy(ID)"):
        file.write('{}\n'.format(str(result["ID"])))
        
with open('./regole/bollo_euro0.pl', 'w') as file:
    for result in prolog.query("rate_euro0(ID,Rate)"):
                                file.write('{}{}{}\n'.format(str(result["ID"])," ",str(result["Rate"])))

with open('./regole/bollo_euro1.pl', 'w') as file:
    for result in prolog.query("rate_euro1(ID,Rate)"):
                                file.write('{}{}{}\n'.format(str(result["ID"])," ",str(result["Rate"])))


with open('./regole/bollo_euro2.pl', 'w') as file:
    for result in prolog.query("rate_euro2(ID,Rate)"):
                                file.write('{}{}{}\n'.format(str(result["ID"])," ",str(result["Rate"])))


with open('./regole/bollo_euro3.pl', 'w') as file:
    for result in prolog.query("rate_euro3(ID,Rate)"):
                                file.write('{}{}{}\n'.format(str(result["ID"])," ",str(result["Rate"])))


with open('./regole/bollo_euro4.pl', 'w') as file:
    for result in prolog.query("rate_euro4(ID,Rate)"):
                                file.write('{}{}{}\n'.format(str(result["ID"])," ",str(result["Rate"])))


with open('./regole/bollo_euro5.pl', 'w') as file:
    for result in prolog.query("rate_euro5(ID,Rate)"):
                                file.write('{}{}{}\n'.format(str(result["ID"])," ",str(result["Rate"])))

with open('./regole/bollo_euro6.pl', 'w') as file:
    for result in prolog.query("rate_euro6(ID,Rate)"):
                                file.write('{}{}{}\n'.format(str(result["ID"])," ",str(result["Rate"])))
