import numpy as np
import matplotlib.pyplot as plt

#Range at sea level, no wind, ball hit at 110mph, with different angles.
#Determine within 1 degree the max range
time = 20
dt = 0.1
N = int(time/dt)
v0 = 1609*110/3600



theta = np.deg2rad(20)

def calc(v0=v0, altitude=0):
    x = np.zeros(N)
    y = np.zeros(N)
    vx = np.zeros(N)
    vy = np.zeros(N)
    #(a) Maximum range is achieved with theta = 35
    y[0] = altitude
    vx[0] = v0*np.cos(theta)
    vy[0] = v0*np.sin(theta)
    g = 9.82
    idx = 0
    a = 6.5e-3
    T0 = 300
    alpha = 2.5
    vd = 35
    delta = 5
    for i in range(1, N):
        v = np.sqrt(vx[i-1]**2 + vy[i-1]**2)
        rho = (1 - a*y[i-1]/T0)**alpha


        B2m = 0.0039 + 0.0058/(1 + np.exp((v - vd)/delta))
        Fdragx = -v*vx[i-1]*B2m
        Fdragy = -v*vy[i-1]*B2m


        x[i] = vx[i-1]*dt + x[i-1]
        y[i] = vy[i-1]*dt + y[i-1]
        vx[i] = vx[i-1] + Fdragx*dt*rho
        vy[i] = -g*dt + vy[i-1] + Fdragy*dt*rho
        idx = i



        if(y[i] < altitude):
            r = -(y[i-1] - altitude)/(y[i] - altitude)
            xl = (x[i-1] + r*x[i])/(r+1)
            x[i] = xl
            y[i] = altitude
            idx += 1
            break

    return x[:idx], y[:idx], vx[:idx], vy[:idx]




#280-300m/s for angle 20deg
v0_vec = [280]

for v0 in v0_vec:

    x, y, _, _ = calc(v0)
    plt.plot(x, y, label=f"{v0}m/s, sea level")

for v0 in v0_vec:

    x, y, _, _ = calc(v0, altitude=14110*0.3048)
    plt.plot(x, y-14110*0.3048, label=f"{v0}m/s, Pike's Peak")

plt.legend()
plt.tight_layout()
plt.show()