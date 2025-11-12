Path = 0
Dict = {
    "Konflikt1": {
        "action": (
            "Konflikt 1:\n"
            "Silje (UX/UI-designer) og Sivert (IT-rådgiver) har havnet i en stadig mer opphetet diskusjon "
            "om teknologi og designvalg. Det som startet som en faglig uenighet, har nå blitt personlig.\n"
            "Hvordan bør Erling håndtere situasjonen?"
        ),
        "options": [
            "Be Silje og Sivert sette seg ned sammen for å finne et kompromiss og minne dem på at målet er felles.",
            "Ta saken opp i plenum slik at hele teamet kan si hva de mener.",
            "Ignorere konflikten og håpe at de ordner opp på egen hånd."
        ],
        "Konsekvens": [
            "Begge blir hørt, og de finner en løsning de kan leve med. Stemningen i teamet blir bedre.",
            "Diskusjonen sklir fort ut. Noen tar parti, og stemningen i gruppa blir mer spent.",
            "Konflikten ligger og ulmer. Kommunikasjonen stopper nesten helt opp, men prosjektet fortsetter så vidt."
        ],
        "correct": 1
    },

    "Konflikt2": {
        "action": (
            "Konflikt 2:\n"
            "Hamdi (kulturavdelingen) vil bruke kommunens faste plattform for innbyggerdialog, "
            "mens Jabir (innbyggerforeningen) ønsker en mer åpen løsning med rom for spontane innspill.\n"
            "Hvordan bør Erling gripe inn før konflikten vokser?"
        ),
        "options": [
            "Ta det opp med hele gruppa og prøve å finne en løsning som kombinerer trygghet og åpenhet.",
            "La dem ordne det selv de er voksne folk.",
            "Ta en beslutning på egen hånd uten å involvere dem mer."
        ],
        "Konsekvens": [
            "Begge føler seg hørt, og teamet blir enige om en balanse mellom struktur og frihet. Tilliten styrkes.",
            "Konflikten forsvinner ikke, men blir liggende og ulme. Stemningen blir anspent.",
            "Den ene parten føler seg overkjørt, og motivasjonen synker. Løsningen holder kanskje teknisk, men ikke sosialt."
        ],
        "correct": 1
    },

    "Konflikt3": {
        "action": (
            "Konflikt 3:\n"
            "Etter flere runder med konflikter merker Erling at motivasjonen i teamet er lav. "
            "Folk virker slitne og distanserte.\n"
            "Hva kan han gjøre for å få opp humøret og samarbeidet igjen?"
        ),
        "options": [
            "Tvinge alle til å delta på en lang forelesning om kommunikasjon og samarbeid.",
            "Stramme inn på struktur og disiplin fokusere kun på resultater og leveranser.",
            "Arrangere en sosial kveld, som et julebord med faste plasser, for å skape bedre samhold og bryte ned små klikker."
        ],
        "Konsekvens": [
            "Folk får snakket sammen og blir bedre kjent. Stemningen løsner, og samarbeidet flyter lettere etterpå.",
            "Lite engasjement og tvungen stemning. Folk lærer kanskje noe, men det endrer ikke så mye i praksis.",
            "Stemningen blir enda mer anspent. Noen føler seg overkjørt, og det går utover motivasjonen."
        ],
        "correct": 3
    }
}
#Tester
def valg(diction_key, path):
    data = Dict[diction_key]

    print("\n" + data["action"])
    for i, option in enumerate(data["options"], start=1):
        print(f"{i}: {option}")

    while True:
        try:
            question = int(input("Hva skal gjøres? (Skriv nummer 1-3): "))
            if question == 1 or question == 2 or question == 3:
                break
            else:
                print("Ugyldig valg. Skriv 1, 2 eller 3.")
        except ValueError:
            print("Støtter kun nummer. Prøv igjen.")

    print("\nKonsekvens:", data["Konsekvens"][question - 1])

    if question == 1:
        path = 1
    elif question == 2:
        path = 2
    elif question == 3:
        path = 3

    return path, question

good = 0

Path, q1 = valg("Konflikt1", Path)
if q1 == Dict["Konflikt1"]["correct"]:
    good += 1

Path, q2 = valg("Konflikt2", Path)
if q2 == Dict["Konflikt2"]["correct"]:
    good += 1

Path, q3 = valg("Konflikt3", Path)
if q3 == Dict["Konflikt3"]["correct"]:
    good += 1

if good >= 2:
    print(
        "balansert interessene og levert en løsning kommunen har tillit til."
    )
elif good == 1:
    print(
        "Prosjektet blir levert, men med noen skader på tillit og samarbeid."
    )
else:
    print(
        "Konflikter og valg underveis fører til svak løsning og redusert tillit."
    )
