import subprocess  # Importera subprocess för att köra andra Python-skript eller program
import os  # Importera os för att hantera operativsystemsfunktioner

class Bankkonto:
    # Metod för att visa banksaldot
    def visa_bankbalans(self):
        try:
            # Försök öppna filen 'banksaldo.txt' för läsning
            with open('banksaldo.txt', 'r') as fil:
                # Läs innehållet från filen
                innehall = fil.read()
                # Skriv ut innehållet i filen
                print(f"Du har totalt:\n{innehall} kr")
        except FileNotFoundError:
            # Om filen inte hittas, skriv ut ett meddelande om det
            print("Filen 'banksaldo.txt' finns inte.")

# Funktion för att visa huvudmenyn genom att köra main.py med subprocess
def visa_huvudmeny():
    subprocess.run([os.sys.executable, 'main.py'])

def huvudprogram():
    bank = Bankkonto()  # Skapa en instans av Bankkonto-klassen

    while True:
        # Användarinmatning för att välja mellan olika alternativ
        anvandar_inmatning = input("""
Skriv 'visa saldo' för att visa din saldo
Skriv 'backa' för att gå tillbaka

> """)

        # Hantera användarinmatningen och utför motsvarande åtgärder
        if anvandar_inmatning.lower() == 'visa saldo':
            bank.visa_bankbalans()
        elif anvandar_inmatning.lower() == 'backa':
            visa_huvudmeny()
            break
        else:
            print("Ogiltigt kommando. Vänligen skriv 'visa saldo', 'satt in' eller 'tillbaka'.")

if __name__ == "__main__":
    huvudprogram()  # Kör huvudprogrammet när filen exekveras
