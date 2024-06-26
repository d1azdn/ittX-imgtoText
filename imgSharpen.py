import cv2
import numpy as np

class sharpening:
    def __init__(self):
        pass
    def morphEx(self, image):
        img = cv2.imread(image)
        imgArray = np.array(img)
        grey = cv2.cvtColor(imgArray,cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(grey,(5,5),0)
        dilated = cv2.dilate(blur,np.ones((3,3)))
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 1))
        closing = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel)
        cv2.imwrite("imageEnhanced.png", closing)
        return closing
    
    def unsharpMask(self, image, kernel_size=(5, 5), sigma=1.0, amount=1.0, threshold=0):
        img = cv2.imread(image)
        blurred = cv2.GaussianBlur(img, kernel_size, sigma)
        sharpened = float(amount + 1) * img - float(amount) * blurred
        sharpened = np.maximum(sharpened, np.zeros(sharpened.shape))
        sharpened = np.minimum(sharpened, 255 * np.ones(sharpened.shape))
        sharpened = sharpened.round().astype(np.uint8)
        if threshold > 0:
            low_contrast_mask = np.absolute(img - blurred) < threshold
            np.copyto(sharpened, img, where=low_contrast_mask)
        cv2.imwrite("imageEnhanced.png", sharpened)
        return sharpened
    
    def gaussThresh(self, image):
        img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
        blur = cv2.GaussianBlur(img,(5,5),0)
        thresh = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
        cv2.imwrite("imageEnhanced.png", thresh)
        return thresh

