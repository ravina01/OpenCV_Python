import os
import cv2

"""
Edge detection - dilate erode, closing and opening
sobel
laplacian
canny
"""

img_bgr = cv2.imread(os.path.join('.', 'Assets', 'dog_out.jpeg'))
img_edg_canny = cv2.Canny(img_bgr, 100, 200)

img_edge_sobel = cv2.Sobel(img_bgr, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=3)

img_edge_laplacian = cv2.Laplacian(img_bgr, cv2.CV_64F, ksize=3)

cv2.imshow("img_edg_canny ", img_edg_canny)
cv2.imshow("img_edge_sobel ", img_edge_sobel)
cv2.imshow("img_edg_laplacian ", img_edge_laplacian)

cv2.waitKey(0)