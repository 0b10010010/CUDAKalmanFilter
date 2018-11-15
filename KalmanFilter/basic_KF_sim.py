import numpy as np
from math import floor
import control
import matplotlib.pyplot as plt
import control.matlab as matlab

# continuos time system parameters (mass, spring and damper constants, F=m*xdd+bxd+kx)
m = 1
ks = 4
kd = 1
F = np.array([[0.0, 1.0], [-ks/m, -kd/m]])
G = np.array([[0.0], [1.0/m]])
H = np.array([1.0, 0.0])
J = 0
sysc = control.ss(F,G,H,J)

# initialize simulations and Kalman Filter
dt = 0.05
time = 100
tf = max(time, floor(1000*dt))
n = 0
t = np.zeros((int(tf/dt),1))
for i in np.arange(0,tf,dt):
    t[n] = i
    n+=1
nSteps = len(t)
Qc2 = 0.0005
Qd2 = Qc2/dt
w = np.sqrt(Qd2)*np.random.randn(nSteps,1)
R = 0.001
v = np.sqrt(R)*np.random.randn(nSteps,1)
X0 = [0.25, 0]
sysd = control.c2d(sysc,dt)
[Phi,Gamma,H,J] = control.ssdata(sysd)
K = np.zeros((2,nSteps))
xp = np.zeros((2,nSteps))
Pp = np.identity(2)
xp[:,0]=[0, 0]

# initialize INS/GPS
Fi = np.array([[0.0, 1.0],[0.0,0.0]])
Gi = np.array([[0],[1]])
Hi = H
Ji = 0
Qdi2 = 0.02**2
wi = np.sqrt(Qdi2)*np.random.randn(nSteps,1)
Ri = R
sysdi = control.c2d(control.ss(Fi,Gi,Hi,Ji),dt)
Phii, Gammai, Hi, Ji = control.ssdata(sysdi)
Ki = K
xpi = xp
Ppi = Pp

u = np.transpose(10*np.sin(2*np.pi*0.05*t))
yt, t, xt = matlab.lsim(sysc, w+np.transpose(u), t, X0)
xt=np.transpose(xt)
y = yt+v

accel = np.array([0, 1])@(F@xt + G*(u+np.transpose(w)))
accelmeas = accel + np.transpose(wi)

for k in range(1, nSteps):
    xm = Phi@xp[:,[(k-1)]] + Gamma*u[:,k-1]
    Pm = Phi@Pp@np.transpose(Phi) + Gamma*Qd2*np.transpose(Gamma)
    
    K[:,[k]] = Pm@np.transpose(H)*np.linalg.inv(H@Pm@np.transpose(H) + R)
    xp[:,[k]] = xm + K[:,[k]]*(y[0,k]-H*xm)
    Pp = Pm - K[:,[k]]@H@Pm

plt.plot(t,xt[0,:], label='true')
plt.plot(t, xp[0,:], label='kalman')
plt.legend()
plt.show()
