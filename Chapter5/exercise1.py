import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

outer_bc = 0
inner_bc = 1
N = 30
width = N*0.15
r1 = int(np.floor(N/2 - width))
r2 = int(np.ceil(N/2 + width))


V = np.zeros((N, N))

V[:, 0] = outer_bc
V[:, -1] = outer_bc
V[0, :] =  outer_bc
V[-1, :] = outer_bc

for i in range(r1, r2):
    for j in range(r1, r2):
        V[i, j] = inner_bc



n_iter = 500
frames = [V.copy()]
for _ in range(n_iter):
    Vn = V.copy()
    for i in range(0, N):
        for j in range(0, N):
            if not (i == 0 or i == N-1 or j == 0 or j == N-1) and not (r1 <= i < r2 and r1 <= j < r2):
                V[i, j] = 1/4 * (Vn[i-1, j] + Vn[i+1, j] + Vn[i, j-1] + Vn[i, j+1])
    frames.append(V.copy())

fig, ax = plt.subplots()
im = ax.imshow(frames[0], cmap="jet", vmin=-1, vmax=1)

def update(frame):
    im.set_data(frames[frame])
    ax.set_title(f"Frame {frame}")

ani = FuncAnimation(fig, update, frames=len(frames), interval=1)
plt.show()

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

X, Y = np.meshgrid(np.arange(N), np.arange(N))
surf = ax.plot_surface(X, Y, frames[-1], cmap="jet",
                       linewidth=0, antialiased=False)



fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()