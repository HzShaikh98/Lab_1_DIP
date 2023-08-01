import cv2
from matplotlib import pyplot as plt

try:
    # Read image from disk.
    img = cv2.imread("HV_Khuzdad.tif")

    # Canny edge detection.
    edges = cv2.Canny(img, 15, 10)

    # Write image back to disk.
    cv2.imwrite('result.tiff', edges)

except IOError:
    print('Error while reading files !!!')

plt.imshow(edges)
plt.show()
