import numpy as np
import matplotlib.pyplot as plt

#Use adiabatic model, rho = rho_0(1 - ay/T0)^alpha
a = 6.5e-3
alpha = 2.5
T0 = 300


N = 100


start_time = 0
end_time = 130
dt = (end_time - start_time) / N
g = 9.82
vi = 700

B2m = 4e-5
def calculate(t):
    x = np.zeros(N)
    y = np.zeros(N)
    vx = np.zeros(N)
    vy = np.zeros(N)
    theta = np.deg2rad(t)
    vx[0] = vi*np.cos(theta)
    vy[0] = vi*np.sin(theta)

    i = 0
    while i < N - 1:
        x[i+1] = x[i] + vx[i] * dt
        y[i+1] = y[i] + vy[i] * dt
        drag = (1 - a*y[i+1]/T0)**alpha
        v = np.sqrt(vx[i]**2 + vy[i]**2)
        vx[i+1] = vx[i] - B2m*drag*v*vx[i]*dt
        vy[i+1] = vy[i] - g * dt - B2m*drag*v*vy[i]*dt
        i += 1
        if y[i] < 0:
            break



    r = -y[i-1]/y[i]
    xl = (x[i-1] + r*x[i])/(r+1)
    print(xl)
    x[i] = xl

    plt.plot(x[:i+1]/1000, y[:i+1]/1000, label=f"Theta = {t}\xb0")

angles = [35, 45]
for angle in angles:
    calculate(angle)

plt.legend()
plt.xlabel("x [km]")
plt.ylabel("y [km]")
plt.ylim([0, 10])
plt.xlim([0, 30])
plt.show()