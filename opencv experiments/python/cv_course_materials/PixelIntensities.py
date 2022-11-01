import cv2
import numpy as np

image = cv2.imread('bird.jpg', cv2.IMREAD_COLOR)

# values close to 0: darker pixels
# values closer to 255: brighter pixels
print(image.shape)
print(image)

cv2.imshow('Computer Vision', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
