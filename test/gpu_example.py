#! /usr/bin/env python

import numpy as np
from timeit import default_timer as timer
from numba import vectorize

@vectorize(["float32(float32, float32)"], target='cuda')
def VectorAdd_GPU(a, b):
    return a + b

def VectorAdd_CPU(a, b, c):
    for i in range(a.size):
        c[i] = a[i] + b[i]

def main():
    N = 3200000
    
    A = np.ones(N, dtype=np.float32)
    B = np.ones(N, dtype=np.float32)
    C = np.zeros(N, dtype=np.float32)
    
    start = timer()
    VectorAdd_CPU(A, B, C)
    vectoradd_cpu_time = timer() - start

    start = timer()
    C = VectorAdd_GPU(A, B)
    vectoradd_gpu_time = timer() - start
    
    print("VectorAdd_CPU took %f seconds" % vectoradd_cpu_time)
    print("VectorAdd_GPU took %f seconds" % vectoradd_gpu_time) 

if __name__ == '__main__':
    main()
