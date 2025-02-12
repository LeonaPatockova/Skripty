#SPOJOVÁNÍ STRINGŮ
jmeno = "Lukáš"
prijmeni = "Dvořák"

#spojit jméno a příjmení do nové proměnné, oddělit mezerou
cele_jmeno = jmeno + " " + prijmeni

#do nové proměnné uložit délku jména a příjmení, včetně mezery, která je odděluje
delka_jmena = len(cele_jmeno)

#vypíše jmého a jeho délku
print("Celé jméno:", cele_jmeno)
print("Délka jména:", delka_jmena)

#vypíše celé jméno, které bude nahoře i dole ohraničené znakem "=" - ten bude zopkakovaný tolikrát, kolik znaků obsahuje sring v proměnné cele_jmeno
print("=" * delka_jmena)
print(cele_jmeno)
print("=" * delka_jmena)