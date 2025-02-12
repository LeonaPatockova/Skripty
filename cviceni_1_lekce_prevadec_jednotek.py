#PŘEVADĚČ JEDNOTEK
#kg -> libry, km -> míle, litry -> galony

#převodník jednotek
kg_lb = 2.20
km_mile = 0.62
l_gal = 0.26

#počet jendotek, kerý má být převedený
kg_pocet = 80
km_pocet = 54
l_pocet = 5

#print(kg_pocet, " kg je", kg_pocet * kg_lb, " lb") řešení bez použití proměnné, do které se nejdřív výsledek uloží

#Výpočty
lb_vysledek = kg_pocet * kg_lb
mil_vysledek = km_pocet * km_mile
gal_vysledek = l_pocet * l_gal

#Výsledky
print(kg_pocet, "kg je", lb_vysledek, "liber")
print(km_pocet, "km je", mil_vysledek, "mil")
print(l_pocet, "l je", gal_vysledek, "galonů")