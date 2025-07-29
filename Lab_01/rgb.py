import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Abre imagem
filename = sys.argv[1]
im = cv2.imread(filename)

# Converte para HSV
hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

# Máscara para pele verde (Gamora) - faixa mais restrita
lower_green = np.array([45, 100, 50])
upper_green = np.array([75, 255, 200])
mask_green = cv2.inRange(hsv, lower_green, upper_green)

# Máscara para pele azul (Nebulosa) - mais fria e menos roxa
lower_blue = np.array([100, 80, 50])
upper_blue = np.array([125, 255, 200])
mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

# Troca verde por azul
hsv[np.where(mask_green != 0)] = [115, 220, 200]  # azul saturado

# Troca azul por verde
hsv[np.where(mask_blue != 0)] = [60, 220, 180]   # verde saturado

# Converte de volta para BGR
output = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

cv2.imwrite('resultado.jpg', output)
plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()

