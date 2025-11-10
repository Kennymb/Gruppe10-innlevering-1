#Mulighet for å lett forandre teksten - skallet er ihvertfall på plass
print("Velkommen til Erlings verden")
print("Du har laget en medborgersportal og skal nå utvikle teamet ditt.")
print("Det er flere konflikter som brygger og dine valg vil påvirke prosjektets suksess")
print()
print("Det er en grå morgen på kontoret. Humøret svinger og du er klar over hvordan teamet ikke er  på topp. I det du går inn døren til pause rommet hører du høylytte stemmer")
print("Silje sier til sivert 'Du er så ubrukelig og du stinker'. Du ser Sivert gå ut av rommet litt lei seg")
score = 0
konflikt="Silje og Sivert"

while True:
    if konflikt== "Silje og Sivert":
        print("Hvordan skal du løse konflikten? ")
        print("A) Kjefte på Silje")
        print("B) Sette deg ned med begge to og snakke om det ")
        valg1= input().upper()

        if valg1 == "A":
            score-=25
            print("Du går bort til Silje og sier 'Du er en voksen dame, hva er du holder på, skjerp deg'")
            print("*Silje vil huske dette*")
            
            konflikt="Hamdi og Jabir"
            continue

        elif valg1== "B":
            score+=100
            print("Du går bort til Silje og ber om å snakke med ho på kontoret")
            print("Du sier til Silje 'Jeg skjønner at ting er vanskelig akkurat nå, men kanskje vi kan prøve å komme til et kompromiss?'")
            print("Silje sier at hun forstår det hun gjorde var umodent og sier 'Jeg skal snakke med Sivert'")
            print("Litt senere setter du deg ned med Sivert og prøver å finne et kompromiss med han også")
            print("*Silje og Sivert blir venner igjen*")
            konflikt="Hamdi og Jabir"
            continue


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
        print("A)Sier de skal fikse opp i det selv")
        print("B)Ta en autoritært valg")
        print("C)Høre begge sine sider")
        valg2=input().upper()

        if valg2=="A":
            score+=0
            print("Dette har vi ikke tid til, fiks opp i det selv og kom til en løsning")
            print()
            print("*Rommet blir stille*")
            print("Person kremter 'Ja skal vi snakke om fristen'")
            print()
            konflikt="Motivasjon"
            continue
        
        elif valg2=="B":
            score+=50
            print("'Ja men vi er jo et demokratisk land derfor bestemmer jeg å inkludere menneskene i en åpen løsning")
            print("'Likevel er det viktig at det er litt kontroll derfor gjør vi dette...'")
            print("Hamdi sitt fjes sier at han ikke er helt fornøyd, mens Jabir er litt usikker på hvordan det her skal fungere")
            konflikt="Motivasjon"
            continue
        elif valg2=="C":
            score+=100
            print("'Okay hvorfor mener du det er viktig med en åpen løsning Jabir' sier du")
            print("Jabir forklarer")
            print("'Okay jeg forstår, hva med deg Hamdi' sier du")
            print("Hamdi forklarer")
            print("Jeg forstår, er det en mulighet for å bruke begge disse ideene?")
            print("*Møtet fortesetter med en åpen diskusjon for å komme fram til en felles løsning*")
            konflikt="Motivasjon"
            continue
    
    if konflikt=="Motivasjon":
        print()
        print("Prosjektet er sluttfasen og teamet har mistet fokus, hvordan skal du få teamet til å bli mer samspleiset for å rekke fristen?")
        print()
        print("A)Du tar alle ut for en felles fest med 3 drikke bonger")
        print("B)Du tvinger alle inn på et 3 timers lang møte for å snakke om åpen kommuinkasjon")
        print("C)Du gjør ingenting siden det er snart frist uansett")
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
            score+=25
            print("Ting fortsetter som før og siden du ikke har tatt noe initiativ for å fobedre ting stiger misnøyen")
            print("Spesielt Silje går rundt i chatrom og snakker om å bytte ut sjefen")
            konflikt="Utfall"
            continue
    
    if konflikt=="Utfall":
        print()
        print("*Prosjekter nærmer seg slutten*")
        print("Din valg har fått en totalsum som er:")
        print(score)
        if score>=250:
            print()
            print("Prosjektet går supert og dere blir ferdig i tide")
            break
        
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
