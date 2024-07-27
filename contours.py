import os
import cv2

img_bgr = cv2.imread(os.path.join('.', 'Assets', 'contors.jpg'))
print(img_bgr.shape)

img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)# objects in white

contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(contours)

for contour in contours:
    # print(cv2.contourArea(contour))
    if cv2.contourArea(contour)>8000:
        cv2.drawContours(img_bgr, contour, -1, (0,0,255), 5)

        x1,y1, w, h = cv2.boundingRect(contour)
        cv2.rectangle(img_bgr, (x1,y1), (x1+w,y1+h), (0,255,0), 3)

cv2.imshow("image", img_bgr)
cv2.imshow("thresh", thresh)
# cv2.imshow("Con", contours)

cv2.waitKey(0)