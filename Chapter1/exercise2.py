import numpy as np
import matplotlib.pyplot as plt

# dx/dt = v
# v is constant = 40 m/s
# use Euler method to solve for x!
# we know that dx/dt ≈ (x[t+dt] - x[t])/dt
v = 40
N = 100

start_time = 0
end_time = 10
dt = (end_time - start_time) / N


x = np.zeros(N)

for i in range(1,100):
    x[i] = v*dt + x[i-1]

time = np.arange(0,10, 10/100)
plt.plot(time, x)
plt.title("Position due to constant velocity, v=40m/s")
plt.xlabel("Time [s]")
plt.ylabel("Displacement [m]")
plt.grid(which="both")
plt.show()