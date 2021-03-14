#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('dark_background')

nsteps = 7
rad = 1
halfedge = rad/np.sqrt(2)
outerhalfedge = rad

def plot_circle():
    theta = np.linspace(0,2*np.pi,100)
    plt.plot(rad*np.cos(theta),rad*np.sin(theta))

def plot_square(a):
    x = [-a,a,a,-a,-a]
    y = [a,a,-a,-a,a]

    plt.plot(x,y)

for k in range(1,nsteps+1):
    N = 10**k
    x = 2*np.random.rand(N,2) - 1  # Generate random coordinates between -1 and 1
    r = np.linalg.norm(x,ord=2,axis=1)


    sqmask = (x[:,0] <  halfedge) & (x[:,1] < halfedge) & (x[:,0] >  -halfedge) & (x[:,1] > -halfedge)
    circmask = r <= rad
    outcircmask = r > rad
    outsqmask = circmask & (~sqmask)

    n_in_square = np.count_nonzero(sqmask)
    n_in_circle = np.count_nonzero(circmask)

    if n_in_square == 0:
        pi_est1 = 0
    else:
        pi_est1 = 2*(n_in_circle/n_in_square)
    
    pi_est2 = 4*(n_in_circle/N)
    pi_est = 0.5*(pi_est1 + pi_est2)

    fig,ax = plt.subplots(1,1,figsize=(12,10))

    plot_circle()
    plot_square(halfedge)
    plot_square(outerhalfedge)
    plt.axis('equal')
    plt.axis('off')

    ax.plot(x[:,0],x[:,1],'o',mfc='#b469ff',mec='#b469ff')
    ax.plot(x[outsqmask,0],x[outsqmask,1],'o',mfc='#9ed9d4',mec='#9ed9d4')

    ax.set_title(r"# points = $10^{%d}$, $\pi = %.3f$" %(k,pi_est),fontsize=40)

    plt.tight_layout()
    #plt.show()
    plt.savefig('pi_anim/img%02d.png' %k, dpi=150,bbox_inches='tight')
    print("%d/%d" %(k,nsteps))
    plt.close()
