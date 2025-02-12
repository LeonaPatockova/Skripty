#Vytvoř proměnné jmeno, vaha, vyska a zadej do nich hodnoty,
jmeno = "Martin"
vaha_kg = 80
vyska_cm = 200
vyska_m = vyska_cm/100

#vytvoř proměnnou bmi a přiřaď k ní vzorec, pomocí proměnných vaha, vyska a aritmetického operátoru na druhou ,vytvoř proměnnou kategorie, do které uložíš název kategorie odpovídající hodnotě BMI,
bmi = vaha_kg/(vyska_m**2)

# vytvoř roměnnou kategorie, do které uložíš název kategorie odpovídající hodnotě BMI,
if bmi < 18.5:
    kategorie = "podvýživa"
elif bmi >= 18.5 and bmi < 25:
    kategorie = "zdravá váha"
elif bmi >= 25 and bmi < 30:
    kategorie = "mírná nadváha"
elif bmi >= 30 and bmi < 40:
    kategorie = "obezita"
elif bmi >= 40:
    kategorie = "těžká obezita"
else: 
    print("Chyba výpočtu")
# takhle je to správně, ale je tam zbytečn mc podmínek v ifu. Pokud se splní podmínka, uloží se hodnotě do proměnné a celý if tím končí
#vypiš výsledek do věty, jak je uvedeno níže
print (jmeno, "tvé BMI je", bmi, ", což spadá do kategorie", kategorie)


# Vstupní hodnoty uživatele
#vyska = 2
#vaha = 80
#jmeno = 'Martin'

# Výpočet BMI
#bmi = vaha / vyska ** 2

# Vytvoř proměnnou "kategorie", kam uložíš slovní ohodnocení BMI
#if bmi > 40:
#    kategorie = 'těžká obezita'
#elif bmi > 30:
#    kategorie = 'obezita'
#elif bmi > 25:
#    kategorie = 'mírná nadváha'
#elif bmi > 18.5:
#    kategorie = 'zdravá váha'
#else:
#    kategorie = 'podvýživa'

# Vytiskni odpoved s vysledkem
#print(jmeno, "tvé BMI je", bmi, ", což spadá do kategorie", kategorie, ".")