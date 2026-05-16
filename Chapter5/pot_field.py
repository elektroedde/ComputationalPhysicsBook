import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

left_bc = -1
right_bc = 1
N = 7
V = np.zeros((N, N))

V[:, 0] = left_bc
V[:, -1] = right_bc
V[0, :] = np.linspace(left_bc, right_bc, N)
V[-1, :] = np.linspace(left_bc, right_bc, N)

n_iter = 9
frames = [V.copy()]
for _ in range(n_iter):
    Vn = V.copy()
    for i in range(1, N-1):
        for j in range(1, N-1):
            V[i, j] = 1/4 * (Vn[i-1, j] + Vn[i+1, j] + Vn[i, j-1] + Vn[i, j+1])
    frames.append(V.copy())

fig, ax = plt.subplots()
im = ax.imshow(frames[0], cmap="jet", vmin=-1, vmax=1)

def update(frame):
    im.set_data(frames[frame])
    ax.set_title(f"Frame {frame}")

ani = FuncAnimation(fig, update, frames=len(frames), interval=2000)
plt.show()