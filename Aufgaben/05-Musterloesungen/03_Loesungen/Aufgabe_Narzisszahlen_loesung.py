

def narzisscheck(zahl):
	ziffern=[int(z) for z in str(zahl)] #Extrahiert die Ziffern der Zahl in eine Liste.
	summe=0
	n=len(ziffern)
	for i in range(n):
		summe+=ziffern[i]**n
	if zahl==summe:
		return 1
	else:
		return 0
		
		
counter=0
liste_aller_4stelligen_narzisszahlen=[]		
for i in range(1000,10000,1):
	if narzisscheck(i)==1: #Narzisszahl gefunden -> Zaehler um einen erhoehen
		counter+=1
		liste_aller_4stelligen_narzisszahlen.append(i)
	
print(counter,liste_aller_4stelligen_narzisszahlen)
