# Cvičení z první lekce
#Najdi a vypiš "u"
print("Matouš"[4]) 
print("Matouš"[-2]) # jiná vairanta

#Najdi a vypiš poslední znak
print("Matouš"[-1])

# Najdi a vypiš "matous"
print("matous.holinka@gmail.com"[0:6])
print("matous.holinka@gmail.com"[:6]) #jiný způsob, když se začíná od prvního znaku, tj. nultého indexu, tak se dá nula vynechat

# Najdi a vypiš všechny sudé číslice (bez nuly)
print("1234567890"[1:9:2]) #vynechá 1 a pak vypíše každou druhou hodnotu a zastaví se u devátého znaku
print("1234567890"[1:-2:2])

# Najdi a vypiš "Matouš" a "Holinka" pomocí mezery
print("Matouš" + "Holinka")
print("Matouš" + " " + "Holinka")