# IPython log file

n = int(1e6)
import alloc as a
for func in filter(lambda f: f.startswith('alloc'), dir(a)):
    print('timing function:', func)
    get_ipython().magic('timeit out = a.%s(n)' % func)
