import pydicom 
from pydicom import dcmread
from pydicom.data import get_testdata_file
import matplotlib.pyplot as plt
from skimage import measure, morphology
from skimage.morphology import ball, binary_closing
from skimage.measure import label, regionprops
from scipy.linalg import norm
import scipy.ndimage

filename = get_testdata_file("CT_small.dcm")

ds = pydicom.dcmread(filename, force=True)

plt.imshow(ds.pixel_array, cmap=plt.cm.bone)
plt.show()
