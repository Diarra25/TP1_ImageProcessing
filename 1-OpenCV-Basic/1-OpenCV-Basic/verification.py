import cv2
import numpy as np
from pathlib import Path

base_dir = Path(__file__).resolve().parent

# Chargement en niveaux de gris
img_gray_path = base_dir / "imagesDeTest" / "imagesDeTest" / "monarch.png"
img_gray = cv2.imread(str(img_gray_path), cv2.IMREAD_GRAYSCALE)
if img_gray is None:
    raise FileNotFoundError(f"Image introuvable : {img_gray_path}")
print(f"Forme (gris) : {img_gray.shape}, Type : {img_gray.dtype}")
# Forme typique : (H, W)

# Chargement en couleur (BGR)
img_color = cv2.imread(str(img_gray_path), cv2.IMREAD_COLOR)
if img_color is None:
    raise FileNotFoundError(f"Image introuvable : {img_gray_path}")
print(f"Forme (couleur) : {img_color.shape}, Type : {img_color.dtype}")
# Forme typique : (H, W, 3)

# Chargement d’une image avec canal alpha (par exemple PNG avec transparence)
img_rgba_path = base_dir / "imagesDeTest" / "imagesDeTest" / "jaguar_rgba.png"
img_rgba = cv2.imread(str(img_rgba_path), cv2.IMREAD_UNCHANGED)
if img_rgba is None:
    raise FileNotFoundError(f"Image introuvable : {img_rgba_path}")
print(f"Forme : {img_rgba.shape}") # (H, W, 4)
print(f"Type : {img_rgba.dtype}")

# Accès à un pixel (100, 150) :
b, g, r, a = img_rgba[100, 150]
print(f"B: {b}, G: {g}, R: {r}, A: {a}")