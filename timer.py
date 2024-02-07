import time
from menu import *

def LireTemps(txt):
    try:
        with open(f"timers\{txt}.txt", 'r') as fichier:
            temps = fichier.readline().strip()
            heures, minutes, secondes = map(int, temps.split(':'))
            return heures * 3600 + minutes * 60 + secondes
    except FileNotFoundError:
        print("name error")
        return 1

def LireTempsToEdit(txt):
    try:
        with open(f"timers\{txt}.txt", 'r') as fichier:
            temps = fichier.readline().strip()
            return temps
    except FileNotFoundError:
        print(f"{txt} n'existe pas")
        time.sleep(4)
        menu()
def StartTime(hours, minutes, seconds, txt):
    with open(f"timers\{txt}.txt", 'w') as fichier:
        fichier.write(f'{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}')

def EditTime(txt, time):
    with open(f"timers\{txt}.txt", 'w') as fichier:
        fichier.write(time)

def EcrireTemps(tempssec, txt):
    """Écrit le temps écoulé dans 'temps.txt' sous la forme hh:mm:ss."""
    heures, reste = divmod(tempssec, 3600)
    minutes, secondes = divmod(reste, 60)
    print(f"temps : {int(heures):02d}:{int(minutes):02d}:{int(secondes):02d}")
    with open(f'timers\{txt}.txt', 'w') as fichier:
        fichier.write(f'{int(heures):02d}:{int(minutes):02d}:{int(secondes):02d}')

def Chronometrer(txt):
    temps_debut = LireTemps(txt)
    debut = time.time() - temps_debut
    try:
        while True:
            temps_actuel = time.time() - debut
            EcrireTemps(temps_actuel, txt)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Chronomètre arrêté.")