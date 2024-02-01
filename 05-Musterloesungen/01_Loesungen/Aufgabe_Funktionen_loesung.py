

def ausgabe(x,y):
	print("Das Ergebnis von ", x, " + ", y, " ist: ", x+y)
    
def quadratzahl(x):
	i = 0
	while i*i < x:
		i = i + 1
	if i*i == x:
		return True
	else:
		return False

def muster1():
	for i in range(1,4):
		print("00000")

def muster2():
	for i in range(1,3):
		print("~~~~~~~~~\n*********")

#hier beginnt die Programmausführung

ausgabe(23456,4637)
ausgabe(987675,11132)
ausgabe(20679,6774222243)
ausgabe(123345,834)
ausgabe(13459325,98765432)

eingabe=input("Gib mir eine Zahl, und ich prüfe, ob sie eine Quadratzahl ist: ")

if(quadratzahl):
	print("Deine Zahl ist eine Quadratzahl.")
else:
	print("Deine Zahl war keine Quadratzahl.")

muster1()
muster2()
