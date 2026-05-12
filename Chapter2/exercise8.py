import numpy as np
import matplotlib.pyplot as plt

N = 100


start_time = 0
end_time = 130
dt = (end_time - start_time) / N
g = 9.82
vi = 700

G = 6.67430e-11
m_earth = 5.9722e24
r_earth = 6.371e6

def calculate(t):
    x = np.zeros(N)
    y = np.zeros(N)
    y_dynG = np.zeros(N)
    vx = np.zeros(N)
    vy = np.zeros(N)
    vy_dynG = np.zeros(N)

    theta = np.deg2rad(t)
    vx[0] = vi*np.cos(theta)
    vy[0] = vi*np.sin(theta)
    vy_dynG[0] = vi*np.sin(theta)

    i = 0
    while i < N - 1:
        x[i+1] = x[i] + vx[i] * dt
        y[i+1] = y[i] + vy[i] * dt
        y_dynG[i+1] = y_dynG[i] + vy_dynG[i] * dt

        newg = G*m_earth/(r_earth+y[i+1])**2
        print(newg)


        vx[i+1] = vx[i]
        vy[i+1] = vy[i] - g * dt
        vy_dynG[i+1] = vy_dynG[i] - newg * dt
        i += 1
        if y[i] < 0:
            break



    r = -y[i-1]/y[i]
    xl = (x[i-1] + r*x[i])/(r+1)
    x[i] = xl

    plt.plot(x[:i+1]/1000, y[:i+1]/1000, label=f"Theta = {t}\xb0")
    plt.plot(x[:i+1]/1000, y_dynG[:i+1]/1000, label="Dynamic gravity")


angles = [45]
for angle in angles:
    calculate(angle)

plt.legend()
plt.xlabel("x [km]")
plt.ylabel("y [km]")
plt.ylim([0, 20])
plt.show()