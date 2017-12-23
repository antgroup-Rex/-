#!/usr/bin/env python3

"""
Bautin bifurcation
"""

# scientific libraries
from matplotlib import pyplot as plt
from random import randint, random
import numpy as np
from scipy.integrate import odeint

# system
def bautin(X, t):
    rho, phi = X
    drho = rho*(b1 + b2*rho**2 - rho**4)
    dphi = 1
    return [drho, dphi]


# parameters
time = np.arange(0, 200, 0.01)
X0 = [[rho0, 0] for rho0 in np.arange(0.0, 1.2, 0.1)]

# figure
plt.figure(figsize=(8,8))
ax = plt.subplot(projection='polar')
ax.set_rlim(0, 1.2)
for tau in np.arange(0, 2*np.pi, 0.1):
    b1 = np.cos(tau)
    b2 = np.sin(tau)
    for x0 in X0:
        # numerical integration
        orbit = odeint(bautin, x0, time)
        rho, phi = orbit.T
        ax.plot(phi, rho, 'magenta', linewidth=0.2)
        ax.set_axis_off()
        plt.suptitle(r"$\tau = \,"+str(tau)+r"$")
        num = int(100*tau)
        if num < 10:
            plt.savefig('img00'+str(num)+'.png')
        elif num < 100:
            plt.savefig('img0'+str(num)+'.png')
        else:
            plt.savefig('img'+str(num)+'.png')
    plt.pause(1)
    ax.clear()