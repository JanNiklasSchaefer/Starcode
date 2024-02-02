 
def verschiebung(zeichen, schluessel):
	zahl = ord(zeichen)
	neueZahl = zahl + schluessel
	if (97<= neueZahl<=122):
		neuesZeichen = chr(neueZahl)
		
	elif (neueZahl>122):
		ueberhang= neueZahl-122 #der "Rest", also wieviele Schritte wir ueber das erlaubte Alphabet hinausgehen 
		ueberhang+=96 #+96, da unser "erster" Buchstabe der Nummer 97 entspricht
		neuesZeichen=chr(ueberhang) 
	return neuesZeichen
    

text='wannistwiedersommer'
verschluesselt=''
for c in text:
	c_neu=verschiebung(c,11)
	verschluesselt+=c_neu
print(verschluesselt)
