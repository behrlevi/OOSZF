import osztalyok
from osztalyok import *

# Kölcsönzők példányosítása
Gyor = Kolcsonzo("Győr")
Budapest = Kolcsonzo("Budapest")
Debrecen = Kolcsonzo("Debrecen")

# Autók példányosítása
Audi_A8 = osztalyok.Szemely("ABC123","Audi","A8",20000,200,5)
Ford_Transit = osztalyok.Teher("CBA456","Ford","Transit",15000,800,"B")

# Autók regisztrálása az egyes kölcsönzőkbe
Gyor.reg(Audi_A8)
Gyor.reg(Ford_Transit)

print("Üdvözöljük a kölcsönzőrendszerben\n\n")
print("Írja be a kölcsönző kódját!\nTelephely      Kód\n\nGyőr           1\nBudapest       2\nDebrecen       3\n\n")
kvalaszt=input("Telepkód: ")
if kvalaszt == "1":
    lista = Gyor.listazas()
    print("A Győri kölcsönzőben jelenleg az alábbi autók elérhetőek:")
    for kocsi in lista:
        print(kocsi)
if kvalaszt == "2":
    print(f"A Budapesti kölcsönzőben jelenleg az alábbi autók elérhetőek: {Budapest.listazas()}")
if kvalaszt == "3":
    print(f"A Debreceni kölcsönzőben jelenleg az alábbi autók elérhetőek: {Debrecen.listazas()}")


berlet = Berles(Audi_A8,"2024.10.15",2)
#print (berlet)
#print(f"Bérlés ára: {berles1.uj()} Forint")
