plz =input("Gib deine Postleitzahl ein: ")
if 10115<=int(plz)<=14199:
	print("Cool! Du wohnst in Berlin!")
else: 
	print("Woanders gibt es auch schoene Staedte")
	
	
print("Bitte nenne mir 3 voneinander verschiedene Zahlen:")
zahl1=int(input("\n"))
zahl2=int(input("\n"))
zahl3=int(input("\n"))

if zahl1>zahl2:
	if zahl1>zahl3:
		print(zahl1, " ist die groesste Zahl!")
else:
	if zahl2>zahl3:
		print(zahl2, " ist die groesste Zahl!")
	else:
		print(zahl3, " ist die groesste Zahl!")

eingabe=input("Magst du Kuchen?")

if eingabe== 'ja' or eingabe=='JA' or eingabe=='Ja':
	print("Kuchen ist echt lecker")
elif eingabe =='nein' or eingabe == 'NEIN' or eingabe=='Nein':
	print("Es gibt auch andere leckere Dinge")
else:
	print("Das war eine ungültige Eingabe :/")
