import random

def wahrsagerin():
    
    antworten = [
        ##Sucht euch beliebig viele Antworten aus, die man auf eine Ja/Nein Frage geben kann
    ]

    
    frage = input("Stelle der Wahrsagerin eine Ja- oder Nein-Frage: ")

    
    antwort = random.choice(antworten)

    ###Lasst die Wahrsagerin die zufällig ausgewählte Antwort auf der Konsole ausgeben


wahrsagerin()
