import threading
import time
import os
import subprocess

def visa_main():
    subprocess.run([os.sys.executable, "main.py"])

tjänstefrekvens_per_sekund = 1
arbeteTjänare = 0
afk_startad = False

def läs_banksaldo():
    try:
        with open('banksaldo.txt', 'r') as fil:
            banksaldo = float(fil.read())
    except FileNotFoundError:
        banksaldo = 0.0
    return banksaldo

def skriv_banksaldo(banksaldo):
    with open('banksaldo.txt', 'w') as fil:
        fil.write(str(banksaldo))

def visa_förtjänst():
    global arbeteTjänare
    print(f"Du har tjänat totalt {arbeteTjänare:.2f} kr under arbete.")

def tjäna_pengar_under_afk():
    global afk_startad
    global arbeteTjänare

    while afk_startad:
        banksaldo = läs_banksaldo()

        banksaldo += tjänstefrekvens_per_sekund
        arbeteTjänare += tjänstefrekvens_per_sekund

        skriv_banksaldo(banksaldo)

        time.sleep(1)

    print("Du har slutat tjäna pengar medan du är borta.")

def huvud():
    global afk_startad

    while True:
        användar_input = input("""
Skriv 'ARBETA' för att arbeta 
Skriv 'SLUTA ARBETA' för att avsluta
Skriv 'TJÄNAT' för att visa ackumulerad förtjänst
Skriv 'Backa' för att gå tillbaka till huvudsidan
>""")

        if användar_input.lower() == 'backa':
            visa_main()

        if användar_input.lower() == 'arbeta':
            if not afk_startad:
                afk_startad = True
                print("Du är nu i AFK-läge. Du kommer tjäna pengar medan du är borta.")
                threading.Thread(target=tjäna_pengar_under_afk, daemon=True).start()
            else:
                print("Du är redan i AFK-läge.")
        elif användar_input.lower() == 'sluta arbeta':
            if afk_startad:
                afk_startad = False
                print("Du har slutat tjäna pengar medan du är borta.")
            else:
                print("Du är inte i AFK-läge.")
        elif användar_input.lower() == 'tjänat':
            visa_förtjänst()
        else:
            print("Ogiltig kommando. Skriv 'arbeta' för att starta, 'sluta arbeta' för att sluta, eller 'tjänat' för att visa hur mycket du har tjänat.")

if __name__ == "__main__":
    huvud()
