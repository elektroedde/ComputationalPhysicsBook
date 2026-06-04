import numpy as np
import matplotlib.pyplot as plt
import time


outer_bc = 0
inner_bc = 1
width = 50 #cm
N = 50

factor = N/width
plate_position = int(40*factor)
plate_thickness = int(3*factor)
plate_height = int(5*factor)

V = np.zeros((N, N))


V[:, 0] = outer_bc
V[0, :] = outer_bc

difference = []
V[-plate_height*2:, plate_position-plate_thickness:plate_position+plate_thickness] = inner_bc

plt.imshow(V)
plt.show()
starttime = time.time()
iterations = 0
totalnorm = 1
while totalnorm > 1e-5:
    Vn = V.copy()
    for i in range(1,N):
        for j in range(1,N):
            if(V[i,j] != 1):
                left = V[i,j-1]
                right = -left if j==N-1 else V[i,j+1]
                top = V[i-1, j]
                bottom = top if i==N-1 else V[i+1,j]
                #If we are on the right edge, symmetry

                V[i, j] = 1/4 * (top + bottom + 2*left)
                V[i, j] = 1/4 * (2*top + left + right)
                V[i, j] = 1/4 * (top+right+left+bottom)
    iterations += 1
    totalnorm = (np.linalg.norm(Vn-V))
    difference.append(totalnorm)



plt.plot(np.arange(iterations), difference)
plt.show()
endtime = time.time() - starttime

#(0,N),#!(0,N):
#Add 0 rows before, N rows after
#!Add 0 columns before, N columns after
V=np.pad(V,((0,N-1),(0,0)),'reflect')
Vright = -V[:, :N-1]
Vright = np.fliplr(Vright)
V = np.concatenate((V, Vright), axis=-1)

M = 2*N - 1
Ex = np.zeros((M, M))
Ey = np.zeros((M, M))
for i in range(M):
    for j in range(M):
        leftV = 0 if j == 0 else V[i,j-1]
        rightV = 0 if j == M-1 else V[i,j+1]
        topV = 0 if i == 0 else V[i-1,j]
        bottomV = 0 if i == M-1 else V[i+1,j]
        Ex[i,j] = (leftV - rightV)*M/2
        Ey[i,j] = (bottomV-topV)*M/2

plt.imshow(Ex)
plt.show()
plt.imshow(Ey)
plt.show()

normE = np.sqrt(Ex**2 + Ey**2)

plt.imshow(normE)
plt.colorbar()
plt.show()
print(f"{endtime*1000:.0f}ms")
plt.matshow(V, cmap="turbo", extent=(0,width,0,width))
plt.title("Electric Potential")
plt.xlabel("x [cm]")
plt.ylabel("y [cm]")
plt.colorbar(cmap="turbo")

plt.show()

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
X, Y = np.meshgrid(np.arange(M), np.arange(M))
surf = ax.plot_surface(X, Y, V, cmap="turbo",
                       linewidth=0, antialiased=False)

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

