def mpbe(o,p,mp):
    return o*3600 + p*60 + mp
def idobe(mp):
    return str(mp//3600) + ' ' + str(mp%3600//60) + ' ' + str(mp/60)


hivasok = []
fajl = open("hivas.txt", "rt", encoding="utf-8")
for sor in fajl:
    sor = [int(elem) for elem in sor.strip().split()]
    hivas = {}
    hivas['eleje'] = mpbe(sor[0],sor[1],sor[2])
    hivas['vege'] = mpbe(sor[3],sor[4],sor[5])
    hivas['hossza'] = hivas['vege'] - hivas['eleje'] 
    hivasok.append(hivas)
fajl.close()

print("3. feladat")
statisztika = {}
for hivas in hivasok:
    ora = idobe(hivas['eleje']).split()[0]
    statisztika[ora] = statisztika.get(ora, 0) + 1
for kulcs, ertek in statisztika.items():
    print(kulcs ,'óra', ertek, 'hívás')
    
print("4. feladat")
leghosszabbhivas = 0
leghosszabbhivasSorszam = 0
hivasSorszam = 1
for hivas in hivasok:
    hivasHossza = hivas['hossza']
    if leghosszabbhivas < hivasHossza:
        leghosszabbhivas = hivasHossza
        leghosszabbhivasSorszam = hivasSorszam
    hivasSorszam += 1    
print("A leghosszabb ideig volban lévő hívó",leghosszabbhivasSorszam,"sorban szerepel, a hívás hossza:",leghosszabbhivas,"volt")

print("5.feladat")
idopont = mpbe(*[int(elem) for elem in input("Adjon meg egy időpontot! (óra,perc,másodperc): ").split()])
eppenhiv = [hivas for hivas in hivasok if hivas['eleje'] <= idopont <= hivas['vege']]
if eppenhiv:
    print('Várakozók száma:', len(eppenhiv)- 1, "és a beszélő az a", hivasok.index(eppenhiv[0])+ 1, ". hívó")
else:
    print('Nem volt beszélő')
    
munkaido_eleje = mpbe(8,0,0)
munkaido_vege =  mpbe(12,0,0)
utolso_beszelo = 0
while hivasok[utolso_beszelo]['vege'] < munkaido_eleje:
    utolso_beszelo += 1
for index, hivas in enumerate(hivasok):
    if hivas['vege'] > hivasok[utolso_beszelo]['vege'] and hivas['eleje'] < munkaido_vege:
        utolso_beszelo_varakozas = max(hivasok[utolso_beszelo]['vege'] - hivas['eleje'], 0)
        utolso_beszelo = index

print("6. feladat")
print("Az utolsó telefonáló adata a(z)", utolso_beszelo+1 ,"sorban vannak",utolso_beszelo_varakozas,"másodpercig várt.")
