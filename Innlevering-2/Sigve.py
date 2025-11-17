def konflikt1():
    print("\nKonflikt 1")
    print("Hvordan håndtere konflikten mellom Silje og Sivert?")
    print("1. Komme til et kompromiss.")
    print("2. Ta ting opp i plenum.")
    print("3. Ignorere konflikten.")

    while True:
        valg = input("Velg 1, 2 eller 3: ")

        if valg == "1":
            print("\nKonsekvens: De blir enige etter å ha snkket sammen, og ting går bedre.")
            print("Poeng: 3\n")
            return 3

        elif valg == "2":
            print("\nKonsekvens: Konflikten løses, men det blir litt splittelser i teamet.")
            print("Poeng: 2\n")
            return 2

        elif valg == "3":
            print("\nKonsekvens: Konflikten blir større og teamet mister det.")
            print("Poeng: -1\n")
            return -1

        else:
            print("Ugyldig valg, prøv igjen.")


def konflikt2():
    print("\nKonflikt 2")
    print("Hvordan håndtere konflikten mellom Hambi og Jabir?")
    print("1. Høre med hele teamet (demokrati).")
    print("2. Ignorere konflikten.")
    print("3. Du tar beslutningen alene.")

    while True:
        valg = input("Velg 1, 2 eller 3: ")

        if valg == "1":
            print("\nKonsekvens: Flere perspektiver hjelper, teamfølelsen øker.")
            print("Poeng: 3\n")
            return 3

        elif valg == "2":
            print("\nKonsekvens: Problemet blir ikke noe bedre.")
            print("Poeng: -2\n")
            return -2

        elif valg == "3":
            print("\nKonsekvens: Rask løsning, men teamet føler seg overkjørt.")
            print("Poeng: 1\n")
            return 1

        else:
            print("Ugyldig valg, prøv igjen.")


def konflikt3():
    print("\nKonflikt 3")
    print("Hvordan bevare motivasjonen i teamet som helhet?")
    print("1. Alkohol og samhold.")
    print("2. 3 timers forelesning om kommunikasjon.")
    print("3. Bare streng disiplin.")

    while True:
        valg = input("Velg 1, 2 eller 3: ")

        if valg == "1":
            print("\nKonsekvens: Teamet hadde det veldig lættis, og føler de har blitt kjempe gode venner.")
            print("Poeng: 3\n") 
            return 3

        elif valg == "2":
            print("\nKonsekvens: Folk lærer noe nytt men det er de kjeder sog og blir demotiverte.")
            print("Poeng: 1\n") 
            return 1

        elif valg == "3":
            print("\nKonsekvens: Ingen føler seg hørt og motivasjonen faller heftig.")
            print("Poeng: -2\n") 
            return -2

        else:
            print("Ugyldig valg, prøv igjen.")


def main():
    

    total_poeng = 0

    total_poeng += konflikt1()
    total_poeng += konflikt2()
    total_poeng += konflikt3()

    print("\nRESULTAT")
    print("Totale poeng:", total_poeng)

    if total_poeng >= 7:
        print("Du håndterte konfliktene veldig godt og lagde et sterkt team.")
    elif total_poeng >= 3:
        print("Du håndterte konfliktene helt passe, men det er fortsatt mye som kan bli bedre.")
    else:
        print("Teamet har det ikke så bra... kanskje på tide å prøve noe nytt?")


main()

