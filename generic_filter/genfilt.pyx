from scipy import ndimage as ndi
import numpy as np
import cython

@cython.boundscheck(False)
@cython.wraparound(False)
def _max(double [::1] arr, int n):
    cdef double m = arr[0]
    cdef Py_ssize_t i
    for i in range(1, n):
        if arr[i] > m:
            m = arr[i]
    return m


def maximum_filter(image, connectivity=1):
    fp = ndi.generate_binary_structure(image.ndim, connectivity)
    return ndi.generic_filter(image, function=_max, footprint=fp,
                              extra_arguments=(len(np.flatnonzero(fp)),))

