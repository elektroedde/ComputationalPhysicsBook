import numpy as np
import matplotlib.pyplot as plt

g = 9.8

start_time = 0
end_time = 10

N = 100
dt = (end_time - start_time) / N

v = np.zeros(N)

for i in range(1, N):
    v[i] = v[i-1] - g*dt


x = np.arange(0,10, 10/N)

plt.plot(x, v)
plt.title("Velocity due to gravity, g = 9.8 m / s^2")
plt.xlabel("Time [s]")
plt.ylabel("Velocity [m/s]")
plt.grid()
plt.xlim([0, 10])
plt.ylim([-100, 0])
plt.show()