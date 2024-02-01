test_liste=["hallo", True, 3.1415, 2345, "ciao", -4]

test_liste[2]= 222
print("test_liste[2]=222 sorgt dafür, dass der Eintrag, der Index 2 hat (also der 3. wenn wir von vorne zählen), zu 222 geändert wird ")


variable = len(test_liste)
print("len(test_liste) gibt die Länge der Liste aus")

test_liste.append(98765)
print("test_liste.append(98765) fügt 98765 ans Ende der Liste an")

variable = test_liste.index(2345)
print("test_liste.index(2345) gibt an, an welchem Index das Element 2345 zu finden ist")

test_liste.remove(222)
print("test_liste.remove(222) entfernt das Element 222 aus der Liste")

test_liste.pop()
print("test_liste.pop() entfernt das hinterste Element der Liste")

variable = test_liste.count(222)
print("test_liste.count(222) zählt, wie häufig 222 in der Liste enthalten ist.")

test_liste.reverse()
print("test_liste.reverse() dreht die Elemente innerhalb der Liste um")
