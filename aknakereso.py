import random
#játéktábla osztály a pálya létrehozásához
class JatekTabla:
    def __init__(self, palyameret, aknaszam):
        self.palyameret=palyameret
        self.aknaszam=aknaszam
        self.jatektabla=self.ujpalyaletrehozasa()#az aknák lerakásához
        self.ertekrendelesatobbimezohoz()
        
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
    
    def ertekrendelesatobbimezohoz(self):
        #itt rendeljük az értékeket a többi mezőhöz, amikkel megtudhatjuk hány szomszédos akna
        #van a közelben
        for s in range(self.palyameret): #végig iterálok a sorokon
            for o in range(self.palyameret): #végig iterálok az oszlopokon
                if self.jatektabla[s][o]=="x":
                    continue #ha a mező alapból egy bomba, nem szeretnék semmit kezdeni vele
                self.jatektabla[s][o]=self.szomszedosaknakszamanakvisszaadasa(s,o)
    
    def szomszedosaknakszamanakvisszaadasa(self, sor, oszlop):
        #itt végig iterálunk az összes szomszédos mezőn, hogy megkapjuk az aknák számát
        szomszedosaknak=0
        for s in range(max(0, sor-1), min(self.palyameret-1, sor+1)+1): #végig iterálok az összes soros
            for o in range(max(0, oszlop-1), min(self.palyameret-1, oszlop+1)+1): #végig iterálok az összes oszlopon
                if s==sor and o==oszlop:
                    continue #az eredeti pozíciónk, ne vizsgálja
                if self.palyameret[s][o]=="x":
                    szomszedosaknak+=1
        return szomszedosaknak
    
            
def jatek(palyameret=10, aknaszam=10):
    pass