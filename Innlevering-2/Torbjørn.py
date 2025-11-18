# Erling må håndtere konflikt

print("Erling oppdager konflikt i teamet.\n")


# valg 1----------
# Viser(print) tekst som forklarer situasjon med 3 valgmuligheter med å velge 1,2 og 3. \n for linjeskifte
# Bruker if, elif, else statement(setning). Setter poeng basert på valg(Input) 1,2 og 3. eller ugyldig valg.
print("Silje og Sivert har begynt å bli frekke med hverandre på grunn av uenigheti prosjektet.""\n"
"Nå krangler de ikke om prosjekt unenigheter, men kaster bare stygge ord mot hverandre",
      "\n","Beslutning 1: Hvordan håndtere konflikt mellom Silje og Sivert?", 
      "\n","1: Komme til kompromiss", 
      "\n","2: Ta ting opp i plenum",
      "\n","3: Ignorere konflikten")

valg1 = input("Skriv valg (1/2/3): ")

if valg1 == "1":
    konsekvens1 = "Du forsøker å megle og finner et kompromiss."
    poeng1 = 2
elif valg1 == "2":
    konsekvens1 = "Konflikten tas opp i plenum. Gruppepress løser det delvis."
    poeng1 = 1
elif valg1 == "3":
    konsekvens1 = "Konflikten vokser og påvirker samarbeidet."
    poeng1 = -1
else:
    konsekvens1 = "Ugyldig valg."
    poeng1 = 0

print("\nKonsekvens:", konsekvens1)
print("Poeng:", poeng1, "\n")



# valg 2----------
# Viser(print) tekst som forklarer situasjon med 3 valgmuligheter med å velge 1,2 og 3. \n for linjeskifte
# Bruker if, elif, else statement(setning). Setter poeng basert på valg(Input) 1,2 og 3. eller ugyldig valg.
print("Hambi og Jabir er uenig med hverandre angående prosjektet.",
      "\n","Beslutning 2: Hvordan håndtere konflikt mellom Hambi og Jabir?", 
      "\n","1: Høre med hele teamet (demokrati)", 
      "\n","2: Ignorere konflikten",
      "\n","3: Du tar et valg")


valg2 = input("Skriv valg (1/2/3): ")

if valg2 == "1":
    konsekvens2 = "Teamet føler eierskap til avgjørelsen."
    poeng2 = 2
elif valg2 == "2":
    konsekvens2 = "Konflikten forverres."
    poeng2 = -1
elif valg2 == "3":
    konsekvens2 = "Du tar en upopulær avgjørelse, men konflikten stoppes."
    poeng2 = 1
else:
    konsekvens2 = "Ugyldig valg."
    poeng2 = 0

print("\nKonsekvens:", konsekvens2)
print("Poeng:", poeng2, "\n")



# valg 3----------
# Viser(print) tekst som forklarer situasjon med 3 valgmuligheter med å velge 1,2 og 3. \n for linjeskifte
# Bruker if, elif, else statement(setning). Setter poeng basert på valg(Input) 1,2 og 3. eller ugyldig valg.
print("Ooo nei! motivasjonen på teamet dropper, hva bør Erling gjøre",
      "\n","Beslutning 3: Hvordan bevare motivasjonen i teamet som helhet?", 
      "\n","1: Alkohol og samhold", 
      "\n","2: Tvinge til 3 timers forelesning om kommunikasjon",
      "\n","3: Hva er motivasjon? Finnes bare disiplin")


valg3 = input("Skriv valg (1/2/3): ")

if valg3 == "1":
    konsekvens3 = "Teamet får det gøy, men produktiviteten faller neste dag."
    poeng3 = 2
elif valg3 == "2":
    konsekvens3 = "Folk lærer noe, men blir slitne og demotiverte."
    poeng3 = -1
elif valg3 == "3":
    konsekvens3 = "Du høres streng ut. Noen liker det, andre ikke."
    poeng3 = 1
else:
    konsekvens3 = "Ugyldig valg."
    poeng3 = 0

print("\nKonsekvens:", konsekvens3)
print("Poeng:", poeng3, "\n")



# Resultat----------
# Kalkulerer sammen poeng fra valg 1,2 og 3.
# Deretter presenterer et resultat basert på sammensatt poeng

total = poeng1 + poeng2 + poeng3

print("----------")
print("RESULTAT")
print("Total poengsum:", total)

if total > 4:
    print("Fantastisk! Teamet ditt fungerer veldig bra.")
elif total > 2:
    print("Ikke verst! Det går greit, men det finnes forbedringsmuligheter.")
else:
    print("Teamet sliter. Kanskje vurder en annen lederstil?")