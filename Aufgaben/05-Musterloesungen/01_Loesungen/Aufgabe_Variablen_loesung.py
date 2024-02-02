zahl=2
kommazahl=2.7
hallo="hola"
tschuess="adios"
immerWahr= True

print(zahl,kommazahl,hallo,tschuess,immerWahr)

#Print mit casten
print(str(kommazahl)+ " ist groesser als "+str(zahl))
#print ohne casten
print(kommazahl, " ist groesser als ", zahl)

gruss= hallo+ tschuess
print(gruss)
zahl+=7
print(zahl)

print((zahl>kommazahl) and immerWahr)
print((zahl>kommazahl) or immerWahr)

#verändere immerWahr, da or nur False zurückgibt, wenn beide Argumente falsch sind
immerWahr=False
print((zahl<kommazahl)or immerWahr)
