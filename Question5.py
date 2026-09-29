import cv2
import numpy as np
import matplotlib.pyplot as plt # Affichage 

#Chargement image en couleur (Gris)
img = cv2.imread('imagesDeTest/imagesDeTest/squares.tif', cv2.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"

rows,cols = img.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1) # Matrice de transformation (90 degrés)
dst = cv2.warpAffine(img,M,(cols,rows))

dst2 = cv2.INTER_NEAREST(img,M,(cols,rows))

#Affichage des images
plt.subplot(121), plt.imshow(img,'gray')
plt.subplot(122), plt.imshow(dst,'gray')
plt.show()