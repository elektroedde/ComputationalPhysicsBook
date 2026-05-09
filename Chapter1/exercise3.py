import numpy as np
import matplotlib.pyplot as plt

#dv/dt = a - b*v
#a and b constants
#v is velocity

N = 100
start_time = 0
end_time = 10

dt = (end_time - start_time) / N

v = np.zeros(N)
a = 9.8
b = 1

# Model: dv/dt ≈ (v[t + dt] - v[t])/dt = a - b*v -> v[i] = a*dt - b*v*dt + v[i-1]
for i in range(1, 100):
    v[i] = a*dt - b*v[i-1]*dt + v[i-1]

time = np.arange(0, 10, 10/N)

plt.plot(time, v)
plt.show()