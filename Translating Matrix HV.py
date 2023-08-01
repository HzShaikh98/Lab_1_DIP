# Let's shift by (100, 50).
import cv2
import numpy as np
from matplotlib import pyplot as plt

M = np.float32([[1, 0, 100], [0, 1, 50]])
try:
    # Read image from disk.
    img = cv2.imread("HV_Khuzdad.tif")

    # warpAffine does appropriate shifting given the
    # translation matrix.
    res2 = cv2.warpAffine(img, M, (55, 90))

    # Write image back to disk.
    cv2.imwrite('result.tiff', res2)

except IOError:
    print('Error while reading files !!!')

plt.imshow(res2)
plt.show()