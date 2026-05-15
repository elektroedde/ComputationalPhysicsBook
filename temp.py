import numpy as np
import matplotlib.pyplot as plt

vd = 35
delta = 5

vmax = 1609*200/3600
v = np.linspace(0, vmax)
B2m = 0.0039 + 0.0058/(1 + np.exp((v - vd)/delta))

plt.plot(v*3600/1609, B2m)
plt.show()