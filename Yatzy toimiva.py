import random
        
def aloitus() -> list:
    '''Tulostaa alkutervehdykset, palauttaa pelaajien nimet listana'''

    print("Heippa! Pelataan Yatzya!")
    print()

    players = int(input("Kuinka monta pelaajaa on mukana? (max 4): "))
    pelaajat = []

    i = 1
    while i <= players:
        name = input(f"{i}. pelaajan nimi? ")
        pelaajat.append(name) 
        i += 1
    return pelaajat

def luo_pistetaulukko(nimet: list) -> dict:
    '''Saa arvoksi pelaajien nimet ja palauttaa sanakirjan, jossa nimi (avain) ja aloituspisteet'''
    pisteet = {}
    for i in nimet:
        pisteet
        pisteet[i] = [0, 0, 0, 0, 0, 0, 0]
    return pisteet

def heita_kaikki() -> list:
    '''Antaa 5 satunnaista numeroa väliltä 1-6 listana ja tulostaa tulokset näytölle'''
    for j in range(5):
        a = random.choice(range(1, 7))
        arvot.append(a)
    print(f"Saamasi silmäluvut ovat:")
    print(f"1. noppa: {arvot[0]}")
    print(f"2. noppa: {arvot[1]}")
    print(f"3. noppa: {arvot[2]}")
    print(f"4. noppa: {arvot[3]}")
    print(f"5. noppa: {arvot[4]}")
    print(f"Eli {arvot}")
    print()
    return arvot

def heita_uudestaan(nopat: str):
    '''Pelaajan antamille "nopille" arvotaan uudet arvot'''
    for i in range(len(nopat)):
        for j in nopat[i]:
            j = int(j) - 1
            arvot[j] = random.choice(range(1, 7))
    print()
    print(f"Nyt silmälukusi ovat siis {arvot}")
    print()

def tallenna_tulokset(tulokset: list):
    '''Tallentaa vuoron lopuksi pelaajan pisteet pistetaulukkoon'''
    print()
    tulosta_pistetaulukko(x)
    osa = int(input("Mihin kohtaan haluaisit tallentaa pisteesi? "))
    if osa in (1,2,3,4,5,6):
        maara = osa * arvot.count(osa)
    elif osa == 7:
        if arvot[0] == arvot[1] == arvot[2] == arvot[3] == arvot[4]:
            maara = 50
        else:
            maara = 0
    lista = pistetaulu[x]
    lista[osa-1] = maara
    print()
    print("Nyt")
    tulosta_pistetaulukko(x)

def tulosta_pistetaulukko(pelaaja: str):
    '''Tulostaa annettua pelaajaa vastaavan pistetaulukon'''
    print(f"Pelaajan {pelaaja} pistetaulukko:")
    pisteet = pistetaulu[pelaaja]

    print(f"1. Ykköset:  {pisteet[0]}")
    print(f"2. Kakkoset: {pisteet[1]}")
    print(f"3. Kolmoset: {pisteet[2]}")
    print(f"4. Neloset:  {pisteet[3]}")
    print(f"5. Vitoset:  {pisteet[4]}")
    print(f"6. Kutoset:  {pisteet[5]}")
    print(f"7. Yatzy:    {pisteet[6]}")
    print(f"Yhteensä: {sum(pisteet)}")

def tallenna_peli():
    '''Tallentaa pelaajan tulokset tiedostoon'''
    with open("tulokset.txt", "a") as tiedosto:
        tulos = ""
        for x in osallistujat:
            tulos = tulos + x + " pisteet: " + str(sum(pistetaulu[x])) + "\n"
        tiedosto.write(tulos)


def vertaile_tuloksia():
    '''Tulostaa ruudulle tiedostoon talletetut tulokset'''
    for x in osallistujat:
        print(f"Pelaajan {x} loppupisteet olivat {sum(pistetaulu[x])}")

#Kirjoitetaan tähän itse ohjelma:
osallistujat = aloitus()
pistetaulu = luo_pistetaulukko(osallistujat)
print()

for i in range(7):
    for x in osallistujat:
        print(f"Sinun vuorosi pelata, {x}.")
        rolls = 3
        print(f"Tällä vuorolla heittoja on vielä jäljellä {rolls}")
        print()
        ro11 = input("Heitä nopat painamalla y. ")
        if ro11 == "y" or ro11 == "Y":
            arvot = []
            heita_kaikki()
            rolls = rolls - 1

            while rolls >0:
                print(f"Tällä vuorolla heittoja on jäljellä {rolls}.")
                print("Halutessasi voit heittää noppia uudelleen.")
                print()
                print("Anna uudelleen heitettävien noppien järjestysnumerot (esim '134').")
                print("0 - En heitä uudelleen")
                komento = input("Mitä haluat siis tehdä? ")
                if komento == "0":
                    rolls = 0
                else:
                    heita_uudestaan(komento)
                    rolls -= 1
            tallenna_tulokset(arvot)
        else:
            print()
            print("Et siis halua tehdä vuoroasi,")
            print("annetaanpa seuraavan pelaajan yrittää!")
            print()
print()
print("Huh, nyt peli on viimein pelattu.")
vertaile_tuloksia()
print()
jatko = input("Haluatko tallentaa pisteet tiedostoon? (y/n) ")
if jatko == "y":
    tallenna_peli()
    print("Pisteet on nyt tallennettu")
print("Tässä nykyiset pisteet!")
with open("tulokset.txt") as tiedosto:
    for rivi in tiedosto:
        print(rivi.strip())

print("Kiitos kun pelasit Yatzya!")
