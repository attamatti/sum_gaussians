#!/usr/bin/env python

import sys
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import math


if len(sys.argv) < 4:
    sys.exit('\nUSAGE: sum_gaussians.py <mean 1> <std 1> <height 1> ... <mean n> <std n> <height n>')
try:
    means = [float(i) for i in sys.argv[1::3]]
    stds = [float(i) for i in sys.argv[2::3]]
    pcts = [float(i) for i in sys.argv[3::3]]
except:
    sys.exit('\nUSAGE: sum_gaussians.py <mean 1> <std 1> <height 1> ... <mean n> <std n> <height n>')

def gaussian(x, mu, sig,pct):
    return pct*(np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.))))

for i in zip(means,stds,pcts):
    tmean = i[0]
    tstd = i[1]
    pct = i[2]
    x_values = np.linspace(tmean-(4*tstd), tmean+(4*tstd), 120)
    plt.plot(x_values, gaussian(x_values, tmean, tstd,pct))

def multigaussian(x, array):
    thesum = 0
    for i in array:
        pct = i[2]
        mu = i[0]
        sig = i[1]
        val = pct*(np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.))))
        thesum= thesum+val
    return(thesum)

for i in zip(means,stds,pcts):
    tmean = i[0]
    tstd = i[1]
    pct = i[2]
    x_values = np.linspace(tmean-(4*tstd), tmean+(4*tstd), 120)
    plt.plot(x_values, multigaussian(x_values, zip(means,stds,pcts)),linewidth=2.0,color='black')
    
plt.savefig('gaussians.png')
