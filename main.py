import cv2
import numpy as np
image = cv2.imread('selfie.jpeg')

# Fill the black background with white color
cv2.floodFill(image, None, seedPoint=(0, 0), newVal=(0, 0, 255), loDiff=(2, 2, 2), upDiff=(2, 2, 2))  # Not working!

# hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  # rgb to hsv color space

# s_ch = hsv_img[:, :, 1]  # Get the saturation channel

# thesh = cv2.threshold(s_ch, 5, 255, cv2.THRESH_BINARY)[1]  # Apply threshold - pixels above 5 are going to be 255, other are zeros.
# thesh = cv2.morphologyEx(thesh, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7)))  # Apply opening morphological operation for removing artifacts.

# cv2.floodFill(thesh, None, seedPoint=(0, 0), newVal=128, loDiff=1, upDiff=1)  # Fill the background in thesh with the value 128 (pixel in the foreground stays 0.

# image[thesh == 128] = (0, 0, 255)  # Set all the pixels where thesh=128 to red.
# image[thesh == 128] = (0, 0, 255)  # Set all the pixels where thesh=128 to red.

cv2.imwrite('selfie-red-bg.jpeg', image)  # Save the output image.