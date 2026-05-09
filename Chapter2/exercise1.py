import numpy as np
import matplotlib.pyplot as plt
N = 1000
v = np.zeros(N)


v[0] = 4

P = 400
m = 70
C = 1.0
rho = 1
A = 0.33
start_time = 0
end_time = 200
dt = (end_time - start_time) / N
for i in range(1, N):
    v[i] = v[i-1] + dt*P/(m*v[i-1])



time = np.arange(0, end_time, end_time/N)
exact_v = np.sqrt(v[0]**2 + 2*P*time/m)

plt.plot(time, v, label="No air resistance, numerical") 
plt.plot(time, exact_v, '--', label="No air resistance, exact") 



plt.legend()
plt.show()