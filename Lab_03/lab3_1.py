import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('imagens/salt_noise.png', 0)

#FILTROS NO DOMÍNIO ESPACIAL

sobel = cv2.Sobel(img, cv2.CV_8U, dx=1, dy=1)

canny = cv2.Canny(img, 100, 200)

low_sigma = cv2.GaussianBlur(img, (3, 3), 0)
high_sigma = cv2.GaussianBlur(img, (5, 5), 0)
dog = cv2.subtract(low_sigma, high_sigma)

#FILTRO NO DOMÍNIO DA FREQUÊNCIA

img_float = np.float32(img)
dft = cv2.dft(img_float, flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

mask = np.float32([[-1, 0, 1],
                   [-2, 0, 2],
                   [-1, 0, 1]])

rows, cols = img.shape
filter_mask = np.zeros((rows, cols), dtype=np.float32)
filter_mask[(rows//2)-1:(rows//2)+2, (cols//2)-1:(cols//2)+2] = mask

filter_dft = cv2.dft(filter_mask, flags=cv2.DFT_COMPLEX_OUTPUT)
filter_dft_shift = np.fft.fftshift(filter_dft)

mag = cv2.magnitude(filter_dft_shift[:, :, 0], filter_dft_shift[:, :, 1])
filter_dft_shift[:, :, 0] = mag
filter_dft_shift[:, :, 1] = mag

filtered_dft = cv2.multiply(dft_shift, filter_dft_shift)

idft_shift = np.fft.ifftshift(filtered_dft)
img_back = cv2.idft(idft_shift)
img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])
img_back = cv2.normalize(img_back, None, 0, 255, cv2.NORM_MINMAX)
img_back = np.uint8(img_back)

titles = ['Original', 'Sobel (Espacial)', 'Canny (Espacial)', 'DoG (Espacial)', 'FFT com Sobel (Freq)']
images = [img, sobel, canny, dog, img_back]


plt.figure(figsize=(12, 6))
for i in range(5):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.tight_layout()
plt.show()
