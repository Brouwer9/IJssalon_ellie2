from helper import decoreer1

def print_aanbieding(): 
    mijn_prijzen = {"aardbei" : 3, "vanille" : 4, "chocolade" : 5}
    aanbieding = mijn_prijzen["aardbei"] * 0.8
    reclame_tekst = f"vandaag in de aanbieding: aardbei-ijs, 1 liter - slecht €{aanbieding}"
    reclame_tekst2 = reclame_tekst[:63]
    reclame_tekst3 = reclame_tekst2.upper()
    reclame_tekst4 = reclame_tekst3.split()
    print(reclame_tekst4)
    for el in reclame_tekst4:
        if len(el) > 4:
            print(el.upper())
        else:
            print(el.lower())

decoreer1 ("Aanbieding")
print_aanbieding()
