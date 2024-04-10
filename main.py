import cv2
import numpy as np
from matplotlib import pyplot as plt
import easyocr
plt.style.use('seaborn')

image = cv2.imread('ada.jpg')
blah = cv2.medianBlur(image,5)

blur = cv2.GaussianBlur(image,(5,5),0)

blor = cv2.bilateralFilter(image,9,100,100)

dst = cv2.fastNlMeansDenoisingColored(image, None, 8, 8, 7, 21)

kernel = np.array([[0,-1,0], [-1,5,-1], [0,-1,0]])
imug = cv2.filter2D(src=image, ddepth=-1, kernel=kernel)

def unsharp_mask(image, kernel_size=(5, 5), sigma=1.0, amount=1.0, threshold=0):
    """Return a sharpened version of the image, using an unsharp mask."""
    blurred = cv.GaussianBlur(image, kernel_size, sigma)
    sharpened = float(amount + 1) * image - float(amount) * blurred
    sharpened = np.maximum(sharpened, np.zeros(sharpened.shape))
    sharpened = np.minimum(sharpened, 255 * np.ones(sharpened.shape))
    sharpened = sharpened.round().astype(np.uint8)
    if threshold > 0:
        low_contrast_mask = np.absolute(image - blurred) < threshold
        np.copyto(sharpened, image, where=low_contrast_mask)
    return sharpened

def example():
    sharpened_image = unsharp_mask(dst)
    return sharpened_image

cv2.imwrite('my-sharpened-a.jpg', dst)

gray1 = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)

thresh1 = cv2.adaptiveThreshold(gray1, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 15)

reader = easyocr.Reader(['en'], gpu=True)
text = reader.readtext(image)
for t in text:
  print(t[1])

row, col = 3, 1
fig, axs = plt.subplots(row, col, figsize=(25, 20))
fig.tight_layout()

axs[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axs[0].set_title('Elephant')

axs[1].imshow(cv2.cvtColor(thresh1, cv2.COLOR_BGR2RGB))
axs[1].set_title('Fast Means Denoising')

axs[2].imshow(cv2.cvtColor(thresh1, cv2.COLOR_BGR2RGB))
axs[2].set_title('Fast Means Denoising')
plt.show()

