import numpy as np
import matplotlib.pyplot as plt
N = 100

vair = np.zeros(N)
vhill = np.zeros(N)

vair[0] = 4
vhill[0] = 4

slope = -12 #degrees
P = 400
m = 70
C = 1.0
rho = 1
rho2 = 0.85*rho
A = 0.33
start_time = 0
end_time = 200
dt = (end_time - start_time) / N
g = 9.82
for i in range(1, N):

    vair[i] = vair[i-1] + dt*P/(m*vair[i-1]) - C*rho*A*vair[i-1]**2*dt/(2*m)
    vhill[i] = vhill[i-1] + dt*P/(m*vhill[i-1]) - C*rho*A*vhill[i-1]**2*dt/(2*m) - g*np.sin(np.deg2rad(slope))*dt





time = np.arange(0, end_time, end_time/N)


plt.plot(time, vair, label="Air resistance")
plt.plot(time, vhill, label="Hill")




plt.legend()
plt.show()