# import rasterio
from matplotlib import pyplot as plt
from rasterio.plot import show
# import rasterio
import geotiff
import tifffile
from PIL import Image
img = Image.open("HH_Khuzdad.tif")
show(img)
pixels = img.load()
plt.show()