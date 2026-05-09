import numpy as np
import matplotlib.pyplot as plt
N = 100
v = np.zeros(N)
vair = np.zeros(N)

v[0] = 4
vair[0] = 4
P = 400
m = 70
C = 1
rho = 1
A = 0.33
start_time = 0
end_time = 200
dt = (end_time - start_time) / N
for i in range(1, N):
    v[i] = v[i-1] + dt*P/(m*v[i-1])
    vair[i] = vair[i-1] + dt*P/(m*vair[i-1]) - C*rho*A*vair[i-1]**2*dt/(2*m)


time = np.arange(0, end_time, end_time/N)

plt.plot(time, v)
plt.plot(time, vair)
plt.show()