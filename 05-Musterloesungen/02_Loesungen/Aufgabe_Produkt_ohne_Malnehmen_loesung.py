

print("Gib zwei natürliche Zahlen ein:")
zahl1=int(input())
zahl2=int(input())
produkt_for=0
produkt_while=0
#Nun beginnen wir mit der "multiplikation" und machen es mit einer for-Schleife:

for i in range(1,zahl1+1,1):
	print(i)
	produkt_for+=zahl2
print("Das Produkt von", zahl1, "und", zahl2, "ist:", produkt_for)
j = zahl1
while j>0:
	print(j)
	produkt_while+=zahl2
	j-=1
print("Das Produkt von", zahl1, "und", zahl2, "ist:", produkt_while)
