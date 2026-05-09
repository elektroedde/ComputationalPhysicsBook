import numpy as np
import matplotlib.pyplot as plt
N = 100

vair = np.zeros(N)
vair2 = np.zeros(N)



vair[0] = 4
vair2[0] = 4

P = 400
m = 70
C = 1.0
rho = 1
rho2 = 0.7*rho
A = 0.33
start_time = 0
end_time = 200
dt = (end_time - start_time) / N
for i in range(1, N):

    vair[i] = vair[i-1] + dt*P/(m*vair[i-1]) - C*rho*A*vair[i-1]**2*dt/(2*m)
    vair2[i] = vair2[i-1] + dt*P/(m*vair2[i-1]) - C*rho2*A*vair2[i-1]**2*dt/(2*m)



time = np.arange(0, end_time, end_time/N)


plt.plot(time, vair, label="Air resistance")
plt.plot(time, vair2, label="Air resistance, 30% less ")
plt.title("Top speed vs air resistance")
plt.legend()
plt.show()

vconst = 13
F1 = C*rho*A*vconst**2/2
F2 = C*rho2*A*vconst**2/2

plt.bar(0, F1, label="Air resistance = 1.0")
plt.bar(1, F2, label="Air resistance = 0.7")
plt.legend()
plt.title("Energy consumed vs air resistance")
plt.show()