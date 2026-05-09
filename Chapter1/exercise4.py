import numpy as np
import matplotlib.pyplot as plt

#dNa/dt = - Na/taua
#dNb/dt = Na/tau_a - Nb/tau_b

N = 1000
start_time = 0
t_a = 1.0
t_b = 10
end_time = 10 
dt = (end_time - start_time) / N
Na = np.zeros(N)
Nb = np.zeros(N)
Na[0] = 1000.0  # initial population
Nb[0] = 1000.0


for i in range(1, N):
    Na[i] = Na[i-1] - dt*Na[i-1]/t_a
    Nb[i] = Nb[i-1] + dt*Na[i-1]/t_a - dt*Nb[i-1]/t_b

time = np.linspace(start_time, end_time, N)
theoretical = Na[0] * np.exp(-time/t_a)

plt.plot(time, Na)
plt.plot(time, theoretical)
plt.plot(time, Nb)

plt.show()