import numpy as np
import matplotlib.pyplot as plt

t_max = 5.0
tau = 1.0
delta_t = [0.05, 0.2, 0.5]


for dt in delta_t:
    N = t_max*tau/dt
    N_u = np.zeros(int(N))
    N_u[0] = 100


    for i in range(1, int(N)):
        N_u[i] = N_u[i-1] - N_u[i-1]*dt/tau

    time = np.linspace(0, 5, int(N))
    plt.scatter(time, N_u, label=f"Time step: {dt}")



plt.legend()
plt.show()