import cv2
import numpy as np
import matplotlib.pyplot as plt # Affichage 

#Sous-échantillonnage d'une image -> Vers une image plus petite
def sous_echantillonner(image, facteur):
    if facteur > 0:
        return image[::facteur, ::facteur]
    else:
        raise ValueError("Le facteur de sous-échantillonnage doit être un entier positif.")

#Chargement image en niveaux de gris
img = cv2.imread('imagesDeTest/imagesDeTest/peppers-128.png', cv2.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"

#Sous-échantillonnage
#img2 = sous_echantillonner(img, 4)

#Affichage des images
plt.subplot(221), plt.imshow(img,'gray')
#plt.subplot(222), plt.imshow(img2,'gray')

# Resize sur 64x64 pixels (512x512 pour 3.2)
img2 = cv2.resize(img, (512, 512), interpolation=cv2.INTER_NEAREST)

plt.subplot(223), plt.imshow(img2,'gray')

# Resize sur 64x64 pixels
img2 = cv2.resize(img, (64, 64), interpolation=cv2.INTER_AREA)

# Resize sur 512x512 pixels
img2 = cv2.resize(img, (512, 512), interpolation=cv2.INTER_LINEAR)

plt.subplot(224), plt.imshow(img2,'gray')

plt.show()
