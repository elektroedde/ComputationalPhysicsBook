import numpy as np
import matplotlib.pyplot as plt
import time


outer_bc = 0
inner_bc = 1e5
width = 50 #cm
rod_separation = 2 #cm
N = 50
M = 25

factor = N/width


V = np.zeros((N, M))


V[0, :] = outer_bc


difference = []
V[rod_separation + 1:, -1] = inner_bc

plt.matshow(V, cmap="turbo", extent=(0, M, 0, N))

plt.xticks(np.linspace(0, M, M+1), minor=True)
plt.yticks(np.linspace(0, N, N+1), minor=True)
plt.grid(which="both",color="white", linewidth=0.3)
plt.show()


iterations = 0
totalnorm = inner_bc
while totalnorm > inner_bc*1e-3:
    Vn = V.copy()
    for i in range(1,N):
        for j in range(0,M):
            if(V[i,j] != inner_bc):
                left = V[i,j] if j == 0 else V[i,j-1]
                right = left if j==M-1 else V[i,j+1]
                top = V[i-1, j]
                bottom = top if i==N-1 else V[i+1,j]
                V[i, j] = 1/4 * (top+right+left+bottom)
    iterations += 1
    totalnorm = (np.linalg.norm(Vn-V))
    difference.append(totalnorm)


plt.matshow(V, cmap="turbo", extent=(0, M, 0, N))


plt.show()





Ex = np.zeros((N, M))
Ey = np.zeros((N, M))

for i in range(1,N):
    for j in range(1,M):
        #Neumann conditions on left,right,bottom

        if V[i,j] != inner_bc:
            leftV =  V[i,j-1]
            rightV = leftV if j == M-1 else V[i,j+1]
            topV = V[i-1,j]
            bottomV = topV if i == N-1 else V[i+1,j]


            Ex[i,j] = -(leftV - rightV)*N/2
            Ey[i,j] = (bottomV-topV)*M/2


Ex[1:,0] = Ex[1:,1] - (Ex[1:,2] - Ex[1:,1])
Ey[1:,0] = Ey[1:,1]

normE = np.sqrt(Ex**2 + Ey**2)




plt.matshow(normE, cmap="turbo", extent=(0, M, 0, N))


plt.show()

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
X, Y = np.meshgrid(np.arange(M), np.arange(N,0,-1))
surf = ax.plot_surface(X, Y, normE, cmap="turbo",
                       linewidth=0, antialiased=False)

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

