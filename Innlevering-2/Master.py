# -------------------
# Gruppeinnlevering 1
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
            "C)Motivasjon? Finnes bare disiplin",
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
            "Spesielt Silje går rundt i chatrom og snakker om å bytte ut sjefen",
        ],  
    },
}
score = 0


def PotetErGodt(nøkkel):
    data = Dict[nøkkel]
    global score

    for linje in data["Spørsmål"]:
        print(linje)

    valg1= input().upper()
    if valg1 == "B":
        score += 25 
        for linje in data["Konsekvens1"]:
            print(linje)

    elif valg1== "A":
        score += 100
        for linje in data["Konsekvens2"]:
            print(linje)

    elif valg1== "C":
        score += 0
        for linje in data["Konsekvens3"]:
            print(linje)
        
    else:
        print("Velg et svar")

PotetErGodt("Konflikt1")

"""
def gyldige_svar (A,B,C):
    while True:
        if valg in gyldige_svar:
            return valg
        print("Velg et riktig valg: A, B eller C")

def konflikter(konflikt_data):
    print[spørsmål]
    valg=input().strip.uppercase()
    if valg== "A":
        print[Konsekvens1]
    elif valg=="B":
        print[Konsekvens2]
    elif valg=="C":
        print[Konsekvens3]"""