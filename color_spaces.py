import os
import cv2

# Color spaces

img_bgr = cv2.imread(os.path.join('.', 'Assets', 'dog_out.jpeg'))


img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
img_grey = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
img_xyz = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2XYZ)
img_lab = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2LAB)
img_YcrCb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2YCrCb)

cv2.imshow("image BGR", img_bgr)
cv2.imshow("image RGB", img_rgb) # swaps red with blue
cv2.imshow("image Grey", img_grey)
cv2.imshow("image HSV", img_hsv) # color detection
cv2.imshow("image XYZ", img_xyz)
cv2.imshow("image LAB", img_lab)
cv2.imshow("image YCrCb", img_YcrCb)

cv2.waitKey(0)