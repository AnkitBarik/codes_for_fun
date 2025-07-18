#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

def isprime(n):
    
    if n in [0,1]:
        return False
    for i in range(2,int(np.sqrt(n))+1):
        if n%i == 0:
            return False

    return True

N = 1000000

n_per_cpu = int(N/size)

dat_arr = None
isp_arr = None

if rank == 0:
    dat_arr = np.arange(N)
    isp_arr = np.zeros_like(dat_arr,dtype=bool)

dat_recvbuf = np.empty(n_per_cpu, dtype=int)
isp_recvbuf = np.empty(n_per_cpu, dtype=int)
comm.Scatter(dat_arr,dat_recvbuf,root=0)
comm.Scatter(isp_arr,isp_recvbuf,root=0)

for i in range(n_per_cpu):
    isp_recvbuf[i] = isprime(dat_recvbuf[i])

comm.Gather(isp_recvbuf,isp_arr) 

if rank == 0:

    for k in range(N):
        if isp_arr[k]:
            n = dat_arr[k]
        
#Polar plot, r,\theta = p,p
            x = n * np.cos(n)
            y = n * np.sin(n)

            ax.plot(x,y,'go',ms=0.5)

ax.set_aspect('equal')
ax.axis('off')
plt.title("N = %d" %N)
plt.show()
