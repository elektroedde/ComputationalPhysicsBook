import numpy as np
import matplotlib.pyplot as plt

mu_0 = 4*np.pi*1e-7
L = 10  # m

#? Field function
def magfield(x, z):
    return x/(np.sqrt(x**2+z**2)**3)

#! Rectangle sum visualization
dz = 2
z_num = np.linspace(-L+dz/2, L-dz/2, int(2*L/dz))
z_ana = np.linspace(-L, L, 1000)


p = 10
z_num_func = magfield(p, z_num)
z_ana_func = magfield(p, z_ana)

plt.plot(z_ana, z_ana_func, label="Analytical function")
plt.scatter(z_num, z_num_func, label="Numerical points", color="r", zorder=2)
plt.title("Analytical function and the integration points")
plt.legend()
plt.show()

plt.bar(z_num, z_num_func, width=dz*0.98, label="Integration rectangles", color="r")
plt.plot(z_ana, z_ana_func, label="Analytical function")
plt.legend()
plt.title("The approximate integral of the function")
plt.show()


#! Integral of Analytical, Rectangle and Simpson
xs = 0.05
xe = 0.2
xnp = 50

x_num = np.linspace(xs, xe, xnp)

dz_num = 0.1
z_rect = np.linspace(-L+dz_num/2, L-dz_num/2, int(2*L/dz_num))

dz_ana = 2*L/1000
x_ana = np.linspace(xs, xe, 1000)
z_ana = np.linspace(-L, L, 1000)


B_rect = np.zeros(x_num.shape)
for i, xpos in enumerate(x_num):
    B_rect[i] = np.sum(dz_num*magfield(xpos, z_rect))

B_analytical = np.zeros(1000)
for i, xpos in enumerate(x_ana):
    B_analytical[i] = np.sum(dz_ana * magfield(xpos, z_ana))



plt.show()
z_simp = np.linspace(-L,L,int(2*L/dz_num))
B_simp = np.zeros(x_num.shape)
for (i, xpos) in enumerate(x_num):

    B_simp[i] += np.sum(dz_num/6 * (magfield(xpos, z_simp)
                           + 4*magfield(xpos, z_simp+dz_num/2)
                           + magfield(xpos, z_simp+dz_num)))

plt.scatter(x_num, B_simp, color="g", zorder=3, label="Simpson Integration")
plt.scatter(x_num, B_rect, color="r", label="Rectangular Integration")
plt.plot(x_ana, B_analytical, label="Analytical Integration")
plt.legend()
plt.show()
