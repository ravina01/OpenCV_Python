import os
import cv2

"""
Blur - to remove noise
Guassian
median filter
biltaral filter
"""

img_bgr = cv2.imread(os.path.join('.', 'Assets', 'dog_out.jpeg'))

k_size = 7

img_blur_7 = cv2.blur(img_bgr, (k_size, k_size))
img_blur_15 = cv2.blur(img_bgr, (15, 15))
img_gaussianBlue = cv2.GaussianBlur(img_bgr, (k_size, k_size), 5)


cv2.imshow("Image Blur 7 ", img_blur_7)
cv2.imshow("Image Blur 15 ", img_blur_15)
cv2.imshow("Image Gaussian Blur ", img_gaussianBlue)

cv2.waitKey(0)