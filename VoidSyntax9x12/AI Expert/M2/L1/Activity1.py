import cv2
import os

print("📁 Current Directory:", os.getcwd())

# Load the image
image = cv2.imread('VoidSyntax9x12/AI Expert/M2/L1/example.jpg')

# Check if image was loaded
if image is None:
    print("❌ Failed to load image. Check the file path.")
    exit()

# Create a resizable window
cv2.namedWindow('Loaded Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Loaded Image', 800, 500)

# Show the image
cv2.imshow('Loaded Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Image info
print(f"✅ Image Dimensions: {image.shape}")