import numpy as np
import matplotlib.pyplot as plt

#Use the shooting method to obtain the lowest six energy levels for a square well. 
#Compare the normalized wave functions with the exact solution
# Try dx = 0.05, 0.01, 0.005 for a box with walls at x = +- 1

N = 1000
nbrStates = 6
mid = int(N/2)
a = 1
x = np.linspace(-1.1*a, 1.1*a, N)
dx = x[1] - x[0]

V = np.where(np.abs(x) < 1, 0, 100000)

psi = np.zeros((N, nbrStates))
energies = np.zeros(nbrStates)
E = 1

divergence_threshold = 1.5
for state in range(nbrStates):
    even = True
    if(state % 2 != 0):
        even = False

    dE = 0.1
    last_diverge_sign = 0

    for _ in range(1000):

        diverge_sign = 0
        psi[mid, state] = 1 if even else 0
        for n in range(mid,N-1):
            if(n == mid):
                if(even):
                    psi[n+1, state] = 1 - dx**2*(E-V[n])
                else:
                    psi[n+1, state] = dx
            else:
                psi[n+1, state] = 2*psi[n, state]-psi[n-1, state] - 2*dx**2*(E-V[n])*psi[n, state]

            if(np.abs(psi[n+1, state]) > divergence_threshold):
                diverge_sign = np.sign(psi[n+1, state])
                break

        if(diverge_sign != 0 and last_diverge_sign != 0 and diverge_sign != last_diverge_sign):
            dE /= -2
        if(diverge_sign != 0):
            last_diverge_sign = diverge_sign
        if(np.abs(dE) < 1e-7):
            break

        E += dE

    energies[state] = E
    if(even):
        psi[:mid, state] = psi[mid:, state][::-1]
    else:
        psi[:mid, state] = -psi[mid:, state][::-1]

print(energies)

psi_plot = np.where(np.abs(x)[:, None] > 1, np.nan, psi)

for state in range(nbrStates):
    plt.plot(x, psi_plot[:, state], label=f"n={state+1}, E={energies[state]:.4f}")
plt.legend()
plt.show()