import random, time
import numpy as np
import os
from helper import start, step, turnRight, turnLeft, blocked

"""
Benutze folgende Befehle zum Steuern der Figur:

step()      - Bewege die Spielfigur ein Feld in Blickrichtung
turnRight() - Drehe die Spielfigur um 90° nach rechts
turnLeft()  - Drehe die Spielfigur um 90° nach links
blocked()      - Überprüfe, ob die Spielfigur vor einer Wand steht 
                wall() gibt einen Boolean (True/False) zurück
"""


def escape():
    # TODO: Schreibe hier dein Programm
    step()
    while True:
        turnRight()
        if not blocked():
            step()
        else:
            turnLeft()
            if not blocked():
                step()
            else:
                turnLeft()

    



# Dieser Befehl startet das Spiel, nicht entfernen!
h,w = 11, 11
start(escape,h,w)




