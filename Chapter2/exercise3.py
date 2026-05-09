import numpy as np
import matplotlib.pyplot as plt

#Stokes term -B_1 v included

N = 500

v_air = np.zeros(N)
v_air2 = np.zeros(N)

v_water = np.zeros(N)
v_water2 = np.zeros(N)



v_air[0] = 4
v_air2[0] = 4
v_water[0] = 0.2
v_water2[0] = 0.2


P = 400
m = 70
C = 1.0
rho_air = 1.205
rho_water = 1000
A = 0.33
start_time = 0
end_time = 100
dt = (end_time - start_time) / N
eta_air = 2e-5
eta_water = 1e-3
h = 2.0
for i in range(1, N):

    v_air[i] = v_air[i-1] + dt*P/(m*v_air[i-1]) - C*rho_air*A*v_air[i-1]**2*dt/(2*m) - dt*v_air[i-1]*eta_air*A/(h*m)
    v_air2[i] = v_air2[i-1] + dt*P/(m*v_air2[i-1]) - C*rho_air*A*v_air2[i-1]**2*dt/(2*m)



time = np.arange(0, end_time, end_time/N)


plt.plot(time, v_air, label="Air resistance")
plt.plot(time, v_air2, label="Air resistance")
plt.legend()
plt.show()


start_time = 0
end_time = 0.5
dt = (end_time - start_time) / N
time = np.arange(0, end_time, end_time/N)


for i in range(1,N):
    v_water[i] = v_water[i-1] + dt*P/(m*v_water[i-1]) - C*rho_water*A*v_water[i-1]**2*dt/(2*m) - dt*v_water[i-1]*eta_water*A/(h*m)
    v_water2[i] = v_water2[i-1] + dt*P/(m*v_water2[i-1]) - C*rho_water*A*v_water2[i-1]**2*dt/(2*m)


plt.plot(time, v_water, label="Water 1")
plt.plot(time, v_water2, label="Water 2")
plt.legend()
plt.show()