Program for histogram stretching algorithm:

import cv2
import numpy as np
def histogram_stretching(image):

# Convert image to LAB color space
lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

# Split the LAB image into channels
l_channel, a_channel, b_channel = cv2.split(lab_image)

# Stretch histogram of L channel
l_channel = cv2.equalizeHist(l_channel)

# Merge the channels back together
stretched_lab = cv2.merge((l_channel, a_channel, b_channel))

# Convert back to BGR color space
stretched_image = cv2.cvtColor(stretched_lab, cv2.COLOR_LAB2BGR)
return stretched_image

# Load an image
image_path = r"D:\final project\IMAGE6\Enhanced Image6.png"
original_image = cv2.imread(image_path)

# Perform histogram stretching
stretched_image = histogram_stretching(original_image)

# Display the original and stretched images
cv2.imshow("Original Image", original_image)
cv2.imshow("Stretched Image", stretched_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
