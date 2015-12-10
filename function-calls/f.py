"""f.py: A module to benchmark Python function call overhead.
"""

def f():
    pass

def g(*args, **kwargs):
    pass


def loop_0_empty(n):
    """Run empty loop n times."""
    for i in range(n):
        pass


def loop_1_f(n):
    """Run loop with empty function n times."""
    for i in range(n):
        f()

def loop_2_f_twice(n):
    """Run loop calling empty function twice per loop, n times."""
    for i in range(n):
        f()
        f()

def loop_3_g(n):
    """Run loop with empty function taking args, n times."""
    for i in range(n):
        g()

def loop_4_g_twice(n):
    """Run loop with empty function taking args, twice per loop, n times."""
    for i in range(n):
        g()
        g()

def loop_5_g_arg(n):
    """Run loop with empty function passing an arg, n times."""
    for i in range(n):
        g(n)

def loop_6_g_kwarg(n):
    """Run loop with empty function passing a kwarg, n times."""
    for i in range(n):
        g(n=n)
