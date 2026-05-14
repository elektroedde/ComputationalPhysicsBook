import numpy as np
import matplotlib.pyplot as plt

#Range at sea level, no wind, ball hit at 110mph, with different angles.
#Determine within 1 degree the max range
time = 10
dt = 0.1
N = int(time/dt)
v0 = 1609*110/3600

v_wind = 1609*25/3600
theta = np.deg2rad(35)

def calc(wind, v0=v0, theta=theta):
    x = np.zeros(N)
    y = np.zeros(N)
    vx = np.zeros(N)
    vy = np.zeros(N)
    #(a) Maximum range is achieved with theta = 35

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
        v = np.sqrt((vx[i-1]-wind)**2 + vy[i-1]**2)

        B2m = 0.0039 + 0.0058/(1 + np.exp((v - vd)/delta))
        Fdragx = -v*(vx[i-1]-wind)*B2m
        Fdragy = -v*vy[i-1]*B2m


        x[i] = vx[i-1]*dt + x[i-1]
        y[i] = vy[i-1]*dt + y[i-1]
        vx[i] = vx[i-1] + Fdragx*dt
        vy[i] = -g*dt + vy[i-1] + Fdragy*dt
        idx = i

        if(y[i] < 0):
            r = -y[i-1]/y[i]
            xl = (x[i-1] + r*x[i])/(r+1)
            x[i] = xl
            y[i] = 0
            idx += 1
            break

    return x[:idx], y[:idx], vx[:idx], vy[:idx]


fig, axes = plt.subplots(2, 2, figsize=(12, 8))

ax = axes[0, 0]
x, y, _, _ = calc(0)
ax.plot(x, y)
ax.set_title("(a) Baseball trajectory, maximum range")
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")

ax = axes[0, 1]
x, y, _, _ = calc(0)
xt, yt, _, _ = calc(v_wind)
xh, yh, _, _ = calc(-v_wind)
ax.plot(x, y, label="No wind")
ax.plot(xt, yt, label="Tailwind")
ax.plot(xh, yh, label="Headwind")
ax.legend()
ax.set_title(f"(b) Baseball trajectory, wind={v_wind:.2f}m/s")
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")

ax = axes[1, 0]
x, y, _, _ = calc(0)
xt, yt, _, _ = calc(0, v0=1609*120/3600 )
xh, yh, _, _ = calc(0, v0=1609*100/3600)
ax.plot(x, y, label="v0 = 110mph")
ax.plot(xt, yt, label="v0 = 120mph")
ax.plot(xh, yh, label="v0 = 100mph")
ax.legend()
ax.set_title(f"(c) Baseball trajectory, different v0")
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")

ax = axes[1, 1]

xh, yh, vx, vy = calc(0, v0=1609*100/3600, theta=np.deg2rad(5))
ax.plot(xh, vx, label="v0 = 100mph")
ax.legend()
ax.set_title(f"(d) Fastball speed")
ax.set_xlabel("x (m)")
ax.set_ylabel("vx (m/s)")

plt.tight_layout()
plt.show()