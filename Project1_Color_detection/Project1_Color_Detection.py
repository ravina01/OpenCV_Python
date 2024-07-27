"""
Project 1 - Color Detection using OpenCV
Detecting Yellow objects by converting BGR to HSV color space
Hue [0,360] - 0 degree - red, 120 degree green, 240 degree is blue
saturation - 0 means grayscale, 1 is fully saturated
value - intesity/brightness
"""

import os
import cv2
from PIL import Image
import numpy as np

from utils import get_limits

yellow = [0, 255, 255] # yellow color in RGB colorspace
green = [0,255,0]
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # to detect colors we are going to use HSV color space- Hue chanel
    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerlimit, upperlimit = get_limits(color=green)

    mask = cv2.inRange(hsv_image, lowerlimit, upperlimit) # 2 values min - max range of yellow color

    mask_ = Image.fromarray(mask)
    # Converts a NumPy array (mask) into a PIL Image object.

    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox

        cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 5)

    # cv2.imshow("mask", mask_)
    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
