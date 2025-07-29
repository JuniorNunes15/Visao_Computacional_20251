import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('imagens/jato.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 

def adjust_gamma(channel, gamma):
    invGamma = 1.0 / gamma
    table = np.array([(i / 255.0) ** invGamma * 255
                      for i in np.arange(0, 256)]).astype("uint8")
    return cv2.LUT(channel, table)

r, g, b = cv2.split(img)

r = adjust_gamma(r, 0.5)
g = adjust_gamma(g, 0.5)
b = adjust_gamma(b, 1.5)

yellowish_img = cv2.merge([r, g, b])

cv2.imwrite('resultado.jpg', img)
plt.imshow(yellowish_img)
plt.axis('off')
plt.show()
