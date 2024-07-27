import os
import cv2

img = cv2.imread(os.path.join('.', 'Assets', 'dog_out.jpeg'))
print(img.shape) # height, width, channels
height , width, channels = img.shape

# resize
img = cv2.resize(img, (600,400))# give width x height
print(img.shape) # height, width, channels

# crop
cropped_img = img[120:320, 220:420]

cv2.imshow("image", cropped_img)


cv2.waitKey(0)