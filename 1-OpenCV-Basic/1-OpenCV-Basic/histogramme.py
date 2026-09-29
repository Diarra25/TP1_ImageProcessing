import cv2
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Gestion des chemins de fichiers
base_dir = Path(__file__).resolve().parent

# Chargement de l'image en niveaux de gris
img_gray_path = base_dir / "imagesDeTest" / "imagesDeTest" / "peppers-512.png"
img_gray = cv2.imread(str(img_gray_path), cv2.IMREAD_GRAYSCALE)
if img_gray is None:
    raise FileNotFoundError(f"Image introuvable : {img_gray_path}")
print(f"Forme (gris) : {img_gray.shape}, Type : {img_gray.dtype}")
plt.subplot(1, 2, 1)
plt.title('Image en niveaux de gris')
plt.imshow(img_gray, cmap='gray')
# Calcul  et afichage de l'histogramme
histogram = cv2.calcHist([img_gray], [0], None, [256], [0, 256])
plt.subplot(1, 2, 2)
plt.title('Histogramme')
plt.plot(histogram)
plt.show()


# Egalisation de l'
img_egalisation = cv2.equalizeHist(img_gray)
plt.subplot(1, 2, 1)
plt.title('Image après égalisation')
plt.imshow(img_egalisation, cmap='gray')
histogram_egalisation = cv2.calcHist([img_egalisation], [0], None, [256], [0, 256])
plt.subplot(1, 2, 2)
plt.title('Histogramme après égalisation')
plt.plot(histogram_egalisation)
plt.show()


# Modification du contraste et de la luninosité
# 1. Augmentation de la luminosité avec alpha = 1 et beta = 40
img_luminosite = cv2.convertScaleAbs(img_gray, alpha=1, beta=40)
plt.subplot(1, 2, 1)
plt.title('Image avec augmentation de la luminosité')
plt.imshow(img_luminosite, cmap='gray')
histogram_luminosite = cv2.calcHist([img_luminosite], [0], None, [256], [0, 256])
plt.subplot(1, 2, 2)
plt.title('Histogramme avec augmentation de la luminosité')
plt.plot(histogram_luminosite)
plt.show()

# 2. Augmentation du contraste avec alpha = 1.5 et beta = 0
img_contraste = cv2.convertScaleAbs(img_gray, alpha=1.5, beta=0)
plt.subplot(1,2, 1)
plt.title('Image avec augmentation du contraste')
plt.imshow(img_contraste, cmap='gray')
histogram_contraste = cv2.calcHist([img_contraste], [0], None, [256], [0, 256])
plt.subplot(1, 2, 2)
plt.title('Histogramme avec augmentation du contraste')
plt.plot(histogram_contraste)
plt.show()