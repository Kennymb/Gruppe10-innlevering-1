Dict = { 
# Ordliste som inneholder alle tre konfliktene og valgmulighet. Grunne jeg valgte dette over lister er at jeg kan gjør alt på en variabel.
    "Konflikt1": {
        "action": (
            "Silje og Sivert har havnet i en stadig mer opphetet diskusjon.\n"
            "Hvordan bør Erling håndtere situasjonen?"
        ),
        "options": [
            "Be Silje og Sivert finne et kompromiss og minne dem på felles mål.",
            "Ta saken opp i plenum for å få alle perspektiver.",
            "Ignorere konflikten og håpe den løser seg selv."
        ],
        "correct": 1
    },

    "Konflikt2": {
        "action": (
            "Hamdi vil bruke kommunens plattform, mens Jabir ønsker en mer åpen løsning.\n"
            "Hvordan bør Erling gripe inn?"
        ),
        "options": [
            "Ta saken med hele gruppa og finne en balansert løsning.",
            "La Hamdi og Jabir ordne opp selv.",
            "Bestemme løsningen alene uten videre dialog."
        ],
        "correct": 1
    },

    "Konflikt3": {
        "action": (
            "Teamet er slitent og motivasjonen er lav.\n"
            "Hva bør Erling gjøre?"
        ),
        "options": [
            "Holde en lang forelesning om samarbeid.",
            "Stramme inn struktur og kun fokusere på resultater.",
            "Arrangere en sosial kveld for å styrke relasjoner."
        ],
        "correct": 3
    }
}


# Denne funksjonen håndterer en konflikt om gangen. Den skriver ut teksten, viser
# alternativene og sørger for at brukeren velger et tall mellom 1 og 3. Til slutt
# returnerer den hvilket valg som ble tatt, slik at programmet kan sjekke om det var
# det korekte valget for historien.

def valg(key): 
    data = Dict[key]

    print( data["action"])
    for i, option in enumerate(data["options"], start=1):
        print(f"{i}: {option}")
   
    while True:
        try:
            question = int(input("Hva skal gjøres? (1-3): "))
            if question in (1, 2, 3):
                break
            print("Ugyldig valg. Skriv 1, 2 eller 3.")
        except ValueError: #Forhindrer at koden breaker hvis bruker skriver noe annet en int verdi
            print("Skriv et gyldig tall (1-3).")

    return question

good = 0  #Variabel for antall korrekte valg brukeren har tatt

#Introduksjon
print("Velkommen til Erlings verden")
print("Du har laget en medborgersportal og skal nå utvikle teamet ditt.")
print("Det er flere konflikter som brygger og dine valg vil påvirke prosjektets suksess")

#Konflikt 1 og konsekvens
quest1 = valg("Konflikt1")
if quest1 == Dict["Konflikt1"]["correct"]:
    good += 1

if quest1 == Dict["Konflikt1"]["correct"]:
    print("Stemningen mellom Silje og Sivert roer seg noe, og resten av teamet merker at du tar ansvar.")
else:
    print("Konflikten mellom Silje og Sivert henger i lufta, og flere i teamet blir mer usikre og stille.")

if quest1 != Dict["Konflikt1"]["correct"]:
    print("Den ulmende konflikten gjør at Hamdi og Jabir blir ekstra følsomme for urettferdighet i beslutninger.")

#Konflikt 2 og konsekvens
print()
quest2 = valg("Konflikt2")
if quest2 == Dict["Konflikt2"]["correct"]:
    good += 1

if quest2 == Dict["Konflikt2"]["correct"]:
    print("Etter møtet med Hamdi og Jabir opplever flere at du prøver å balansere ulike behov.")
else:
    print("Uenigheten mellom Hamdi og Jabir gjør at motivasjonen synker litt i gruppa.")

if good >= 2:
    print("Til tross for noen tøffe diskusjoner har teamet fortsatt tro på prosjektet.")
else:
    print("Flere konflikter er dårlig håndtert, og teamet er mer slitne enn før.")

#Konflikt 3 og avsluttning
print()
quest3 = valg("Konflikt3")
if quest3 == Dict["Konflikt3"]["correct"]:
    good += 1

print("\n Resultat")
if good >= 2:
    print("Erling balanserer interessene, teamet gjenoppretter tillit og får et bra resultat.")
elif good == 1:
    print("Prosjektet leveres, men konfliktene er bare delvis løst og relasjonene er sårbare noe som går utover kvaliteten.")
else:
    print("Konflikter fører til svak løsning, redusert tillit og forsinket prosjekt.")
