"""IPython timer for module f.

Run this file with ``python itimer.py``.
"""
import timeit

n = int(1e6)
num_exec = 1
import f

for func in filter(lambda f: f.startswith('loop'), sorted(dir(f))):
    print('====== timing function:', func)
    print(getattr(f, func).__doc__)
    # t: seconds taken to execute `stmt` `num_exec` times.
    t = timeit.timeit(stmt='f.%s(n)' % func,
                      number=num_exec, globals=globals())
    # execution time in ns
    per_loop = round(t / n * 1e9)
    print('time: %ins.\ntheoretical max bandwidth: %.2fMB/s' %
          (per_loop, 1000 / per_loop))
