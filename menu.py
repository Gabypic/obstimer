import time
import os
from timer import *

def menu():
    print(f"Bienvenue dans ObsTimer ! \n"
          f"1. Lancer un timer au choix \n"
          f"2. Créer un timer \n"
          f"3. Afficher et changer le temps d'un timer \n"
          f"4. Liste des timers")
    choice = input("faites votre choix : ")
    if choice == "1":
        txt = input("Quel timer voulez vous lancer ? \n")
        print(f"Lancement du timer {txt}! ctrl+c to stop.")
        Chronometrer(str(txt))
        print("retour au menu")
        time.sleep(5)
        os.system('cls')
        menu()

    if choice == "2":
        i=0
        name = input("Quel nom souhaitez vous donner au timer ? \n")
        while i == 0:
            start_time = input("Quel temps de départ souhaitez vous lui donner (au format hh:mm:ss) ? \n")
            try :
                hours, minutes, seconds = map(int, start_time.split(':'))
                StartTime(hours, minutes, seconds, str(name))
                print(f"Le timer {name} avec pour temps de départ {start_time} a bien été créé \n\n")
                time.sleep(4)
                os.system('cls')
                menu()
            except:
                print(f"Erreur le forma de temps doit être hh:mm:ss \n")
                time.sleep(2)
                os.system('cls')

    if choice == "3":
        i = 0
        name = input("Quel timer voulez vous lire ? \n")
        txt_time = LireTempsToEdit(name)
        print(f"temps du timer {name} : {txt_time}.")
        choice_modif = input("Voulez vous le modifier o,n ? ")
        while i == 0:
            if choice_modif == "o":
                start_time = input("Quel temps de départ souhaitez vous lui donner (au format hh:mm:ss) ? \n")
                try:
                    hours, minutes, seconds = map(int, start_time.split(':'))
                    StartTime(hours, minutes, seconds, str(name))
                    print(f"Le timer {name} a bien été modifié au temps {start_time}")
                    time.sleep(4)
                    os.system('cls')
                    menu()
                except:
                    print(f"Erreur de format : hh:mm:ss")
                    time.sleep(2)
                    os.system('cls')
            elif choice_modif == "n":
                print(f"Il n'y aura pas de modifications ! \n"
                      f"Retour au menu. \n")
                time.sleep(5)
                os.system('cls')
                menu()

    if choice == "4":
        timersDos = "timers"
        dossier = f'E:\programmation\projet\obstimer\{timersDos}'
        print(f"\nListe des timers :")
        for fichier in os.listdir(dossier):
            if fichier.endswith('.txt'):
                print(fichier)
        print(f"\n")
        while True:
            next_switch = input(f"m pour retourner au menu \n")
            if next_switch == "m" or next_switch == "M":
                print(f"Retour au menu")
                time.sleep(3)
                os.system('cls')
                menu()

    else:
        print(f"Erreur de selection retour au menu")
        time.sleep(4)
        os.system('cls')
        menu()
