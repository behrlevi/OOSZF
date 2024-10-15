import time
from datetime import date
from osztalyok import *

# # # Kódolt adatok # # #

# Kölcsönzők példányosítása
Gyor = Kolcsonzo("Győr")
Budapest = Kolcsonzo("Budapest")
Debrecen = Kolcsonzo("Debrecen")

# Autók példányosítása
Audi_A8 = Szemely("ABC123","Audi","A8",20000,200,5)
Ford_Transit = Teher("CBA456","Ford","Transit",15000,800,"B")

# Autók regisztrálása az egyes kölcsönzőkbe
Gyor.reg(Audi_A8)
Gyor.reg(Ford_Transit)
Budapest.reg(Audi_A8)
Budapest.reg(Ford_Transit)
Debrecen.reg(Audi_A8)
Debrecen.reg(Ford_Transit)

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

# Bérlés
print ("\nÍrja be a bérelni kívánt autó sorszámát!\n")
avalaszt = input("Sorszám: ")
nvalaszt = input("\nÍrja be a napok számát! ")
vauto = Szemely(avalaszt)
print (vauto)
#berlet = Berles(vauto,date.today(),int_nvalaszt)
#print (berlet)


#print (berlet)
#print(f"Bérlés ára: {berles1.uj()} Forint")
