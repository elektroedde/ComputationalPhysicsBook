import numpy as np
import matplotlib.pyplot as plt
N = 100
v = np.zeros(N)


v[0] = 0

P = 400
m = 70
C = 1.0
rho = 1
rho2 = 0.85*rho
A = 0.33
start_time = 0
end_time = 200
dt = (end_time - start_time) / N

F0 = P/7
for i in range(1, N):
    if(v[i-1] < 7):
        v[i] = v[i-1] + F0*dt/m - C*rho*A*v[i-1]**2*dt/(2*m)
    else:
        v[i] = v[i-1] + dt*P/(m*v[i-1])- C*rho*A*v[i-1]**2*dt/(2*m)




time = np.arange(0, end_time, end_time/N)

plt.plot(time, v, label="")


plt.legend()
plt.show()