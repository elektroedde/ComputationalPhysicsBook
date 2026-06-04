import numpy as np
import matplotlib.pyplot as plt
import time


outer_bc = 0
inner_bc = 1
width = 50 #cm
N = 50

plate_thickness = 3
plate_height = 5
factor = int(width/N)



separations = 18



difference = []
fringing = []


starttime = time.time()


for i in range(separations):
    plate_position = 30 + 1*i
    V = np.zeros((N, N))

    V[:, 0] = outer_bc
    V[0, :] = outer_bc
    V[-plate_height*2:, plate_position-plate_thickness:plate_position] = inner_bc
    totalnorm = 1

    while totalnorm > 1e-2:
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

        totalnorm = (np.linalg.norm(Vn-V))
        difference.append(totalnorm)

    fringing.append(np.linalg.norm(V[:N-plate_height*2,:]))





plt.plot(30 + np.arange(separations), fringing)
plt.show()
endtime = time.time() - starttime

#(0,N),#!(0,N):
#Add 0 rows before, N rows after
#!Add 0 columns before, N columns after
V=np.pad(V,((0,N),(0,0)),'reflect')
Vright = -V
Vright = np.fliplr(Vright)
V = np.concatenate((V, Vright), axis=-1)



print(f"{endtime*1000:.0f}ms")
plt.matshow(V, cmap="turbo", extent=(0,width,0,width))
plt.title("Electric Potential")
plt.xlabel("x [cm]")
plt.ylabel("y [cm]")
plt.colorbar(cmap="turbo")

plt.show()

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
X, Y = np.meshgrid(np.arange(N*2), np.arange(N*2))
surf = ax.plot_surface(X, Y, V, cmap="turbo",
                       linewidth=0, antialiased=False)

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

