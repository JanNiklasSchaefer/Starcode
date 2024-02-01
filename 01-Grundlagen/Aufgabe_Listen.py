test_liste=[]

test_liste[2]= 222
print("test_liste[2]=222 sorgt dafür ...")


variable = len(test_liste)
print("len(test_liste) gibt ...")

test_liste.append(98765)
print("test_liste.append(98765) ... ")

variable = test_liste.index(2345)
print("test_liste.index(2345) gibt an, ...")

test_liste.remove(222)
print("test_liste.remove(222) ... ")

test_liste.pop()
print("test_liste.pop() ...")

variable = test_liste.count(222)
print("test_liste.count(222) ...")

test_liste.reverse()
print("test_liste.reverse() ...")
