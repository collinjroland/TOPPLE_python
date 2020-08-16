# -*- coding: utf-8 -*-
"""
Make bluff -- creates 2D cross section of bluff geometry
Based on makebluff.m by K. Barnhart (https://github.com/kbarnhart/topple)

Created on Sun Aug 16 11:52:19 2020

@author: colli
"""

import numpy as np
import matplotlib.pyplot as mpl

def makebluff(deltax, xmax, bluff_edge, bluff_height, shelf_slope, beach_slope, beach_length):

    x = np.arange(0,xmax+deltax,deltax)
    a = np.argwhere(x<bluff_edge)
    b = np.max(a)+1
    c_all = np.argwhere(x<(bluff_edge+beach_length))
    c = np.max(c_all)+1
    
    z = np.zeros_like(x)
    z[a] = bluff_height
    
    x_end = len(x)
    
    if c<np.size(x):
        z[b:c+1] = np.linspace(z[b], (z[b]+(x[c]-x[b])*beach_slope), c-b+1)
        z[c:] = np.linspace(z[c], (z[c]+(x[x_end-1]-x[c])*shelf_slope), len(z)-c)
    else:
        z[b:] = np.linspace(z[b], (z[b]+(x[x_end-1]-x[b])*beach_slope), len(z)-b)
        
    xnew = np.arange(0,xmax+(deltax/10),(deltax/10))
    znew = np.interp(xnew,x,z)
    
    # now, get rid of all of the unnecessary points

    blufftop_all=np.argwhere(znew==bluff_height)
    blufftop = np.max(blufftop_all)+1

    index = np.arange(1,blufftop-1,1)
    xnew = np.delete(xnew,index);
    znew=np.delete(znew,index);

    beachend_all=np.argwhere(xnew>bluff_edge+beach_length)
    beachend = np.min(beachend_all)

    index = np.arange(beachend+10,len(xnew)-1,1)
    xnew = np.delete(xnew,index);
    znew= np.delete(znew,index);