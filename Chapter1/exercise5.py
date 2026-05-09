import numpy as np
import matplotlib.pyplot as plt

#dNA / dt = Nb/tau - Na/tau

N = 100
start_time = 0
end_time = 10
tau = 1
dt = end_time / N
Na = np.zeros(N)
Nb = np.zeros(N)

Na[0] = 100

for i in range(1, 100):
    Na[i] = Na[i-1] + Nb[i-1]*dt/tau - Na[i-1]*dt/tau
    Nb[i] = Nb[i-1] + Na[i-1]*dt/tau - Nb[i-1]*dt/tau


time = np.arange(0, end_time, end_time/N)

plt.plot(time, Na)
plt.plot(time, Nb)
plt.show()                                                                                                                                                                                                                                                                                                      