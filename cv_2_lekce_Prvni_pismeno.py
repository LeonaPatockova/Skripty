#zapiš proměnné
vstupni_cisla = [1,2,3,4,5,6,7] #list
vstupni_pismena = ["p", "ú", "s", "č", "p", "s", "n"] #list
tyden = ("pondělí", "úterý", "středa", "čtvrtek", "pátek", "sobota", "neděle") #tuple

#vytvoř proměnnou cislo_dne a zapiš do ní hodnotu 3
cislo_dne = 3

#ověř, jestli hodnota v cislo_dne je v listu vstupni_cisla, pokud není, vypiš výstup podle vzoru níže,pokud je, vypiš zprávu "Správná vstupní hodnota!"
#print(vstupni_cisla.index(cislo_dne)) #vypíše index, na kterém se nachází zadaná hodnota ve zvoleném listu, pokud číslo nenajda, zahlásí chybu, protože nenajde index
print(vstupni_cisla.count(cislo_dne)) #vrátí počet výskytů zadané hodnoty ve zvoleném listu

if cislo_dne in vstupni_cisla: # další varianta ověření, jestli číslo v proměnné cislo_dne je v listu vstupni_cisla
    print("Správná vstupní hodnota. Číslo dne", cislo_dne, "je v seznamu vstupních čísel")
else:
    print("Špatná vstupní hodnota. Číslo dne", cislo_dne, "není v seznamu vstupních čísel")

#.. dále vytvoř proměnnou den_tydne a pomocí upravené hodnoty v proměnné cislo_dne, naindexuj z proměnné tyden požadovaný den (př. 1 --> "pondělí", 2 --> "úterý"),
den_tydne = tyden[cislo_dne - 1]
print(den_tydne)

#ověř, jestli vybraný str v proměnné den_tydne má stejné počáteční písmeno, jako jsou v proměnné vstupni_pismena (ověř opět pomocí upraveného indexu),
if den_tydne[0] == vstupni_pismena[cislo_dne - 1]:
    print("Správné písmeno je:", den_tydne[0])
else:
    print("Špatné písmeno")


#zápis do jednoho ifu
print("Řešením se zadáním s vnořeným ifem")
vstupni_cisla = [1,2,3,4,5,6,7] #list
vstupni_pismena = ["p", "ú", "s", "č", "p", "s", "n"] #list
tyden = ("pondělí", "úterý", "středa", "čtvrtek", "pátek", "sobota", "neděle")   
cislo_dne = 3

if cislo_dne in vstupni_cisla:
    print("Správná vstupní hodnota. Číslo dne", cislo_dne, "je v seznamu vstupních čísel")
    den_tydne = tyden[cislo_dne - 1]
    if den_tydne.startswith(vstupni_pismena[cislo_dne - 1]):
        print("Správné písmeno")
    else: 
        print("Špatné písmeno")
else:
    print("Špatná vstupní hodnota")
