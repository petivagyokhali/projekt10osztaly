import random
#először a pálya kinézete szükséges

def megjelenites():
    global n
    global aknaertekei
    
    print("\t\tAKNAKERESŐ JÁTÉK\n")
    
    #üres helyek a szebb kinézet miatt
    be="   "
    for i in range(n):
        be=be+"     "+str(i+1)
    print(be)
    
    #teteje,alja
    for s in range(n):
        be="     "
        if s==0:
            for oszlop in range(n):
                be=be+"______"
                
        #oldala      
        be="     "
        for oszlop in range(n):
            be=be+"I     "
        print(be+"I")
        
        #belső oldal
        be="  "+str(s+1)+"  "
        for oszlop in range(n):
            be=be+"I  "+str(aknaertekei[s][oszlop])+"  "
        print(be+"I")
        
        #sarkak
        be="     "
        for oszlop in range(n):
            be=be+"I_____"
        print(be+"I")
                
    
if __name__=="__main__":
    #mező mérete
    n=8
    aknaszam=8
    #mező valós értéke
    ertekek=[[0 for x in range(n)] for y in range(n)]
    #mező látszólagos értéke
    aknaertekei=[[" "for x in range(n)] for y in range(n)]
    zaszlok=[]
    
#aknák leplántálása:
def aknalerakas():
    count=0
    global aknaszam
    global n
    global ertekek
    
    while count<aknaszam:
        ert=random.randint(0, n*n-1)
        
        #az értékekből megcsináljuk a sorokat és oszlopokat
        s=ert//n
        oszlop=ert%n
        
        #lerakjuk az aknát, ha az nem tartalmaz azt. Az aknának -1 az értéke.
        if ertekek[s][oszlop]!=-1:
            count+=1
            ertekek[s][oszlop]=-1

#további rácsok értékeinek megadása:
def tobbibeallitasa():
    global n
    global ertekek
    
    #bejárjuk a mezőket hogy megnézzük az értékeiket
    for s in range(n):
        for oszlop in range(n):
            #menjen tovább ha a mező egy akna
            if ertekek[s][oszlop]==-1:
                continue
            
            #ellenőrizzük a szomszédos mezőt fent
            if s>0 and ertekek[s-1][oszlop]==-1:
                ertekek[s][oszlop]=ertekek[s][oszlop]+1
            #baloldalt
            if oszlop>0 and ertekek[s][oszlop-1]==-1:
                ertekek[s][oszlop]=ertekek[s][oszlop]+1
            #jobboldalt
            if oszlop<n-1 and ertekek[s][oszlop+1]==-1:
                ertekek[s][oszlop]=ertekek[s][oszlop]+1