import os
import cv2

img_bgr = cv2.imread(os.path.join('.', 'Assets', 'dog_out.jpeg'))
print(img_bgr.shape)

#line
cv2.line(img_bgr, (151, 420), (751,420), (0, 0, 255), 2)

#rectangle
cv2.rectangle(img_bgr, (254,156), (571, 383), (0,0,0), 2)

#Circle
cv2.circle(img_bgr, (421,290), 30, (255, 255, 0), 4)

#Text
cv2.putText(img_bgr, 'woo woo !', (320,200), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255), 4)

cv2.imshow("image", img_bgr)
cv2.waitKey(0)