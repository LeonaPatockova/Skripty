#Vytvoř list zamestnanci, který bude obsahovat stringy 'František', 'Anna', 'Jakub', 'Klára',
zamestnanci = ["František","Anna","Jakub","Klára"]
#zamestnanci = list() nemůže mít rovnou zapsaná jména, muse se vytvořit prázdný a pak do něj jednotlivá jména přidávat, takže je jednodušší vytvořit list přes hranaté závorky

#vypiš obsah zamestnanci za větu 'Zaměstnanci na začátku: '
print("Zaměstnanci na začátku:", zamestnanci)

#,vytvoř kopii listu zamestnanci a pojmenuj proměnnou zamestnanci_a,
zamestnanci_a = zamestnanci.copy()
#print(zamestnanci_a)  #jen pro kontrolu, jestli se udělala kopie zaměstnanců do proměnné zamestnanci_a

#přidej do listu zamestnanci_a jména 'Bruno' a 'Anežka',
novi_zamestnanci = ["Bruno", "Anežka"] #nejdřív vytvářím proměnnou pro nové zaměstnance, protože přes .append se nedá přidat víc jmen najednou. I extend potřebuje mít uvedený jen jeden nový seznam
zamestnanci_a.extend(novi_zamestnanci)
#print(zamestnanci_a) #kontrola, jeslti vypisuje správně

#vypiš obsah listu zamestnanci_a za string 'Nová jména přidána: ',
print("Nová jména přidána:", zamestnanci_a)

#vytvoř kopii listu zamestnanci a pojmenuj proměnnou zamestnanci_b
zamestnanci_b = zamestnanci.copy()

#vlož jméno 'Bruno' na index 1
zamestnanci_b.insert(1,"Bruno")

#vypiš obsah proměnné zamestnanci_b za string: 'Nová jména vložena:'.
print("Nová jména vložena:", zamestnanci_b)