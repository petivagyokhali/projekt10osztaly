import random
import re
#játéktábla osztály a pálya létrehozásához
class JatekTabla:
    def __init__(self, palyameret, aknaszam):
        self.palyameret=palyameret
        self.aknaszam=aknaszam
        self.jatektabla=self.ujpalyaletrehozasa()#az aknák lerakásához
        self.ertek_rendeles_a_tobbi_mezohoz()
        
        #a sor és oszlop adatokat ebben a halmazban mentjük
        self.asas=set() #ha például a 3. sorban és a 4. oszlopban ásunk, akkor:self.asas={(3,4)}
    
    def ujpalyaletrehozasa(self):
        jatektabla=[[None for _ in range(self.palyameret)] for _ in range(self.palyameret)] #ezzel egy négyzetalakú táblát kapunk, egyenlőre None értékekkel
        #aknák lerakása
        lerakottaknak=0
        while lerakottaknak<self.aknaszam:
            elhelyezes=random.randint(0, self.palyameret**2-1)#ezzel az egész pályát megadjuk neki feltételként
            sor=elhelyezes//self.palyameret #szeretnénk visszakapni, hogy a palyameret hányszor megy bele az elhelyezésbe, hogy megtudjuk melyik sort nézzük (sor számozása)
            oszlop=elhelyezes%self.palyameret #oszlop számozása
            
            if jatektabla[sor][oszlop]=="x": #ha már ezen a mezőn egy akna(x) van, haladjon tovább
                continue
            jatektabla[sor][oszlop]="x" #tegye is oda az aknát
            lerakottaknak+=1
        return jatektabla
    
    def ertek_rendeles_a_tobbi_mezohoz(self):
        #itt rendeljük az értékeket a többi mezőhöz, amikkel megtudhatjuk hány szomszédos akna
        #van a közelben
        for s in range(self.palyameret): #végig iterálok a sorokon
            for o in range(self.palyameret): #végig iterálok az oszlopokon
                if self.jatektabla[s][o]=="x":
                    continue #ha a mező alapból egy bomba, nem szeretnék semmit kezdeni vele
                self.jatektabla[s][o]=self.szomszedosaknak_szamanak_visszaadasa(s,o)
    
    def szomszedosaknak_szamanak_visszaadasa(self, sor, oszlop):
        #itt végig iterálunk az összes szomszédos mezőn, hogy megkapjuk az aknák számát
        szomszedosaknak=0
        for s in range(max(0, sor-1), min(self.palyameret-1, sor+1)+1): #végig iterálok az összes soron
            for o in range(max(0, oszlop-1), min(self.palyameret-1, oszlop+1)+1): #végig iterálok az összes oszlopon
                if s==sor and o==oszlop:
                    continue #az eredeti pozíciónk, ne vizsgálja
                if self.palyameret[s][o]=="x":
                    szomszedosaknak+=1
        return szomszedosaknak
    
    def asas(self, sor, oszlop):
        
        #ásson a megadott sor és oszlop koordinátán
        #ha sikeres az ásás, True-t adunk vissza, ha viszont akna, akkor False-ot
        #ha van szomszédos akna, akkor befejezzük az ásást, ha nincs, akkor kiássuk az üres mezőket körülötte, mint a játékban
        
        self.asas.add((sor, oszlop)) #gyakorlatilag nyilvántartjuk az ásásokat itt
        if self.jatektabla[sor][oszlop]=="x":
            return False #aknát ástunk
        elif self.jatektabla[sor][oszlop]>0:
            return True #nem aknát ástunk
        for s in range(max(0, sor-1), min(self.palyameret-1, sor+1)+1): 
            for o in range(max(0, oszlop-1), min(self.palyameret-1, oszlop+1)+1):
                if (s, o) in self.asas:
                    continue #ne ásson ott, ahol már történt ásás, ezeket a koordinátákat ugye a self.asas tartalmazza
    
                self.asas(s,o)
        return True
    
    def __str__(self):
        #ezzel a függvénnyel, ha meghívom a printet ebben az objektumban, kifogja printelni azt,
        #amit ez a függvény visszaad, tehát, vissza kell adni egy stringet, ami a pályát tartalmazza
        #a játékos számára
        
        #egy tömb ami megmutatja amit a játékos látni szeretne(fog)
        lathatopalya=[[None for _ in range(self.palyameret)] for _ in range(self.palyameret)]
        for sor in range(self.palyameret):
            for oszlop in range(self.palyameret):
                if (sor,oszlop) in self.asas:
                    lathatopalya[sor][oszlop]=str(self.jatektabla[sor][oszlop])#átalakítjuk a mezőt stringé, hogy majd kitudjuk printelni
                else:
                    lathatopalya[sor][oszlop]=" "
        #az egészet stringbe kell rakni, formázzuk meg a pályát
        stringvissza=''
        #kellenek a maximum szélességek a printeléshez
        szelessegek=[]
        for idx in range(self.palyameret):
            oszlopok=map(lambda x:[idx], lathatopalya)
            szelessegek.append(len(max(oszlopok, key=len)))
        
        #kiprinteljük a csv stringet
        indexek=[i for i in range(self.palyameret)]
        indexeksor="   "
        mezok=[]
        for idx, oszlop in enumerate(indexek):
            format="%-"+str(szelessegek[idx])+"s"
            mezok.append(format%(oszlop))
        indexeksor+="  ".join(mezok)
        indexeksor+="  \n"
        
        for i in range(len(lathatopalya)):
            sor=lathatopalya[i]
            stringvissza+=f'{i} I'
            mezok=[]
            for idx, oszlop in enumerate(sor):
                format='%-'+str(szelessegek[idx])+"s"
                mezok.append(format%(oszlop))
            stringvissza+=" I".join(mezok)
            stringvissza+=" I\n"
        
        stringhosszusag=int(len(stringvissza)/self.palyameret)
        stringvissza=indexeksor+"-"*stringhosszusag+"\n"+stringvissza+"-"*stringhosszusag
        return stringvissza
            
def jatek(palyameret=10, aknaszam=10):
    # első lépés: megycsinálni és megtervezni a bombákat
    jatektabla=JatekTabla(palyameret, aknaszam) #meghívom a táblát
    pass

    while len(jatektabla.asas) < jatektabla.palyameret ** 2 - aknaszam:
        # jó a 0,0 és a 0, 0 meg a 0,     0
        felh_input = re.split(',(\\s)*', input("Hol szeretne ásni? Irja be a sor és oszlopot! ")) # 1, 2
        sor , oszlop = int(felh_input[0]), int(felh_input[-1])
        if sor < 0  or sor >= jatektabla.palyameret or oszlop < 0 or oszlop >= palyameret:
            print("Rossz a hely! Írd be újra! ")
            continue

        biztonsag = jatektabla.asas(sor, oszlop)
        if not biztonsag:
            break # game over
    if biztonsag:
        print("Gratulálok nyertél!")
    else:
        print("Vesztettél!")
        jatektabla.asas = [{s,o} for s in range(jatektabla.palyameret) for o in range(jatektabla.dim_size)]
        print(jatektabla)
if __name__ == '__main__':
    jatek() 
#További feladatok a commit leírásban