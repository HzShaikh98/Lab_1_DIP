import rasterio
from PIL import Image
from matplotlib import pyplot as plt

a=rasterio.open("HV_Khuzdad.tif")
img = Image.open("HV_Khuzdad.tif")
width= a.width
height=a.height

num_bands = a.count

print("Image(HH) Size  (Width x Height):", width, "x", height)

print("Number of Bands of HH:", num_bands)


import matplotlib.pyplot as plt
plt.imshow(img)

import numpy as np
from PIL import Image

# Open the image
img = Image.open("HV_Khuzdad.tif")

# Convert the image to a NumPy array
img_array = np.array(img)

# Calculate image statistics
mean = np.mean(img_array)
std_dev = np.std(img_array)
min = np.min(img_array)
max = np.max(img_array)

# Print the results
print("Mean:", mean)
print("Standard Deviation:", std_dev)
print("Min:", min)
print("Max:", max)

width, height = img.size

# Print the results
print("Width:", width)
print("Height:", height)

plt.imshow(img)
plt.show()