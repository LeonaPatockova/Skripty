#KOUPĚ AUTA, OPERACE S DATOVÝM TYPEM str A int
#ceník
mercedes = 150_000
rolls_royce = 400_000
vybava = 50_000

#vytvoření slevy pro mercedes
sleva_merc = 5_000

#cena za 2 mercedesy
cena_2_merc = mercedes * 2

#cena mercedes a rolls-royce
cena_merc_a_rolls = mercedes + rolls_royce

#vypočítat cenu za dva Rolls-Royce s příplatkovou výbavou (každý z nich)
cena_2_rolls_s_vybavou = 2 * (rolls_royce + vybava)

#vypočítat cenu za Mercedes s příplatkovou výbavou
cena_merc_s_vybavou = mercedes + vybava

#vypočítat cenu po slevě Mercedesu
merc_se_slevou = mercedes - sleva_merc

#výpis infromací
print("Sleva na Mercedes:", sleva_merc)
print("Cena za dva Mercedesy je", cena_2_merc)
print("Cena za Mercdes a Rolls-Royce:", cena_merc_a_rolls)
print("Cena za dva Rolls-Royce s příplatkovou výbavou:", cena_2_rolls_s_vybavou)
print("Cena za Mercedes s příplatkovou výbavou:", cena_merc_s_vybavou)
print("Cena za Mercedes se slevou:", merc_se_slevou)