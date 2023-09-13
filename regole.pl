% regola per definire se una macchina è semplice da portare
drive_easy(ID):- car(ID,_,_,_,_,Body_Type,_,_,_,_,_,_,_,Transmission_Type,_,_,_,_), Body_Type \== 2, Transmission_Type \== 1.     

% regola per definire se una macchina non è semplice da portare
drive_not_easy(ID):- car(ID,_,_,_,_,Body_Type,_,_,_,_,_,_,_,Transmission_Type,_,_,_,_), Body_Type = 2, Transmission_Type = 1.     

% regola per definire la classe euro
euro0(ID):-car(ID,_,_,Make_Year,_,_,_,_,_,_,_,_,_,_,_,_,_,_), Make_Year<1993.

euro1(ID):-car(ID,_,_,Make_Year,_,_,_,_,_,_,_,_,_,_,_,_,_,_), Make_Year<1996.

euro2(ID):-car(ID,_,_,Make_Year,_,_,_,_,_,_,_,_,_,_,_,_,_,_), Make_Year>=1996, Make_Year<2000.

euro3(ID):-car(ID,_,_,Make_Year,_,_,_,_,_,_,_,_,_,_,_,_,_,_), Make_Year>=2000, Make_Year<2005.

euro4(ID):-car(ID,_,_,Make_Year,_,_,_,_,_,_,_,_,_,_,_,_,_,_), Make_Year>=2005, Make_Year<2009.

euro5(ID):-car(ID,_,_,Make_Year,_,_,_,_,_,_,_,_,_,_,_,_,_,_), Make_Year>=2009, Make_Year<2014.

euro6(ID):-car(ID,_,_,Make_Year,_,_,_,_,_,_,_,_,_,_,_,_,_,_), Make_Year>=2014.

% REGOLA PER STABILIRE SE E UNA MACCHINA ADATTA A FARE VIAGGI
travel(ID):-car(ID,_,_,_,_,Body_Type,_,_,_,_,Fuel_Tank_Capacity,_,_,_,_,_,_,_), Body_Type = 2, Fuel_Tank_Capacity > 50.

% REGOLA PER STABILIRE SE NON E UNA MACCHINA ADATTA A FARE VIAGGI
not_travel(ID):-car(ID,_,_,_,_,Body_Type,_,_,_,_,Fuel_Tank_Capacity,_,_,_,_,_,_,_), Body_Type \== 2, Fuel_Tank_Capacity < 51.


% REGOLA PER STABILIRE IN QUALE RANGE DI ANNO RIENTRA UNA MACCHINA
old_years_car(ID):-car(ID,_,_,Make_Year,_,_,_,_,_,_,_,_,_,_,_,_,_,_), Make_Year<2014.

recent_years_car(ID):-car(ID,_,_,Make_Year,_,_,_,_,_,_,_,_,_,_,_,_,_,_), Make_Year<2020, Make_Year>2013.

new_years_car(ID):-car(ID,_,_,Make_Year,_,_,_,_,_,_,_,_,_,_,_,_,_,_), Make_Year>2019.

% REGOLA PER DEFINIRE SE UN AUTO è SPORTIVA O UTILITARIA
sport_cars(ID):-car(ID,_,_,_,_,_,_,_,_,_,_,_,_,_,Power,_,_,_), Power>121.
utilitarian_cars(ID):-car(ID,_,_,_,_,_,_,_,_,_,_,_,_,_,Power,_,_,_), Power<122.

% regola per definire i kilowatt
kilowatt(ID, Kilowatt) :-
    car(ID, _, _, _, _, _, _, _, _, _, _, _, _, _, Power, _, _, _),
    Kilowatt is Power * 0.7355.

% regola per definire il bollo auto per macchine euro0
rate_euro0(ID, Rate) :-
    car(ID, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _),
    euro0(ID),
    kilowatt(ID, Kilowatt),
    (Kilowatt < 101 -> Rate is 3.00 * Kilowatt ; Result is Kilowatt - 100, Rate is 3.00 * 100 + Result * 4.50).


% regola per definire il bollo auto per macchine euro1
rate_euro1(ID, Rate) :-
    car(ID, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _),
    euro1(ID),
    kilowatt(ID, Kilowatt),
    (Kilowatt < 101 -> Rate is 2.90 * Kilowatt ; Result is Kilowatt - 100, Rate is 2.90 * 100 + Result * 4.35).

% regola per definire il bollo auto per macchine euro2
rate_euro2(ID, Rate) :-
    car(ID, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _),
    euro2(ID),
    kilowatt(ID, Kilowatt),
    (Kilowatt < 101 -> Rate is 2.80 * Kilowatt ; Result is Kilowatt - 100, Rate is 2.80 * 100 + Result * 4.35).

% regola per definire il bollo auto per macchine euro3
rate_euro3(ID, Rate) :-
    car(ID, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _),
    euro3(ID),
    kilowatt(ID, Kilowatt),
    (Kilowatt < 101 -> Rate is 2.70 * Kilowatt ; Result is Kilowatt - 100, Rate is 2.70 * 100 + Result * 4.05).

% regola per definire il bollo auto per macchine euro4
rate_euro4(ID, Rate) :-
    car(ID, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _),
    euro4(ID),
    kilowatt(ID, Kilowatt),
    (Kilowatt < 101 -> Rate is 2.58 * Kilowatt ; Result is Kilowatt - 100, Rate is 2.58 * 100 + Result * 3.87).

% regola per definire il bollo auto per macchine euro5
rate_euro5(ID, Rate) :-
    car(ID, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _),
    euro5(ID),
    kilowatt(ID, Kilowatt),
    (Kilowatt < 101 -> Rate is 2.58 * Kilowatt ; Result is Kilowatt - 100, Rate is 2.58 * 100 + Result * 3.87).

% regola per definire il bollo auto per macchine euro6
rate_euro6(ID, Rate) :-
    car(ID, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _),
    euro6(ID),
    kilowatt(ID, Kilowatt),
    (Kilowatt < 101 -> Rate is 2.58 * Kilowatt ; Result is Kilowatt - 100, Rate is 2.58 * 100 + Result * 3.87).



% regola per definire se una macchina è a bassi consumi
low_fuel_consumption(ID) :- car(ID,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,KilometerAtLiter,_), KilometerAtLiter > 19.9.

% regola per definire se una macchina ha dei consumi giusti 
medium_fuel_consumption(ID) :- car(ID,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,KilometerAtLiter,_), KilometerAtLiter > 10.0, KilometerAtLiter < 20.0.

% regola per definire se una macchina ha dei consumi alti
high_fuel_consumption(ID) :- car(ID,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,KilometerAtLiter,_), KilometerAtLiter < 10.1.

