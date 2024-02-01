import numpy as np
import matplotlib.pyplot as plt
import random, sys
from PIL import Image


"""
Die Variable image_array lässt sich als Matrix der Farbwerte des geladenen Bildes verstehen:
Falls image_array[z][s] == 1, ist das Pixel in der Zeile z, Spalte s schwarz,
falls image_array[z][s] == 0, ist das Pixel in der Zeile z, Spalte s weiß

In height und width sind die Höhe und Breite des Bildes gespeichert
"""
def decide(image_array):
    height, width = image_array.shape[0], image_array.shape[1]

    # TODO: Schreibe hier deinen Code, um zu entscheiden, ob image_array eine 6 oder 9 ist

    # Lösung: Mehr Schwarze Pixel in der oberen Bildhälfte => 9, ansonsten => 6
    black_pixels_top = 0
    black_pixels_bottom = 0


    # Finde erste und letzte Zeile mit schwarzen Pixeln
    first = height-1
    last = 0

    for z in range(height):
        for s in range(width):
            if image_array[z][s]==1:
                if z < first:
                    first = z
                if z > last:
                    last = z

    for z in range(first, last+1):
        for s in range(width):
            if z<((first+last+1)/2) and image_array[z][s]==1:
                black_pixels_top = black_pixels_top+1
            if z>=((first+last+1)/2) and image_array[z][s]==1:
                black_pixels_bottom = black_pixels_bottom+1


    # Weise answer abhängig von der erkannten Zahl entweder den Wert 6 oder 9 zu
    answer = 6
    if black_pixels_top > black_pixels_bottom:
        answer = 9

    return answer




def convert_image(image):
    image_array = np.array(image)
    image_array[image_array == 0] = 1
    image_array[image_array == 255] = 0
    return image_array

def test_6():
    path = "Data/6/" + str(random.randint(0,499)) + ".png"
    image = Image.open(path).convert("L")
    image_array = convert_image(image)
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.title("Erkannte Zahl: " + str(decide(image_array)))
    plt.show()

def test_9():
    path = "Data/9/" + str(random.randint(0,499)) + ".png"
    image = Image.open(path).convert("L")
    image_array = convert_image(image)
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.title("Erkannte Zahl: " + str(decide(image_array)))
    plt.show()

def test_all():
    correct_answers = 0
    for i in range(500):
        path = "Data/6/" + str(i) + ".png"
        image = Image.open(path).convert("L")
        image_array = convert_image(image)
        if decide(image_array) == 6:
            correct_answers += 1

    for i in range(500):
        path = "Data/9/" + str(i) + ".png"
        image = Image.open(path).convert("L")
        image_array = convert_image(image)
        if decide(image_array) == 9:
            correct_answers += 1

    print("Dein Code kann " + str(correct_answers/1000) + "% aller Bilder korrekt klassifizieren.")



if __name__ == '__main__':
    globals()[sys.argv[1]]()
    