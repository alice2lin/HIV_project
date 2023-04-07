# -*- coding: utf-8 -*-
"""
Created Fri 03.31.2023 10:24:33 AM

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

# The equation is:
# V(t)=Aexp(-alpha*t)+Bexp(-beta*t)
# t is time in days
# V is viral load

time = np.linspace(0,1,101)
A = 10000
B = 90000
alpha = 100
beta = 0.1

# Calculate viral load
viral_load = A * np.exp(-alpha*time) + B * np.exp(-beta*time)

# Plot viral load
Astring = 'A =' + str(A) + '\n'
Bstring = 'B =' + str(B) + '\n'
alphastring = 'alpha =' + str(alpha) + '\n'
betastring = 'beta =' + str(beta) + '\n'
sample = Astring + Bstring + alphastring + betastring
plt.plot(time,viral_load,label=sample)
plt.xlabel('Time (days)')
plt.ylabel('Viral load')
plt.legend()


