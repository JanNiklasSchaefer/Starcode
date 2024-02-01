for i in range(0,24):
	print(i)
i=23
while i>=0:
	print(i)
	i-=1
	
for i in range(1,13,2):
	print(i*"*")

eingabe=input("Gib mir die geheime Eingabe: ")
while eingabe != "huppala":
	eingabe = input("Falsch! Gib mir die geheime Eingabe: ")
print("Gut! Danke!")
