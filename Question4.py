import cv2
import numpy as np
import matplotlib.pyplot as plt # Affichage 

#Quantification de l'image, en fonction du nombre de niveaux de gris n
def quantification(image, n):
    if n > 0 and n <= 256:
        pas = 256//n
        return (image // pas) * pas + pas // 2  # Quantification de l'image
    else:
        return image  # Si n est invalide, on retourne l'image originale

#Chargement image en couleur (BGR)
img = cv2.imread('imagesDeTest/imagesDeTest/peppers-512-RGB.png', cv2.IMREAD_COLOR)
assert img is not None, "file could not be read, check with os.path.exists()"

#===============================
# Affichage de l'image en fonction du nombre de niveaux de gris donné
#img = quantification(img, 64)
#plt.subplot(221), plt.imshow(img,'gray')

#img = quantification(img, 16)
#plt.subplot(221), plt.imshow(img,'gray')

#img = quantification(img, 4)
#plt.subplot(221), plt.imshow(img,'gray')

#img = quantification(img, 2)
#plt.subplot(221), plt.imshow(img,'gray')

#Calcul de l'histogramme
#hist = cv2.calcHist([img],[0],None,[256],[0,256])

# Affichage de l'image et de l'histogramme
#plt.subplot(222), plt.plot(hist)

#===============================
#Application d'une LUT pour coloriser l'image en fct des niveaux de gris
#img = cv2.applyColorMap(img, cv2.COLORMAP_JET)
#plt.subplot(221), plt.imshow(img)

#img = cv2.applyColorMap(img, cv2.COLORMAP_HOT)
#plt.subplot(222), plt.imshow(img)

#img = cv2.applyColorMap(img, cv2.COLORMAP_OCEAN)
#plt.subplot(223), plt.imshow(img)

#img = cv2.applyColorMap(img, cv2.COLORMAP_PINK)
#plt.subplot(224), plt.imshow(img)

#===============================

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # BGR->RGB
b,g,r = cv2.split(img) # Séparation des canaux de couleur
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Conversion en niveaux de gris

#Affichage RBG + niveaux de gris
plt.subplot(221), plt.imshow(b, 'gray')
plt.subplot(222), plt.imshow(g, 'gray')
plt.subplot(223), plt.imshow(r, 'gray')
plt.subplot(224), plt.imshow(gray, 'gray')

plt.show()
