Program for color balance algorithm:

import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image # Not used in this code

def color_balance_underwater(image):
# Convert the image to float32 for better precision in calculations
img_float = image.astype(np.float32)

# Separate the image into individual color channels
b, g, r = cv2.split(img_float)

# Calculate the mean values for each channel
mean_b = np.mean(b)
mean_g = np.mean(g)
mean_r = np.mean(r)
x =(( np.mean(r) + np.mean(b)+ np.mean(g))/3)
mean_x = np.mean(x)

# Calculate the correction factors based on the mean values
correction_r = x / mean_r
correction_b = x / mean_b
correction_g = x / mean_g
#correction_r1 = r + correction_r
#correction_b1 = b + correction_b
#correction_g1 = g + correction_g

# Apply the correction factors to balance the colors
balanced_b = np.clip(b * correction_b , 0, 255).astype(np.uint8)
balanced_g = np.clip(g * correction_g , 0, 255).astype(np.uint8)
balanced_r = np.clip(r * correction_r , 0, 255).astype(np.uint8)

# Ensure all channels have the same shape
# r = r[:balanced_b.shape[0], :balanced_b.shape[1]]

# Merge the balanced channels back into an RGB image
balanced_image = cv2.merge([balanced_b, balanced_g, balanced_r])
return balanced_image

# Read the underwater image
input_image_path = r"D:\final project\IMAGE6.jpg"
original_image = cv2.imread(input_image_path)

# Apply color balance
balanced_image = color_balance_underwater(original_image)

# Create separate histograms for each color channel (original and balanced)
plt.figure(figsize=(12, 6))

# Balanced image histograms
plt.subplot(1,2, 2)
plt.hist(balanced_image[:, :, 0].ravel(), bins=256, range=(0, 256), color='blue', alpha=0.5, label='Blue')
plt.hist(balanced_image[:, :, 1].ravel(), bins=256, range=(0, 256), color='green', alpha=0.5, label='Green')
plt.hist(balanced_image[:, :, 2].ravel(), bins=256, range=(0, 256), color='red', alpha=0.5, label='Red')
plt.title('balanced Image Histogram')
plt.legend()


# Original image histograms
plt.subplot(1, 2,1)
plt.hist(original_image[:, :, 0].ravel(), bins=256, range=(0, 256), color='blue', alpha=0.5, label='Blue')
plt.hist(original_image[:, :, 1].ravel(), bins=256, range=(0, 256), color='green', alpha=0.5, label='Green')
plt.hist(original_image[:, :, 2].ravel(), bins=256, range=(0, 256), color='red', alpha=0.5, label='Red')
plt.title('original Image Histogram')
plt.legend()

#plt.subplot(2, 3, 5)
#plt.imshow(balanced_image)
#plt.title('balanced image')
#plt.axis('off')
# Display original and balanced images
#plt.subplot(2, 3, 4)
#plt.imshow(original_image)
#plt.title('original image')
#plt.axis('off')
plt.tight_layout()
plt.show()

# Display the original and balanced images using OpenCV (unmodified)
cv2.imshow('Original Image', original_image)
cv2.imshow('Balanced Image', balanced_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
