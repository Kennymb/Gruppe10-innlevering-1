# -------------------
# Gruppeinnlevering 2
# -------------------

# -------------------------------
# Group number and student names:
# -------------------------------
# Group 10

# Emma Moland Leiknes, emmaml@uia.no

# Kenny Minh Bui, Kennymb@uia.no 

# Lenia Barzan, Leniab@uia.no

# Lucas Fjeld, lucasf@uia.no 

# Sigve Sørensen, sigves@uia.no 

# Torbjørn Pedersen, torbjornp@uia.no

# Course Code & Name: IS-118 Programmering og prosjektsamarbeid

# Deliverable Title: Innleveringsoppgave 2

# Date: 28.Oktober 2025


#Introduksjon
print("Velkommen til Erlings verden")
print("Du har laget en medborgersportal og skal nå utvikle teamet ditt.")
print("Det er flere konflikter som brygger og dine valg vil påvirke prosjektets suksess")
print()
print("Det er en grå morgen på kontoret. Humøret svinger og du er klar over hvordan teamet ikke er  på topp. I det du går inn døren til pause rommet hører du høylytte stemmer")
print("Silje sier til sivert 'Du er så ubrukelig og du stinker'. Du ser Sivert gå ut av rommet litt lei seg")

Dict = { 
# Ordliste som inneholder alle tre konfliktene og valgmulighet. Grunne jeg valgte dette over lister er at jeg kan gjør alt på en variabel.
    "Konflikt1": {
        "Spørsmål": [
            "Hvordan skal du løse konflikten?", 
            "A) Snakk med begge og prøve å finne et felles forslag",
            "B) Kall inn til et møte med en gang og snakk om konflikten",
            "C) Ta deg en kopp kaffi",
        ],
        "Konsekvens1": [
            "*Du kaller inn til et møte*",
            "Okei folkens, så vi har et problem vi må ta opp",
            "Husk at vi skal holde en profesjonell oppførsel på jobb",
            "*Siver og Silje rødmer av oppførselen sin*",
            "*Teamet blir ikke no nærmere",
        ],
        "Konsekvens2": [
            "Du går bort til Silje og ber om å snakke med ho på kontoret",
            "Du sier til Silje 'Jeg skjønner at ting er vanskelig akkurat nå, men kanskje vi kan prøve å komme til et kompromiss?'",
            "Silje sier at hun forstår det hun gjorde var umodent og sier 'Jeg skal snakke med Sivert'",
            "Litt senere setter du deg ned med Sivert og prøver å finne et kompromiss med han også",
            "*Silje og Sivert blir venner igjen*",
        ],
        "Konsekvens3": [
            "Du går bort og tar deg en kopp kaffi, det er altfor tidlig å med drama nå",
            "*Konflikten utvikler seg*",
        ],
    },
    "Konflikt2": {
        "Spørsmål": [
            "Imens du snakker med Sivert så krangles det på andre siden av kontoret",
            "Hamdi og Jabir er uenige om noe, men Erling får ikke vite det før senere",
            "Neste dag har dere et møte der dere skal snakke om innbyggerens innflytelse",
            "Hamdi sier 'Vi burde la dem bli med men på en kontrollert måte'",
            "Jabir svarer med 'Norge er et fritt og demokratisk land vi burde stole på dem'",
            "Du merker at spenningen går mot en klimaks og motivasjonen vil kræsje hvis du ikke gjør noe",
            "Hva gjør du?",
            "A)Tar et demokratisk valg",
            "B)Ta deg en kopp kaffi",
            "C)Ta et autoritært valg",
        ],
        "Konsekvens1": [
            "Da har vi enda et møte",
            "Hamdi og Jabir er uenig om noe, så kan vi da stemme over hva folk synes er best",
            "*Folk stemmer*",
            "Ser ut som folk foretrekker å ha et kontrollert samarbeid med innbyggerne",
            "*Jabir er ufornøyd - det er jo han som skal opprettholde dette forholdet med innbyggerne*",
        ],
        "Konsekvens2": [
            "'Jo da var det vel kaffi pause' sier du til deg selv",
            "*konflikten utvikler seg*",
        ],
        "Konsekvens3": [
            "'Okay hvorfor mener du det er viktig med en åpen løsning Jabir' sier du",
            "Jabir forklarer",
            "'Okay jeg forstår, hva med deg Hamdi'sier du",
            "Hamdi forklarer",
            "Jeg forstår, jeg tror vi burde stole på innbyggerne våre",
            "*Hamdi virker ufornøyd men stoler på din dømmekraft som leder*",
        ],
    },
    "Konflikt3": {
        "Spørsmål": [
            "Prosjektet er sluttfasen og teamet har mistet fokus, hvordan skal du få teamet til å bli mer samspleiset for å rekke fristen?",
            "A)Du tar alle ut for en felles fest med 3 drikke bonger",
            "B)Du tvinger alle inn på et 3 timers lang møte for å snakke om åpen kommuinkasjon",
            "C)Motivasjon? Finnes bare disiplin!",
        ],
        "Konsekvens1": [
            "Du tar med alle ut på en felles fest for at folk skal kommunisere på tvers av grupper",
            "Du ser at alle koser seg og stemningen er høy",
            "Dere ender opp på en karaoke bar",
            "Selv om regninga var dyr har effektivtet økt med 100%",
        ],
        "Konsekvens2": [
            "Du får proffen kommunikasjons mester til å holde et foredrag som varer i 3 timer",
            "Du ser at folk er interessert men mister fokus etter andre timen",
            "Svært få fikk noe ut av foredraget og ting fortsetter slik som før",
        ],
        "Konsekvens3": [
            "Du er klar over at motivasjonen ikke er på topp, men du vet fra egen erfaring at dispilin er hva som drar et prosjekt framover",
            "og som sjef, så vet jo du best",
        ],  
    },
}
#Poengsystemet
score = 0
poeng = {
    "Konflikt1": {"A": 100, "B": 25, "C": 0},
    "Konflikt2": {"A": 100, "B": 0,  "C": 50},
    "Konflikt3": {"A": 100, "B": 50, "C": 0},
}

#tar i mot valg
def valgmottaker(nøkkel):
    data = Dict[nøkkel]
    global score

    for linje in data["Spørsmål"]:
        print(linje)
    
    while True: #While løkke hvis de skriver inn feil så vil den hele tida spørre til riktig svar før den går videre
        valg = input().upper()

        if valg in ("A", "B", "C"):
            score += poeng[nøkkel][valg]

            if valg == "A":
                for linje in data["Konsekvens1"]:
                    print(linje)

            elif valg== "B":
                for linje in data["Konsekvens2"]:
                    print(linje)

            elif valg== "C":
                for linje in data["Konsekvens3"]:
                    print(linje)
            break #to break out and continue if correct answer
        else:
            print("Velg et gyldig svar: A, B eller C")

#kjører koden gjennom alle konfliktene
valgmottaker("Konflikt1")
print("\n" + "-" *50) #linje for å vise skifte av scene
valgmottaker("Konflikt2")
print("\n" + "-" *50)
valgmottaker("Konflikt3")
print("\n" + "-" *50)

#De 3 utfallene basert på et poengsystem
print("*Prosjektet nærmer seg slutten*")
print("\n" + "-" *50)
if score>=250:
    print()
    print("Prosjektet går supert og dere blir ferdig i tide")
elif score >=150:
    print()
    print("Prosjektet går helt greit, men du møter på flere utfordringer som er mentalt slitsomt")     
else:
    print()
    print("Prosjektet går skeivs og dere må utsette fristen litt")

print("\n" + "-" *50)
print("Takk for at du spilte")