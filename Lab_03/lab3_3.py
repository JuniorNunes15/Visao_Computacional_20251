import cv2
import numpy as np

img = cv2.imread('oguri.png')

sepia_filter = np.array([[0.272, 0.534, 0.131],
                         [0.349, 0.686, 0.168],
                         [0.393, 0.769, 0.189]])

sepia = cv2.transform(img, sepia_filter)
sepia = np.clip(sepia, 0, 255).astype(np.uint8)

cv2.imwrite('respostas/oguri_sepia.jpg', sepia)
cv2.imshow('Sépia', sepia)
cv2.waitKey(0)
cv2.destroyAllWindows()
