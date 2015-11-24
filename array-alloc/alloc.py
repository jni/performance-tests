import numpy as np


def alloc_broadcast(n):
    steps = np.random.randint(-50, 50, size=6).astype(np.int64)
    indices = np.arange(n, dtype=np.int64)[:, np.newaxis]
    ns_all = indices + steps
    for i in indices:
        ns = ns_all[i]


def alloc_in_loop(n):
    steps = np.random.randint(-50, 50, size=6).astype(np.int64)
    for i in np.arange(n):
        ns = i + steps


def alloc_out_loop(n):
    steps = np.random.randint(-50, 50, size=6).astype(np.int64)
    ns = np.empty_like(steps)
    for i in np.arange(n):
        ns[:] = i + steps


def alloc_cp(n):
    steps = np.random.randint(-50, 50, size=6).astype(np.int64)
    ns = np.empty_like(steps)
    for i in np.arange(n):  # i is float
        np.copyto(ns, steps)
        ns += i


def alloc_cp_same(n):
    steps = np.random.randint(-50, 50, size=6).astype(np.int64)
    ns = np.empty_like(steps)
    for i in np.arange(n, dtype=np.int64):
        np.copyto(ns, steps)
        ns += i
