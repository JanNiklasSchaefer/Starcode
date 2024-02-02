
import math 
def loesungen(a,b,c):
	p=b/a
	q=-c/a
	if (p/2)**2-q <0:
		print("Es gibt keine reellen Loesungen.")
	else:
		loesung12=-(p/2)+ math.sqrt((p/2)**2-q)
		loesung34=-(p/2)- math.sqrt((p/2)**2-q)
		
		if (loesung12<0 and loesung34>=0):
			print("Es gibt nur 2 reelle Loesungen:")
			loesung3=math.sqrt(loesung34)
			loesung4=-math.sqrt(loesung34)
			print(loesung3, loesung4)
				
		elif (loesung34<0 and loesung12>=0):
			print("Es gibt nur 2 reelle Loesungen:")
			loesung1=math.sqrt(loesung12)
			loesung2=-math.sqrt(loesung12)
			print(loesung1, loesung2)
		elif (loesung12<0 and loesung34<0):
			print("Es gibt keine reellen Loesungen.")
		else:
			print("Es gibt 4 reelle Loesungen:")
			loesung1=math.sqrt(loesung12)
			loesung2=-math.sqrt(loesung12)
			loesung3=math.sqrt(loesung34)
			loesung4=-math.sqrt(loesung34)
			print(loesung1, loesung2, loesung3, loesung4)
	
print("Bitte rufe die Funktion loesungen mit den Parametern a,b,c einer Funktion mit der Form a*x^4+b*x^2=c auf")
