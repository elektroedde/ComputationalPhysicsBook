import numpy as np
import matplotlib.pyplot as plt

#d^2V/dx^2 = - rho/epsilon_0

N = 55
V = np.zeros((N, N, N))
rho = V.copy()

mid = int(N/2)
print(mid)
rho[mid, mid, mid] = 1

for _ in range(20):
    for i in range(1, N-1):
        for j in range(1, N-1):
            for k in range(1, N-1):
                Vn = V.copy()
                V[i,j,k] = 1/6 * (V[i-1,j,k] + V[i+1,j,k] + V[i,j-1,k] + V[i,j+1,k] + V[i,j,k-1] + V[i,j,k+1] + rho[i,j,k])


#plt.imshow(V[:, :, mid], cmap="jet")
plt.plot(np.linspace(mid, N, mid+1), V[mid:, mid, mid])
plt.show()