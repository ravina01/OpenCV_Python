import cv2
import os

#read image
image_path = os.path.join('.','Assets', 'Happy-Shih-tzu-dog-sitting.jpeg')
print(image_path)
#"Assets/Happy-Shih-tzu-dog-sitting.jpeg"
img = cv2.imread(image_path)


#write image
cv2.imwrite(os.path.join('.','Assets', 'dog_out.jpeg'), img)

#display image
cv2.imshow("Image", img)
cv2.waitKey(0) # to wait until i press the key - its in miliseconds
