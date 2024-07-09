import cv2
import matplotlib.pyplot as plt

image = cv2.imread('notebooks/test-image.jpg')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
