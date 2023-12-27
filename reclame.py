from algemene_functies import mijn_functie_2

smaak = ["aardbei", "banaan", "citroen"]
prijs = 4
korting = 0.1
procent = korting * 100 * prijs / 100
prijs_nieuw = prijs - procent

def aanbieding_1(smaak,prijs,korting):
        if smaak == "aardbei" and prijs == 4 and korting == 0.1:
                uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs_nieuw} euro."
                return uitvoer

print(aanbieding_1("aardbei",4,0.1))


inkomsten = [220, 430, 125, 160, 205, 90, 345]
btw = 0.09

def inkomsten_totaal(inkomsten):
    totaal = 0
    bedrag = 0
    for nr in inkomsten:
        totaal += nr
        bedrag = btw * totaal / 1
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden."


mijn_lijst = [220, 430, 125, 160, 205, 90, 345]

def laag_en_hoog(mijn_lijst):
        return max(mijn_lijst), min(mijn_lijst)


mijn_lijst = [220, 430, 125, 160, 205, 90, 345]

def gemiddelde(mijn_lijst): 
        return f"De gemiddelde inkomsten deze week zijn {sum(mijn_lijst) / 7} euro."


invoer_lijst = [10,5,3,2,1,2,9]

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)


def combinatie(invoer_lijst_2):
     korte_lijst = laag_en_hoog(invoer_lijst_2)
     uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
     return uitvoer






    

    


