import numpy as np
import matplotlib.pyplot as plt
import time


outer_bc = 0
inner_bc = 1
width = 50 #cm
N = 50
prism_width = width*0.3
r1 = int(np.floor((N*0.7)))

V = np.zeros((N, N))
Ex = np.zeros((N, N))
Ey = np.zeros((N, N))

V[:, 0] = outer_bc
V[0, :] = outer_bc


for i in range(r1, N):
    for j in range(r1, N):
        V[i, j] = inner_bc

starttime = time.time()
for _ in range(1000):
    for i in range(N):
        for j in range(i, N):
            if  (i != 0 and j != 0 and (i < r1 or j < r1)):
                left = V[i,j-1]
                right = left if j==N-1 else V[i,j+1]
                top = V[i-1, j]
                bottom = V[i+1,j]
                #If we are on the right edge, symmetry
                if(j==N-1):
                    V[i, j] = 1/4 * (top + bottom + 2*left)
                #If we are on the slope, symmetry
                elif(i==j):
                    V[i, j] = 1/4 * (2*top+ 2*right)
                else:
                    V[i, j] = 1/4 * (top+right+left+bottom)




V[:r1, :r1] += np.triu(V[:r1, :r1],1).transpose()


V[r1:N,:r1] += V[:r1, r1:N].transpose()
endtime = time.time() - starttime


#(0,N),#!(0,N):
#Add 0 rows before, N rows after
#!Add 0 columns before, N columns after
V=np.pad(V,((0,N-1),(0,N-1)),'reflect')


print(f"{endtime*1000:.0f}ms")
plt.imshow(V, cmap="jet", extent=(0,width,0,width))
plt.title("Electric Potential")
plt.xlabel("x [cm]")
plt.ylabel("y [cm]")
plt.colorbar(cmap="jet")

plt.show()