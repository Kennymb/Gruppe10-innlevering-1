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



print("Velkommen til Erlings verden")
print("Du har laget en medborgersportal og skal nå utvikle teamet ditt.")
print("Det er flere konflikter som brygger og dine valg vil påvirke prosjektets suksess")
print()
print("Det er en grå morgen på kontoret. Humøret svinger og du er klar over hvordan teamet ikke er  på topp. I det du går inn døren til pause rommet hører du høylytte stemmer")
print("Silje sier til sivert 'Du er så ubrukelig og du stinker'. Du ser Sivert gå ut av rommet litt lei seg")
score = 0
konflikt="Silje og Sivert"

while True: #brukt while løkke slik at den hele tida skal sjekke videre
    if konflikt== "Silje og Sivert":
        print("Hvordan skal du løse konflikten? ")
        print("A) Snakk med begge og prøve å finne et felles forslag")
        print("B) Kall inn til et møte med en gang og snakk om konflikten")
        print("C) Ta deg en kopp kaffi")
        valg1= input().upper()

        if valg1 == "B":
            score+=25 #Dette er for å holde styr på valgets kosekvenser og det påvirker slutt resultatet
            print("*Du kaller inn til et møte*")
            print("Okei folkens, så vi har et problem vi må ta opp")
            print("Husk at vi skal holde en profesjonell oppførsel på jobb")
            print("*Siver og Silje rødmer av oppførselen sin*")
            print("*Teamet blir ikke no nærmere")
            print()
            
            konflikt="Hamdi og Jabir" #Her bytter du til neste konflikt
            continue #her er continue fordi i første omgang så ville den ikke sendes videre/bytte til neste konflikt

        elif valg1== "A":
            score+=100
            print("Du går bort til Silje og ber om å snakke med ho på kontoret")
            print("Du sier til Silje 'Jeg skjønner at ting er vanskelig akkurat nå, men kanskje vi kan prøve å komme til et kompromiss?'")
            print("Silje sier at hun forstår det hun gjorde var umodent og sier 'Jeg skal snakke med Sivert'")
            print("Litt senere setter du deg ned med Sivert og prøver å finne et kompromiss med han også")
            print("*Silje og Sivert blir venner igjen*")
            konflikt="Hamdi og Jabir"
            continue

        elif valg1== "C":
            score+=0
            print("Du går bort og tar deg en kopp kaffi, det er altfor tidlig å med drama nå")
            print("*Konflikten utvikler seg*")
            konflikt="Hamdi og Jabir"
            continue
        
        else:
            print("Velg et svar")
            konflikt="Silje og Sivert"



    if konflikt== "Hamdi og Jabir":
        print()
        print("Imens du snakker med Sivert så krangles det på andre siden av kontoret")
        print()
        print("Hamdi og Jabir er uenige om noe, men Erling får ikke vite det før senere")
        print("Neste dag har dere et møte der dere skal snakke om innbyggerens innflytelse")
        print("Hamdi sier 'Vi burde la dem bli med men på en kontrollert måte'")
        print("Jabir svarer med 'Norge er et fritt og demokratisk land vi burde stole på dem'")
        print("Du merker at spenningen går mot en klimaks og motivasjonen vil kræsje hvis du ikke gjør noe")
        print("Hva gjør du?")
        print("A)Tar et demokratisk valg")
        print("B)Ta deg en kopp kaffi")
        print("C)Ta et autoritært valg")
        valg2=input().upper() #Upper sånn at de kan lett skrive inn og det blir til stor bokstav 

        if valg2=="A":
            score+=50
            print("Da har vi enda et møte")
            print("Hamdi og Jabir er uenig om noe, så kan vi da stemme over hva folk synes er best")
            print("*Folk stemmer*")
            print("Ser ut som folk foretrekker å ha et kontrollert samarbeid med innbyggerne")
            print("*Jabir er ufornøyd - det er jo han som skal opprettholde dette forholdet med innbyggerne*")
            konflikt="Motivasjon"
            continue
        
        elif valg2=="B":
            score+=0
            print("'Jo da var det vel kaffi pause' sier du til deg selv")
            print("*konflikten utvikler seg*")
            print()
            
            konflikt="Motivasjon"
            continue
        elif valg2=="C":
            score+=50
            print("'Okay hvorfor mener du det er viktig med en åpen løsning Jabir' sier du")
            print("Jabir forklarer")
            print("'Okay jeg forstår, hva med deg Hamdi'sier du")
            print("Hamdi forklarer")
            print("Jeg forstår, jeg tror vi burde stole på innbyggerne våre")
            print("*Hamdi virker ufornøyd men stoler på din dømmekraft som leder*")
            konflikt="Motivasjon"
            continue
        else:
            print("Velg et riktig svar")
            konflikt="Hamdi og Jabir"
    
    if konflikt=="Motivasjon":
        print()
        print("Prosjektet er sluttfasen og teamet har mistet fokus, hvordan skal du få teamet til å bli mer samspleiset for å rekke fristen?")
        print()
        print("A)Du tar alle ut for en felles fest med 3 drikke bonger")
        print("B)Du tvinger alle inn på et 3 timers lang møte for å snakke om åpen kommuinkasjon")
        print("C)Motivasjon? Finnes bare disiplin")
        valg3=input().upper()
        
        if valg3=="A":
            score+=100
            print("Du tar med alle ut på en felles fest for at folk skal kommunisere på tvers av grupper")
            print("Du ser at alle koser seg og stemningen er høy")
            print("Dere ender opp på en karaoke bar")
            print("Selv om regninga var dyr har effektivtet økt med 100%")
            konflikt="Utfall"
            continue
        
        elif valg3=="B":
            score+=50
            print("Du får proffen kommunikasjons mester til å holde et foredrag som varer i 3 timer")
            print("Du ser at folk er interessert men mister fokus etter andre timen")
            print("Svært få fikk noe ut av foredraget og ting fortsetter slik som før")
            konflikt="Utfall"
            continue

        elif valg3=="C":
            score+=0
            print("Du er klar over at motivasjonen ikke er på topp, men du vet fra egen erfaring at dispilin er hva som drar et prosjekt framover")
            print("og som sjef, så vet jo du best")
            print("Spesielt Silje går rundt i chatrom og snakker om å bytte ut sjefen")
            konflikt="Utfall"
            continue
        else:
            print("Velg et riktig svar")
            konflikt="Motivasjon"
    
    if konflikt=="Utfall":
        print()
        print("*Prosjekter nærmer seg slutten*")
        print("Din valg har fått en totalsum som er:")
        print(score)
        if score>=250:
            print()
            print("Prosjektet går supert og dere blir ferdig i tide")
            break #slutte while løkken
        
        elif 150 <= score <=250:
            print()
            print("Prosjektet går helt greit, men du møter på flere utfordringer som er mentalt slitsomt")
            break
        
        elif 50<= score <= 150:
            print()
            print("Prosjektet går skeivs og dere må utsette fristen litt")
            break 
        else:
            print()
            print("Prosjektet faller sammen, kommunikasjonen svikter og alt blir forsinket")

            break
