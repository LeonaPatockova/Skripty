#vytvořím list se zaměstnanci
zamestnanci = ["František","Bruno","Anna", "Jakub", "Klára", "Anežka", "Anežka", "Anežka"]

#Ulož poslední index ze zadaného listu zamestnanci do proměnné posledni_index
posledni_index = zamestnanci[-1]
print(posledni_index) #kontrola, že se uložila správná hodnota

#Vypiš jméno na indexu 2 za string: 'Na indexu 2 je: '
print("Na indexu 2 je:", zamestnanci[2])

#Vypiš jméno na posledním indexu za string: 'Na <posledni_index> indexu je:',
cislo_posledniho_indexu = len(zamestnanci) - 1
print(cislo_posledniho_indexu)
print("Na",cislo_posledniho_indexu,".indexu je:", posledni_index)

#vypiš jména od indexu 2 do 5 za string: 'V intervalu od 2 do 5 je:',

print("V intervalu od indexu 2 do indexu 5 je:", zamestnanci[2:6])
print("V intervalu od indexu 2 do indexu 5 je:", zamestnanci[2], ", ", zamestnanci[3], ", ", zamestnanci[4], "a ", zamestnanci[5]) #nápad jak to uděla, aby se vypsala jména bez hranatých závorek

#vypiš každý třetí prvek listu zamestnanci počínaje hodnotou 'František' za string: 'Každý třetí člen je:'.
index_Frantisek = zamestnanci.index("František")
print(index_Frantisek) #kontrola, že se uložila nula
print(zamestnanci[index_Frantisek::3])