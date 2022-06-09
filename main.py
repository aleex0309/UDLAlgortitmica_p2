import sys
from findpeaks import findpeaks
import random
import numpy as np
from matplotlib import pyplot as plt


def image_generator(n_size=10):
    img = [[random.randint(0, 255) for i in range(n_size)] for j in range(n_size)]
    fp = findpeaks(method='mask', whitelist='peak', scale=False, denoise=None, verbose=0)
    result = fp.fit(img)
    solution = np.argwhere(result['Xdetect'] == True)
    return {
        "image": img,
        "solution": solution.tolist()
    }

# TODO: Realizar cada una de vuestras funciones para detectar barcos dentro de la imagen de entrada que se encuentra en la variable "image2D".
def shipDetectorIterativo(image):
    # ITERATIVO Nº 1
    image = setBorders(image)
    results = []
    for i in range(1, len(image) - 1):
        for j in range(1, len(image) - 1):
            if isBigger(i, j, image):
                results.append([i - 1, j - 1])

    print("The image is: ", image)
    print("The results are: ", results)
    return results

def shipDetectorRecursivo(image):
    cleanImage = setBorders(image)
    positions = []

    return lateralesRecursivo(cleanImage, positions, 1, 1)


def lateralesRecursivo(image, positions, i, j):
    if i == len(image) - 2 and j == len(image) - 1:
        return positions
    if j == len(image) - 1:
        return lateralesRecursivo(image, positions, i + 1, 1)

    if isBigger(i,j,image):
        positions.append([i - 1, j - 1])

    return lateralesRecursivo(image, positions, i, j + 1)

def setBorders(image): #Crea los bordes de -1's
    new_img = [[-1 for i in range(len(image) + 2)] for j in range(len(image) + 2)]

    for i in range(1, len(image) + 1):
        for j in range(1, len(image) + 1):
            new_img[i][j] = image[i - 1][j - 1]

    return new_img


def isBigger(i, j, image): #Comprobar laterales
    element = image[i][j]
    return (element >= image[i + 1][j] and element >= image[i - 1][j] and element >= image[i][j + 1] and element >= image[i][j - 1])


# TODO: En este programa, debereis generar las imagenes de costos correspondientes tal y como hicimos en laboratorios y en la práctica 1.
# Programa principal para la generación de las matrices 2D y la identificación de barcos.

if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.exit('Usage: ' + sys.argv[0] + ' <matrix_size_number>')

    image2D = image_generator(int(sys.argv[1]))
    print("The original image is: ", image2D)
    shipDetectorIterativo(image2D["image"])

