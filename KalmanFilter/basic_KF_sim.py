import numpy as np
from math import floor
import control

# continuos time system parameters (mass, spring and damper constants, F=m*xdd+bxd+kx)
m=1
ks=4
kd=1
F=np.array([[0, 1], [-ks/m, -kd/m]])
G = np.array([[0], [1/m]])
H=np.array([1, 0])
J=0
sysc=control.ss(F,G,H,J)

# initialize simulations and Kalman Filter
T=0.05
time=20
tf=max(time, floor(1000*T))

sysd=control.c2d(sysc,T)
print(sysd)
