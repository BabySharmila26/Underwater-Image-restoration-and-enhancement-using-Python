Program for contrast optimization:

import cv2
import numpy as np
def enhance_contrast(image, alpha, beta):
#Enhance contrast of an image using linear transformation:
g(x) = alpha * f(x) + beta
enhanced_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
return enhanced_image

def main():
# Load the image
image_path = r"D:\final project\IMAGE6\Balanced Image6.png" # Change this to your image path
original_image = cv2.imread(image_path)

# Define alpha and beta values for contrast enhancement
alpha = 1.5 # Contrast control (1.0-3.0)
beta = 0 # Brightness control (0-100)

# Apply contrast enhancement
enhanced_image = enhance_contrast(original_image, alpha, beta)

# Display original and enhanced images
cv2.imshow('Original Image', original_image)
cv2.imshow('Enhanced Image', enhanced_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
if __name__ == "__main__":
main()
