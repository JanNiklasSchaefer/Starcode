def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y
   
def potenz(x,y):
	ergebnis=0
	for i in range(1,x):
		ergebnis*=i
	return ergebnis

def test_gerade(x):
	if x%2==0:
		return True
	else:
		return False

def test_4_teilbarkeit(x):
	if x%4==0:
		return True
	else: 
		return False

def test_5_teilbarkeit(x):
	if x%5==0:
		return True
	else: 
		return False
def test_6_teilbarkeit(x):
	if x%6==0:
		return True
	else: 
		return False

def test_9_teilbarkeit(x):
	if x%9==0:
		return True
	else: 
		return False	
		
def primzahl(x):
	for i in range(2,x):
		if x%i==0:
			return False
	return True	




while True:
     
    print(" Wähle eine Operation: \n 1: Addieren\n 2: Subtrahieren \n 3: Multiplizieren \n 4: Dividieren \n 5: Potenzieren\n 6: Ist die Zahl gerade oder ungerade?\n "
           +"7: Ist die Zahl durch 4 teilbar? \n 8: Ist die Zahl durch 5 teilbar? \n 9: Ist die Zahl durch 6 teilbar? \n 10: Ist die Zahl durch 9 teilbar?\n 11: Ist die Zahl eine Primzahl?\n ")
    choice = input("Gib jetzt deine Wahl ein (1/.../11):\n")
    if choice == '1':
        x= input("Erste Zahl eingeben: x= ")
        y=input ("Zweite Zahl eingeben: y= ")
        print ("x plus y ist ", add(float(x),float(y)))

    elif choice == '2':
        x= input("Erste Zahl eingeben: x= ")
        y=input ("Zweite Zahl eingeben: y= ")
        print ("x minus y ist ", subtract(float(x),float(y)))
    elif choice == '3':
        x= input("Erste Zahl eingeben: x= ")
        y=input ("Zweite Zahl eingeben: y= ")
        print ("x mal y ist ", multiply(float(x),float(y)))
    elif choice == '4':
        x= input("Erste Zahl eingeben: x= ")
        y=input ("Zweite Zahl eingeben: y= ")
        print ("x geteilt durch y ist ", divide(float(x),float(y)))
    elif choice == '5': 
        x= input("Erste Zahl eingeben: x= ")
        y=input ("Zweite Zahl eingeben: y= ")
        print ("x hoch y ist ", potenz(float(x),float(y)))
    elif choice == '6':
        x = input("Zahl eingeben: x= ")
        if (test_gerade(int(x))):
            print ("x ist gerade.\n")
        else:
	        print ("x ist ungerade.\n")
    elif choice == '7':
        x = input("Zahl eingeben: x= ")
        if (test_4_teilbarkeit(int(x))):
            print ("x ist durch 4 teilbar.\n")
        else:
            print ("x ist nicht durch 4 teilbar.\n")
    elif choice == '8':
         x = input("Zahl eingeben: x= ")
         if (test_5_teilbarkeit(int(x))):
            print ("x ist durch 5 teilbar.\n")
         else:
            print ("x ist nicht durch 5 teilbar.\n")
    elif choice == '9':
         x = input("Zahl eingeben: x= ")
         if (test_6_teilbarkeit(int(x))):
            print ("x ist durch 6 teilbar.\n")
         else:
            print ("x ist nicht durch 6 teilbar.\n")
    elif choice == '10':
         x = input("Zahl eingeben: x= ")
         if (test_9_teilbarkeit(int(x))):
            print ("x ist durch 9 teilbar.\n")
         else:
            print ("x ist nicht durch 9 teilbar.\n")    
    elif choice == '11':
         x = input("Zahl eingeben: x= ")
         if (primzahl(int(x))):
            print ("x ist eine Primzahl.\n")
         else:
            print ("x ist keine Primzahl.\n")                        
    else:
        print("Diese Operation existiert nicht")    
           
    nochmal = input("Willst du noch etwas ausrechnen? (ja/nein): ")
    if nochmal == "ja":
        continue
    elif nochmal != "nein" and nochmal!= "ja":

        print("Ungültige Eingabe. Das Programm wird neu gestartet.")
    else: 
        break
