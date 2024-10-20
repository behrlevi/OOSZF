import time
from datetime import date, datetime, timedelta
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

# A bérléseket tartalmazó tábla létrehozása és feltöltése alapértelmezett adatokkal a feladatkiírás alapján
berlesek=[]
berlesek.append(Berles(Audi_A8,date(2024,5,18),2))
berlesek.append(Berles(Audi_TT,date(2024,6,20),1))
berlesek.append(Berles(Ford_Transit,date(2024,9,15),5))
berlesek.append(Berles(VW_Krafter,date(2024,10,19),7))

# # # Felhasználói felület # # #
while True:
# Fő menü
    print("Üdvözöljük a kölcsönzőrendszerben!\n")
    print("1. Foglalás indítása\n2. Aktuális foglalások megtekintése\n3. Foglalás lemondása")
    fomenu=input(": ")
    if fomenu=="2":
        print("\n")
        for berles in berlesek:
            print(f"{berles}\n")
        time.sleep(2)
        print("\n\n\n\n")
        continue
    elif fomenu=="3":
        print("Melyik foglalást szeretné lemondani?")
        for index, berles in enumerate(berlesek, start=1):
            print(f"{index}. {berles}")
        lemond=input(": ")
        if berlesek[int(lemond)-1].datum <= date.today() <= berlesek[int(lemond)-1].datum + timedelta(days=berlesek[int(lemond)-1].napok):
            print("Folyamatban lévő foglalást nem lehet lemondani.")
            time.sleep(2)
        else:
            try:
                berlesek.pop(int(lemond)-1)
                print(f"A(z) {int(lemond)}. foglalás sikeresen lemondva.")
                time.sleep(2)
            except:
                print("Hibás foglalási azonosító.") # Csak létező foglalást lehet lemondani.
    elif fomenu=="1":
# Telephely kiválasztása
        vlsz = False
        while vlsz == False:
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
# Gépjárműadatok megtekintése vagy továbblépés a foglaláshoz.
        berles=False
        while berles == False:
            print("\n")
            print("Egy adott gépjármű részletes adatainak megtekintéséhez írja be a sorszámát.")
            print("Ha tovább szeretne lépni a foglaláshoz, üsse le az Enter billentyűt.")
            bovebb=input(": ")
            if bovebb.isnumeric():
                try:
                    print(autok[int(bovebb)-1].adatok())
                    time.sleep(2)
                except:
                    print("Nincs ilyen jármű az adatbázisban.")
                    time.sleep(2)
            else:
                berles=True
# A foglalási adatok bekérése és a foglalás rögzítése
        print ("\nÍrja be a bérelni kívánt autó sorszámát!\n")
        sorszam = input("Sorszám: ")
        napok = input("\nHánya napra szeretne bérelni? ")
        if berlesek[int(sorszam)-1].datum <= date.today() <= berlesek[int(sorszam)-1].datum + timedelta(days=berlesek[int(sorszam)-1].napok):
            print("A jármű erre az időszakra nem foglalható.") # Az adott időszakra már lefoglalt jármű nem foglalható
        try:
            uj_berlet = Berles(autok[int(sorszam)-1],date.today(),int(napok))
        except:
            print("Adja meg a bérlés időtartamát napokban.")
        berlesek.append(uj_berlet)
        print(uj_berlet)
        print(uj_berlet.vegosszeg())
        time.sleep(2)
        print("\n\n\n")

