import numpy as np
import matplotlib.pyplot as plt
import time


outer_bc = 0

width = 50 #cm

N = 49
charge = 1e3


factor = N/width


V = np.zeros((N, N))


V[0, :] = outer_bc
V[-1, :] = outer_bc
V[:,0] = outer_bc
V[:,-1] = outer_bc
V[10, int(N/2)] = 1


difference = []


plt.imshow(V, cmap="turbo", extent=(0, N, 0, N), origin='lower')

plt.xticks(np.linspace(0, N, N+1), minor=True)
plt.yticks(np.linspace(0, N, N+1), minor=True)
plt.grid(which="both",color="white", linewidth=0.3)
plt.show()


iterations = 0
totalnorm = 1
while totalnorm > 1e-3:
    Vn = V.copy()
    for i in range(1,N-1):
        for j in range(1,N-1):
            xten = 0
            if i == 10 and j == int(N/2):
                xten=-1
            left = V[i,j-1]
            right = 0 if j==N-2 else V[i,j+1]
            top = V[i-1, j]
            bottom = 0 if i==N-2 else V[i+1,j]
            V[i, j] = 1/4 * (top+right+left+bottom) + xten*charge
    iterations += 1
    totalnorm = (np.linalg.norm(Vn-V))
    difference.append(totalnorm)


plt.imshow(V, cmap="turbo", extent=(0, N, 0, N), origin='lower')
plt.show()





Ex = np.zeros((N, N))
Ey = np.zeros((N, N))

for i in range(1,N):
    for j in range(1,N):


        if V[i,j] != 0:
            leftV =  V[i,j-1]
            rightV = leftV if j == N-1 else V[i,j+1]
            topV = V[i-1,j]
            bottomV = topV if i == N-1 else V[i+1,j]


            Ex[i,j] = -(leftV - rightV)*N/2
            Ey[i,j] = (bottomV-topV)*N/2


Ex[1:,0] = Ex[1:,1] - (Ex[1:,2] - Ex[1:,1])
Ey[1:,0] = Ey[1:,1]

normE = np.sqrt(Ex**2 + Ey**2)
safe_norm = np.where(normE == 0, 1, normE)
Ex_unit = Ex / safe_norm
Ey_unit = Ey / safe_norm

plt.imshow(normE, cmap="turbo", extent=(0, N, 0, N), origin='lower')
plt.show()

plt.quiver(Ex_unit[::4, ::4], Ey_unit[::4, ::4])
plt.show()





