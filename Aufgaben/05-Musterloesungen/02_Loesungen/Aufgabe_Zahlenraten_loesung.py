import random
import math
# Inputs nehmen
lower = int(input("Untere Grenze eingeben:- "))
 
upper = int(input("Obere Grenze eingeben:- "))
 
# Generierung einer Zufallszahl zwischen 
#der unteren und oberen Grenze
x = random.randint(lower, upper)
print(" Du hast nur 7 Versuche, die Zahl zu erraten !")
 
# Die Anzahl der Vermutungen beginnen.
count = 0
 

while count < 7:
    count += 1
 
    # nimmt eine Vermutung als Eingabe
    guess = int(input("Zahl raten:- "))
 
    # Condition testing
    if x == guess:
        print("Glückwunsch, du hast es geschafft!", count , "Versuche")
        break
    elif x > guess:
        print("Du hast zu niedrig geraten!")
    elif x < guess:
        print("Du hast zu hoch geraten!")
if count >= 7:
    print("Die richtige Zahl ist", x)
    print("Viel Glück beim nächsten Mal!")
