from scipy import ndimage as ndi
import numpy as np

def _max(arr, n):
    m = arr[0]
    for i in range(1, n):
        if arr[i] > m:
            m = arr[i]
    return m


def maximum_filter(image, connectivity=1):
    fp = ndi.generate_binary_structure(image.ndim, connectivity)
    return ndi.generic_filter(image, function=_max, footprint=fp,
                              extra_arguments=(len(np.flatnonzero(fp)),))

