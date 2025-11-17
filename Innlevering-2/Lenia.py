# TEAM KONFLIKT - LENIA.py
# PROBLEM: Erling oppdager konflikt i temaet

# SOLUTION: Løs konflikten ved å bruke if, else og elif



def alternativ_losning_på_konflikten_mellom_silje_og_sivert():
    print("Hvordan kan vi løse denne konflikten mellom Silje og Sivert?")
    valg = input(
        "Skriv '1' for å komme til kompromiss, '2' for å ta det opp i plenum, eller '3' for å ignorere konflikten, og ta det senere: ")
    if valg == '1':
        print("Konsekvens: Begge parter blir hørt, og stemningen bedres.")
        poeng = 3
    elif valg == '2':
        print("Konsekvens: Ved å ta det opp i plenum, får vi flere perspektiver på saken, samtidig som det er ubehagelig å bli pekt ut.")
        poeng = 2
    else:
        print("Konsekvens: Konflikten skyves under teppet, dermed kun forverres, og kan komme på overflaten senere hvor de har knapp med tid.")
        poeng = 1
    print("Du har tjent", poeng, "poeng for denne løsningen.")

    return poeng


def alternativ_losning_mellom_hamdi_og_jabir():
    print("Hvordan håndtere konflikt mellom Hamdi og Jabir?")
    valg = input(
        "Skriv '1' for å høre med hele teamet, demokrati, '2' for å ignorere konflikten, eller '3' for at lederen tar en avgjørelse: ")
    if valg == '1':
        print("Konsekvens: Å brette ut konflikten for hele teamet kan føre til en mer demokratisk beslutningsprosess.")
        poeng = 3
    elif valg == '2':
        print("Konsekvens: Å ignorere konflikten kan føre til at den vokser og blir mer alvorlig, samtidig kan det føles godt i øyeblikket.")
        poeng = 2
    else:
        print("Konsekvens: Ingen får kommet med sine synspunkter, og dermed må bare godta lederens avgjørelse.")
        poeng = 1
    print("Du har tjent", poeng, "poeng for denne løsningen.")
    return poeng


def alternativ_losning_motivasjon_i_teamet():
    print("Hvordan kan vi øke motivasjonen i teamet?")
    valg = input(
        "Skriv '1' for alkohol og fest/samhold, '2' for å tvinge teamets medlemmer til 3 timers forelesning om kommunikasjon, eller '3' for tenke - hva er motivasjon? Finnes bare disiplin! : ")
    if valg == '1':
        print(
            "Konsekvens: Kulturelle aktiviteter kan styrke båndene mellom teammedlemmene.")
        poeng = 3
    elif valg == '2':
        print("Konsekvens: Regelmessige møter kan hjelpe med å holde alle på samme side, men kan også oppleves som tvang.")
        poeng = 2
    else:
        print("Konsekvens: Å ignorere konflikten kan føre til at den vokser og blir mer alvorlig, samtidig kan det føles godt i øyeblikket.")
        poeng = 1
    print("Du har tjent", poeng, "poeng for denne løsningen.")
    return poeng


def total_poengsum():
    poengsum = alternativ_losning_på_konflikten_mellom_silje_og_sivert() + alternativ_losning_mellom_hamdi_og_jabir(
    ) + alternativ_losning_motivasjon_i_teamet()
    print("Din totale poengsum er:", poengsum)
    if poengsum >= 8:
        print("Flott jobbet! Du har håndtert konfliktene på en utmerket måte, og teamet beveger seg ut av storming-fasen!")
    elif poengsum >= 4:
        print("Konflikten er på vei mot løsning, men det er fortsatt rom for forbedring- teamet er enda under storming-fasen.")
    else:
        print(
            "Teamet sliter enda - vurder å prøve andre tilnærminger til konfliktløsning.")

    return poengsum


total_poengsum()

