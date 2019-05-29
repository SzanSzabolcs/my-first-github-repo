from enum import Enum
from random import randint

#-----------------------------------------------------------------
# Függvény definíciók
# -----------------------------------------------------------------
def sorsol():
    targyak = ["balta", "páncél", "pajzs", "láda", "kard", "sisak"]
    index = randint(0, len(targyak) - 1)
    return targyak[index]

def pontszam(targylista):
    pontertekek = {
        "balta": 1,
        "páncél": 5,
        "pajzs": 3,
        "láda": 3,
        "kard": 4,
        "sisak": 2
    }

    osszpontszam = 0

    for targy in targylista:
        osszpontszam += pontertekek[targy]

    return osszpontszam

def kiir(targyak):
    for targy in targyak:
        print(targy)

def kiir_fejlett(targyak):
    pontertekek = {
        "balta": 1,
        "páncél": 5,
        "pajzs": 3,
        "láda": 3,
        "kard": 4,
        "sisak": 2
    }

    print("")
    print("Ezeket a targyakat szerezted:")

    for targy in targyak:
        print("    - " + targy + ": " + str(pontertekek[targy]))
    print("")
    print("Összpontszám: " + str(pontszam(targyak)))
    print("")

def nevvalasztas():
    nev = input("Add meg a neved! ")
    with open("nev.txt", 'w') as f:
        f.write(nev)
    return nev

def file_kiiras(filenev):
    with open(filenev, 'r') as f:
        tartalom = f.read()
    print(tartalom)

def nevolvasas():
    with open("nev.txt", 'r') as f:
        nev = f.read()
    return nev

def udvozlet():
    print("")
    print("------------------------")
    print("Üdvözöllek a játékomban!")
    print("------------------------")
    print("")
    print("Juss messzebb az erdőben!")
    print("")

def viszlat(megtett_tavolsag, gyujtott_arany):
    print("")
    print("-------------------------")
    print("Sajnos vége a játéknak...")
    print("-------------------------")
    print("")
    print("Megtett távolság: " + str(megtett_tavolsag))
    print("Gyűjtött arany:   " + str(gyujtott_arany))
    print("")

def aranyat_talaltal(uj_arany, osszes_arany):
    osszes_arany += uj_arany

    print("")
    print("Megbotlasz valamiben...")
    print("Lenézel a lábad elé...")
    print("Találtál " + str(uj_arany) + " aranyat!")
    print("Most " + str(osszes_arany) + " aranyad van.")

    return osszes_arany

def csapdara_leptel(osszes_elet):
    osszes_elet -= 1

    if osszes_elet == 0:
        print("Sajnos meghaltál!")
    else:
        print("Csapda! Már csak " + str(osszes_elet) + " életed van!")

    return osszes_elet


class Irany(Enum):
    SEMERRE = 0
    BALRA = 1
    JOBBRA = 2
    FEL = 3
    LE = 4