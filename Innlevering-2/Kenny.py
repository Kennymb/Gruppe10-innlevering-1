#Story time - Erlings rolle som leder.
print("En dag kommer Erling inn på kontoret, hvor han møter på Silje og Sivert som har en konflikt.")
print("\nSilje sier: Du er så ubrukelig, og du stinker!!")
print("\nSivert blir stum og lei seg, før han stormer ut av kontoret")
print("\nErling lurer på hvem han skal prate med først.")
Hvem = input ("\nhva skal Erling gjøre: (1: Prate med silje / 2: Prate med Sivert)")
print()

if Hvem == "1":
    print("\nErling prater først med silje")
    print("Erling sier at personangrep ikke hører hjemme i prosjektarbeid, og ønsker at Silje finner et kompromiss")


elif Hvem == "2":
    print("\nErling løper etter Sivert")
    print("Han finner Sivert, og ønsker å høre hans side av saken")

print()
Valg = input("\nEtter en samtale med begge parter, så står Erling ovenfor 3 valg: \n1: Erling ber dem å finne et kompromiss \n2: Erling mekler sammen og ber \n3: Erling ignorerer konflikten")

Poengsum = 0

if Valg == "1":
    print("\nErling samler begge parter, og ber dem snakke ut")
    print("Silje og Sivert beklager seg selv, og forstår et sammerbeid er best for fellesskapet")
    Poengsum += 30

elif Valg == "2":
    print("\nErling kaller inn til et møte med begge parter")
    print("Meklingen fører til mer splittelse, og den private gruppechatten viser forakt til valget. Konflikten er fortsatt tilstede.")
    Poengsum += 10

elif Valg == "3":
    print("\nErling ignorerer konflikten")
    print("Uten innvending, så eskalerer personalkonflikten. Kommunikasjon stopper opp, og konflikten er ikke løst i det hele tatt.")
    Poengsum += 0

print()
print("\nI mellomtiden på andre siden av kontoret hører man et høyt smell. \nHamdi er oppgitt fordi Jabir ikke hører på hennes meninger. \nDet som startet som noe lite har eskalert til et større personalkonflikt.")
print("Hamdi mener at innbyggere skal delta gjennom en kontrollert løsning, \nMens Jabir ønsker en mer åpen løsning.")
print()
print("Erling er opptatt med Silje og Sivert, og får ikke med seg den nye konflikten, \nEtter noen team meetings, så skjønner Erling at det er noe konflikt hos Hamdi og Jabir.")
print()
Valg2 = input("\nHva skal Erling gjøre i denne situasjonen? \n1: Kjøre demokratisk og spør gruppa sin mening \n2: Selv velge et av alternativene \n3: Ignorere konflikten")

if Valg2 == "1":
    print("\nErling spør prosjekt teamet.")
    print("Teamet stemmer over forslagene, og Hamdi og Jabir ser det store bilde og arbeider sammen igjen.")
    Poengsum += 30

elif Valg2 == "2":
    print("\nErling tar på seg sjefsrollen, og bestemmer selv.")
    print("Det ender selfølgelig i missnøye hos en av partene, og den ene føler seg bedre enn den andre. \nTeamet arbeider igjen, men er fortsatt splittelse i personalet.")
    Poengsum += 10


elif Valg2 == "3":
    print("\nErling velger å ignorere, og håper konflikten går vekk av seg selv.")
    print("Teamet ender opp med å arbeide i forskjellig retning, og prosjektet stopper opp.")
    Poengsum += 0


if Poengsum >= 60:
    print("\nSLUTT BRA:")
    print("Erling har klart å løse konfliktene profesjonelt, teamet er tilbake til normal og prosjektet fortsetter som vanlig.")
    print("\nErling er fornøyd, å ønsker å ha en liten feiring.")
    Valg3 = input("\nHva skal Erling finne på? \n1: Samle alle på byen \n2: Bestille kake til kontoret \n3: Erling spanderer lunsj")

    if Valg3 == "1":
        print("\nAlle møtes på Markens, blir drita og teamets moral styrker")
    
    elif Valg3 == "2":
        print("\nErling bestiller kake, og teamet har en hyggelig pause på jobb.")
    
    elif Valg3 == "3":
        print("\nErling spanderer lunsj, og alle koser seg.")

elif 10 <= Poengsum <= 40:
    print("\nSlutt middels:")
    print("Konflikten er delvis løst, men det fortsatt spenning i gruppa som krever videre oppfølging.")
    print("\nErling ønsker å løse opp spenningen, hvordan skal han gjøre det?")
    Valg3 = input("\n1: Bestille yoga instruktør \n2: Dra på byen \n3: Erling spanderer lunsj")

    if Valg3 == "1":
        print("\nFolk er skeptisk til yoga, men etter timen føler teamet seg avslappet, men konfliktene er fortsatt der.")
    
    elif Valg3 == "2":
        print("\nErling inviterer teamet ut på byen, men det er tydelig sosial splittelse i gjengen.")
    
    elif Valg3 == "3":
        print("\nErling spanderer lunsj, men folk setter seg i forskjellige grupper, og konfliktene forblir.")

else:
    print("SLUTT DÅRLIG:")
    print("Erling løser ingen konflikter, og samarbeidet faller sammen. prosjektet stopper opp.")
    print("\nErling får sparken, og ender opp på NAV kontoret.")