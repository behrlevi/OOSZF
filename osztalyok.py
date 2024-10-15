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


class Teher(Auto):
    def __init__(self,rendszam,marka,tipus,dij,rakter,kat):
        super().__init__(rendszam,marka,tipus,dij)
        self.rakter = rakter
        self.kat = kat

class Kolcsonzo:
    def __init__(self,nev,):
        self.nev = nev
        self.autok = []
    def ujauto(self,auto):
        self.autok.append(auto)
    def listazas(self):
        return [auto.adat() for auto in self.autok]