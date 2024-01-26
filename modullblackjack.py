import random

def nämn():
    # Tar spelarens namn som input och välkomnar spelaren till blackjack.
    spelare = input("Vad heter du som ska spela? ") 
    print(f"Välkommen till blackjack, {spelare}")

nämn()

def skapa_kortlek():
    # Skapar och blandar en kortlek bestående av kortnummer och kortfärger.
    kortnummer = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    kortfärger = ['Hjärter', 'Ruter', 'Klöver', 'Spader']
    kortlek = [{'nummer': nummer, 'färg': färg} for nummer in kortnummer for färg in kortfärger]
    random.shuffle(kortlek)
    return kortlek

def räkna_poäng(hand):
    # Beräknar poängen för en given hand med blackjack-reglerna.
    poäng = 0
    ess_räknare = 0

    for kort in hand:
        if kort['nummer'] in ['K', 'Q', 'J']:
            poäng += 10
        elif kort['nummer'] == 'A':
            ess_räknare += 1
            poäng += 11
        else:
            poäng += int(kort['nummer'])

    # Justerar poängen om det finns ess i handen.
    while poäng > 21 and ess_räknare:
        poäng -= 10
        ess_räknare -= 1

    return poäng

def visa_hand(hand):
    # Visar korten i en given hand.
    for kort in hand:
        print(f"{kort['nummer']} av {kort['färg']}", end='  ')

def uppdatera_banksaldo(banksaldo):
    # Uppdaterar banksaldot genom att skriva det till en textfil.
    with open('banksaldo.txt', 'w') as fil:
        fil.write(str(banksaldo))

def läs_banksaldo():
    # Läser banksaldot från en textfil eller ger ett standardvärde om filen inte finns.
    try:
        with open('banksaldo.txt', 'r') as fil:
            banksaldo = float(fil.read())
    except FileNotFoundError:
        banksaldo = 1000.0  # Om filen inte finns, använd ett standardvärde (1000 i det här fallet)
    return banksaldo

def blackjack():
    # Huvudfunktionen för blackjack-spelet.
    banksaldo = läs_banksaldo()
    satsning = float(input("Hur mycket vill du satsa? "))

    if satsning > banksaldo:
        print("Du har inte tillräckligt med pengar för den insatsen.")
        return

    kortlek = skapa_kortlek()

    spelare_hand = [kortlek.pop(), kortlek.pop()]
    dator_hand = [kortlek.pop(), kortlek.pop()]

    # Spelaromgång där spelaren kan ta fler kort eller stanna.
    while True:
        spelare_poäng = räkna_poäng(spelare_hand)
        dator_poäng = räkna_poäng(dator_hand)

        # Visar spelarens hand och poäng.
        print("\nDin hand:")
        visa_hand(spelare_hand)
        print(f"\nPoäng: {spelare_poäng}")

        # Hanterar olika scenarier baserat på spelarens poäng.
        if spelare_poäng == 21:
            print("Grattis!, Du har Blackjack!")
            banksaldo += satsning + satsning * 1.5  # Insats + 1.5 gånger satsningen vid blackjack
            break
        elif spelare_poäng > 21:
            print("Du har förlorat. Över 21 poäng.")
            banksaldo -= satsning
            break

        # Frågar om spelaren vill ta ett till kort eller stanna.
        val = input("Vill du ta ett till kort? (ja/nej): ").lower()

        if val == 'ja':
            spelare_hand.append(kortlek.pop())
        else:
            break

    # Datorns tur att dra kort tills poängen når minst 17.
    while dator_poäng < 17:
        dator_hand.append(kortlek.pop())
        dator_poäng = räkna_poäng(dator_hand)

    # Visar datorns hand och poäng.
    print("\nDatorns hand:")
    visa_hand(dator_hand)
    print(f"\nDatorns poäng: {dator_poäng}")

    # Avgör vinnare och uppdaterar banksaldo.
    if dator_poäng > 21:
        print("Datorn har över 21 poäng. Du vinner!")
        banksaldo += satsning
    elif spelare_poäng > dator_poäng:
        print("Grattis! Du vinner!")
        banksaldo += satsning  # Lägg till insatsen i banksaldot vid vinst
    elif spelare_poäng < dator_poäng:
        print("Du förlorar. Datorn vinner.")
        banksaldo -= satsning  # Minska banksaldot med insatsen när spelaren förlorar
    else:
        print("Det blev oavgjort. Du behåller din insats.")

    # Visar det nya banksaldot och uppdaterar textfilen.
    print(f"Ditt nya banksaldo är: {banksaldo}")
    uppdatera_banksaldo(banksaldo)

if __name__ == "__main__":
    blackjack()
