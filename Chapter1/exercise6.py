import numpy as np
import matplotlib.pyplot as plt

N = 1000
start_time = 0
end_time = 4
dt = (end_time - start_time) / N
a = 1
b = 0.25
Na = np.zeros(N)
Na[0] = 7

for i in range(1,N):
    Na[i] = Na[i-1] + a*Na[i-1]*dt - b*Na[i-1]**2*dt

time = np.arange(0, end_time, end_time/N)

plt.plot(time, Na)
plt.show()