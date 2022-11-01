import numpy as np
import cv2

original_image = cv2.imread('unsharp_bird.jpg', cv2.IMREAD_COLOR)

# sharpen kernel
# face recognition and we have a blurry CCTV video then we can apply this kernel in order to
# increase the precision of the underlying model
kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

sharpen_image = cv2.filter2D(original_image, -1, kernel)

cv2.imshow('Original Image', original_image)
cv2.imshow('Sharpen Image', sharpen_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
