import os
import cv2

"""
Threshold - color to binary

"""

img_bgr = cv2.imread(os.path.join('.', 'Assets', 'dog_out.jpeg'))

img_grey = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
# ret, img_threshold = cv2.threshold(img_grey, 150, 255, cv2.THRESH_BINARY)

# ret, img_threshold_1 = cv2.threshold(img_grey, 120, 255, cv2.THRESH_BINARY_INV)
img_threshold = cv2.adaptiveThreshold(img_grey, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 30)

# img_threshold = cv2.blur(img_threshold, (5,5))
cv2.imshow("Threshold ", img_threshold)
# cv2.imshow("Threshold_1", img_threshold_1)


cv2.waitKey(0)