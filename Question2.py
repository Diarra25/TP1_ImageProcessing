import cv2
import numpy as np
import matplotlib.pyplot as plt # Affichage 

#Chargement image en niveaux de gris
img = cv2.imread('imagesDeTest/imagesDeTest/peppers-512.png', cv2.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"

#Affichage de l'image
#plt.subplot(221), plt.imshow(img,'gray')

#Calcul de l'histogramme
hist = cv2.calcHist([img],[0],None,[256],[0,256])

# Affichage de l'image et de l'histogramme
#plt.plot(hist)
#plt.show()

#égalisation de l'histogramme
equa = cv2.equalizeHist(img)

#Affichage et comparaison avec l'image d'origine
#plt.subplot(222), plt.imshow(equa,'gray')

alpha =1.5
beta =0

#Modification luminosité+contraste en fonction de alpha et beta
result = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

#Calcul de l'histogramme
histConvert = cv2.calcHist([result],[0],None,[256],[0,256])

plt.subplot(221),plt.plot(histConvert)
plt.subplot(222), plt.imshow(result,'gray')
plt.show()
