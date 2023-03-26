import cv2
import numpy as np

# Load and resize the image
img = cv2.imread('GreenScreen.jpg')
img = cv2.resize(img, (600, 500))

# Convert BGR to HSV for masking
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define the lower and upper hsv bounds of the green color
lower = np.array([40, 40, 40])
upper = np.array([70, 255, 255])

# Create a mask that only includes pixels in the green range
mask = cv2.inRange(hsv, lower, upper)

# Apply the mask on the original image to only show the green color
green = cv2.bitwise_and(img, img, mask=mask)

# Display the resulting image
cv2.imshow("Green Only", green)
cv2.waitKey(0)
cv2.destroyAllWindows()