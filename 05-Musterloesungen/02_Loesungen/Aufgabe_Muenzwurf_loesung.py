import random
choice=input ("Kopf oder Zahl?:" )
num=random.randint(1,2)

if num==1:
    Ergebnis="Kopf"

elif num==2:
    Ergebnis="Zahl"

if choice==Ergebnis:
    print ("Du hast gewonnen!Die Münze hat",Ergebnis,"geworfen")
else:
    print ("Du hast verloren! Die Münze warf", Ergebnis)
