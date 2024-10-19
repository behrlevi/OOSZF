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
        return f"{self.marka} {self.tipus}, {self.ajtok} ajtós személyautó - Rendszám: {self.rendszam}, Csomagtér: {self.csomagter} liter, Napidíj: {self.dij}."

class Teher(Auto):
    def __init__(self,rendszam,marka,tipus,dij,rakter,kat):
        super().__init__(rendszam,marka,tipus,dij)
        self.rakter = rakter
        self.kat = kat
    def adatok(self):
        return f"{self.marka} {self.tipus} teherautó - Rendszám: {self.rendszam}, Raktér: {self.rakter} m^3, Jog.kat.: {self.kat} Napidíj: {self.dij}."

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
        return f"{self.auto.marka} {self.auto.tipus} bérelve {self.datum} időponttól {self.napok} napra."
    def vegosszeg(self):
        return f"A bérlet teljes díja: {self.osszeg} Forint"
