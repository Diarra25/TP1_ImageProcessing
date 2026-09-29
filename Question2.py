import cv2
import numpy as np
import matplotlib.pyplot as plt # Affichage 

#Chargement image
img = cv2.imread('imagesDeTest/imagesDeTest/peppers-512.png', cv2.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"

#Calcul de l'histogramme
hist = cv2.calcHist([img],[0],None,[256],[0,256])

# Affichage de l'image et de l'histogramme
plt.plot(hist)
plt.show()