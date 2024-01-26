# Importera nödvändiga bibliotek
import subprocess
import os

# Funktion för att visa bankmenyn
def visa_bank():
    # Använd subprocess för att köra bankmenyn från en annan fil (bankkonto.py)
    subprocess.run([os.sys.executable, 'bankkonto.py'])

# Funktion för att visa jobbmenyn
def visa_jobb():
    # Använd subprocess för att köra jobbmenyn från en annan fil (jobb.py)
    subprocess.run([os.sys.executable, 'jobb.py'])

def visa_bj():
    subprocess.run([os.sys.executable, "modullblackjack.py"])

# Huvudfunktion för att visa huvudmenyn
def huvudmeny():
    # Skriv ut välkomstmeddelande och menyinstruktioner
    print("""
########    ###    ######## #### ##    ## #########  ##         ##       #### ######## ########
##    ##   ## ##   ##    ##  ##  ###   ## ##     ##  ##    ##   ##        ##  ##       ##
##        ##   ##  ##        ##  ####  ## ##     ##  ##    ##   ##        ##  ##       ##
##       ##     ##  #####    ##  ## ## ## ##     ##  ##    ##   ##        ##  ######   ######
##       ##     ##     ###   ##  ## ## ## ##     ##  ##    ##   ##        ##  ##       ##
##       #########       ##  ##  ##  #### ##     ##  ########   ##        ##  ##       ##
##    ## ##     ## ##    ##  ##  ##   ### ##     ##        ##   ##        ##  ##       ##
######## ##     ## ######## #### ##    ## #########        ##   ######## #### ##       ######## 

    Välkommen till CASINO 4 LIFE""")

    # Huvudloopen som väntar på användarinmatning
    while True:
        start = input("""\nINSTRUKTIONER 
---------------------------------------------------------------------------------
|         1         |         2         |         3         |         4         |        
|      AVSLUTA      |     BANKKONTO     |       JOBB        |    BLACK JACK     |                     
|                   |                   |                   |                   |                     
|                   |                   |                   |                   |                       
|--------------------------------------------------------------------------------                                                               
SKRIV HÄR >""")
        
        # Kontrollera användarinmatning och vidta åtgärder baserat på valet
        if start == "1":
            break
        elif start == "2":
            visa_bank()
        elif start == "3":
            visa_jobb()
        elif start == "4":
            visa_bj()
        else:
            print("VÄLJ BARA MELLAN 1,2,3,4")

# Kör huvudfunktionen när skriptet körs
if __name__ == "__main__":
    huvudmeny()
