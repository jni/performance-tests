# IPython log file


import genfilt as c
import genfilt_py as p
import numpy as np
image = np.random.rand(500, 500)
get_ipython().magic('timeit out = c.maximum_filter(image)')
get_ipython().magic('timeit out = p.maximum_filter(image)')
