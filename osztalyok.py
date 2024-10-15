class Auto:
    def __init__(self,rendszam,marka,tipus,dij):
        self.rendszam = rendszam
        self.marka = marka
        self.tipus = tipus
        self.dij = dij

class Szemely(Auto):
    def __init__(self,rendszam,marka,tipus,dij,csomagter,ajtok):
        super().__init__(rendszam,marka,tipus,dij)
        self.csomagter = csomagter
        self.ajtok = ajtok
    def adatok(self):
        return f"Személyautó - Rendszám: {self.rendszam}, Márka: {self.marka}, Típus: {self.tipus}, Napidíj: {self.dij}."

class Teher(Auto):
    def __init__(self,rendszam,marka,tipus,dij,rakter,kat):
        super().__init__(rendszam,marka,tipus,dij)
        self.rakter = rakter
        self.kat = kat
    def adatok(self):
        return f"{self.marka} {self.tipus} teherautó - Rendszám: {self.rendszam}, Raktér: {self.rakter} m^2, Jog.kat.: {self.kat} Napidíj: {self.dij}."

class Kolcsonzo:
    def __init__(self,nev):
        self.nev = nev
        self.autok = []
    def reg(self,auto):
        self.autok.append(auto)
    def listazas(self):
        return [auto.adatok() for auto in self.autok]

class Berles(Kolcsonzo):
    def __init__(self,auto,datum,napok):
        self.auto = auto
        self.datum = datum
        self.napok = napok
        self.osszeg = self.auto.dij * self.napok
    def __str__(self):
        return f"Az aktuális bérlet teljes díja {self.osszeg} Forint"
    def uj(self):
        return self.auto.dij * self.napok