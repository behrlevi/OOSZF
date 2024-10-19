import time
from datetime import date
from osztalyok import *

# # # Kódolt adatok # # #

# Kölcsönzők példányosítása
Gyor = Kolcsonzo("Győr")
Budapest = Kolcsonzo("Budapest")
Debrecen = Kolcsonzo("Debrecen")

# Autók példányosítása
Audi_A8 = Szemely("AAA111","Audi","A8",20000,505,4)
Audi_TT = Szemely("BBB222","Audi","TT",30000,300,2)
Ford_Transit = Teher("CCC333","Ford","Transit",15000,5,"B")
VW_Krafter = Teher("DDD444","Volkswagen","Krafter",25000,6.5,"C")

# Ebből a listából keresi ki a program a bérléskor választott autót.
# A megvalósítás hátránya, hogy kölcsönzőként eltérő készlet esetén minden telephely részére külön listát kellene létrehozni.
# Az egyszerűség kedvéért a jelen megvalósítás az összes telep esetén azonos járműválasztékot feltételez.
autok = [Audi_A8,Audi_TT,Ford_Transit,VW_Krafter]

# Autók regisztrálása az egyes kölcsönzőkbe
Gyor.reg(Audi_A8)
Gyor.reg(Audi_TT)
Gyor.reg(Ford_Transit)
Gyor.reg(VW_Krafter)
Budapest.reg(Audi_A8)
Budapest.reg(Audi_TT)
Budapest.reg(Ford_Transit)
Budapest.reg(VW_Krafter)
Debrecen.reg(Audi_A8)
Debrecen.reg(Audi_TT)
Debrecen.reg(Ford_Transit)
Debrecen.reg(VW_Krafter)

# # # Felhasználói felület # # #

# Telephely kiválasztása
vlsz = False
while vlsz == False:
    print("Üdvözöljük a kölcsönzőrendszerben\n\n")
    print("Írja be a kölcsönző kódját!\nTelephely      Kód\n\nGyőr           1\nBudapest       2\nDebrecen       3\n\n")
    kvalaszt=input("Telepkód: ")
    if kvalaszt == "1":
        lista = Gyor.listazas()
        print("A Győri kölcsönzőben jelenleg az alábbi autók elérhetőek:")
        for index,kocsi in enumerate(lista, start=1):
            print(f"{index}. {kocsi}")
            vlsz = True
    elif kvalaszt == "2":
        lista = Budapest.listazas()
        print("A Budapesti kölcsönzőben jelenleg az alábbi autók elérhetőek:")
        for kocsi in lista:
            print(kocsi)
            vlsz = True
    elif kvalaszt == "3":
        lista = Debrecen.listazas()
        print("A Debreceni kölcsönzőben jelenleg az alábbi autók elérhetőek:")
        for kocsi in lista:
            print(kocsi)
            vlsz = True
    else:
        print("Helytelen telepkód.")
        time.sleep(2)
        print("\n\n\n")

berles=False
while berles == False:
    print("\n")
    print("Egy adott gépjármű részletes adatainak megtekintéséhez írja be a sorszámát.")
    print("Ha tovább szeretne lépni a bérléshez, üsse le az Enter billentyűt.")
    bovebb=input(": ")
    if bovebb.isnumeric():
        try:
            print(autok[int(bovebb)-1].adatok())
        except:
            print("Nincs ilyen jármű az adatbázisban.")
            time.sleep(2)
    else:
        berles=True
# Bérlés
print ("\nÍrja be a bérelni kívánt autó sorszámát!\n")
sorszam = input("Sorszám: ")
napok = input("\nHánya napra szeretne bérelni? ")
uj_berlet = Berles(autok[int(sorszam)-1],date.today(),int(napok))
print(uj_berlet)
print("Köszönjük, hogy bennünket választott.")

