#ROZDĚLENÍ STRINGU

#prvních 5 písmen ze slova indexování
#print("indexování" [0:5])
print("indexování" [:5])

#posledních 5 písmen ze slova indexování
#print("indexování" [5:]) # bude fungovat pouze pokud vím, s jakým slovem se bude pracovat a odpočítám si, jaký index znamená páté písmeno od konce
print("indexování" [-5:]) #vypíše posledních 5 znaků, nemusím počítat indexy od začátku.

#každé třetí písmeno slova 'indexování' (počínaje prvním písmenem "i")
print("indexování" [::3])