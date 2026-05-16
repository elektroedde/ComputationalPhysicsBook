import numpy as np
import matplotlib.pyplot as plt




theta0 = np.deg2rad(30)
#fmg = 0.5*(np.sin(4*theta) - 0.25*np.sin(8*theta) + 0.08*np.sin(12*theta) - 0.025*np.sin(16*theta))



N = 1000
pos = np.zeros((N, 3))
vel = np.zeros((N, 3))
theta = np.zeros(N)
theta[0] = theta0
dt = 0.001

m = 0.149
B2 = 4e-5*m

v0x = 1609*70/3600
vel[0] = np.array([v0x, 0, 0])
pos[0] = np.array([0, 1, 0])
g = 9.82
S0 = 4.1e-4*m
omega_0 = 0.2*np.pi*2
vd = 35
delta = 5
for i in range(1, N):
    v = np.sqrt(vel[i-1, 0]**2 + vel[i-1, 1]**2 + vel[i-1, 2]**2)
    B2 = (0.0039 + 0.0058/(1 + np.exp((v - vd)/delta)))*m



    pos[i, 0] = vel[i-1, 0]*dt + pos[i-1, 0]
    pos[i, 1] = vel[i-1, 1]*dt + pos[i-1, 1]
    pos[i, 2] = vel[i-1, 2]*dt + pos[i-1, 2]
    vel[i, 0] = -B2/m*v*vel[i-1, 0]*dt + vel[i-1, 0]
    vel[i, 1] = -g*dt + vel[i-1, 1]
    fmg = 0.5*(np.sin(4*theta[i-1]) - 0.25*np.sin(8*theta[i-1]) + 0.08*np.sin(12*theta[i-1]) - 0.025*np.sin(16*theta[i-1]))
    vel[i, 2] = fmg*g*dt + vel[i-1, 2]
    theta[i] = omega_0*dt + theta[i-1]

pos /= 0.340
plt.plot(pos[:, 0], pos[:, 2], label="z-deflection")

plt.legend()
plt.ylim([-1, 1])
plt.xlim([0, 60])
plt.show()
