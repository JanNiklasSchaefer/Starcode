def sortieren(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            # if we haven't needed to make a single swap, we 
            # can just exit the main loop.
            return
            
print("Gib eine vierstellige Zahl ein, bei der NICHT alle vier Ziffern gleich sein dürfen")
zahl=input()

ziffern=[int(z) for z in str(zahl)]
if len(ziffern) != 4:
				print("Die Zahl muss vierstellig sein. Versuchs nochmal.")
				exit()
if ziffern[0]==ziffern[1]==ziffern[2]==ziffern[3]:
				print("Die Zahl darf nicht aus vier gleichen Ziffern bestehen. Versuchs nochmal.")
				exit()
hilfsbool = True
GesuchteKonstante=0

while hilfsbool:
				
				if len(ziffern)==3:
								ziffern.append(0)
				
				elif len(ziffern)==2:
								ziffern.append(0)
								ziffern.append(0)
				
				elif len(ziffern)==1:
								ziffern.append(0)
								ziffern.append(0)
								ziffern.append(0)
				sortieren(ziffern)
				vKnG=ziffern #Ziffern der Zahl sind von klein nach Groß sortiert
				vGnK=vKnG[::-1] #Das kehrt die Liste der Ziffern um, die Ziffern sind so von groß nach kl. sortiert
				differenz=(1000*vGnK[0] +100*vGnK[1] +10*vGnK[2] +vGnK[3])-(1000*vKnG[0] +100*vKnG[1] +10*vKnG[2] +vKnG[3])
				ziffern=[int(z) for z in str(differenz)]
				if differenz!=GesuchteKonstante:
								GesuchteKonstante=differenz
				else:
								hilfsbool=False
				
print("Die gesuchte Konstante ist:",GesuchteKonstante)
