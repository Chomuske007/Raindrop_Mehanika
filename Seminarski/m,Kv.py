import math
import numpy as np
import matplotlib.pyplot as plt

ro = 1000.0 #kg/m^3
ni = 1.82e-5 #Ns/m^2


#inputs
d = float(input("Unesite precnik kapi(mm): ")) / 1000

#variables
mass = np.zeros(100, float)
kv = np.zeros(100, float)
R = np.zeros(100, float)

R[0] = d/100
for i in range(100 - 1):
    mass[i] = (4*math.pi/3)*((R[i]/2) ** 3) * ro
    kv[i] = 6*math.pi*ni*(R[i]/2)
    R[i + 1] = R[i] + d/100

mass[-1] = (4*math.pi/3)*((R[-1]/2) ** 3) * ro
kv[-1] = 6*math.pi*ni*(R[-1]/2)
print(f"za precnik d = {d} dobijamo \n masu m = {mass[-1]:e} i koeficijent otpora kv = {kv[-1]:e}\n")

fig, axs = plt.subplots(2, 1, figsize=(8,6)) # figsize adjusts the figure size

axs[0].plot(R, mass)
axs[0].set_xlabel("Precnik")
axs[0].set_ylabel("masa")


axs[1].plot(R, kv)
axs[1].set_xlabel("Precnik")
axs[1].set_ylabel("koeficijent otpora")

plt.tight_layout() # Adjust layout to prevent overlapping titles/labels
plt.show()

