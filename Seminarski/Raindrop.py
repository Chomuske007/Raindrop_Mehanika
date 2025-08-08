import math
import matplotlib.pyplot as plt
import numpy as np

#simulating raindrop velocity change
#Formulas
#V = 4pi/3 * r^3
#G = -m*g where g = 9.81 m/s^2
#Fd = -kv*v(t) - air resistance
#a = -g -kv/m * v
#v(t + dt) = v(t) + dt*a(t, v(t))

#const
g = 9.81 # m/s^2
ni = 1.82e-5    # Ns/m^2
water_density = 1000 # kg/m^3
dt = 0.001

#inputs
diameter = float(input("Input diameter of raindrop: ")) # milimetres
time = int(input("Input the time: "))

#variables
r = (diameter/2)/1000 # diameter/2 put into metres
mass = 4/3 * math.pi * (r ** 3) * water_density # kg
kv = 6*math.pi*r*ni
n = int(round(time/dt))
vt = mass*g/kv

#arrays
t = np.zeros(n, float)
v = np.zeros(n, float)
a = np.zeros(n, float)

#simulation
for i in range(n-1):
    a[i] = g - (kv/mass)*v[i]
    v[i+1] = v[i] + dt*(a[i])
    t[i+1] = t[i] + dt
a[n-1] = g - (kv/mass)*v[n-1]

fig, axs = plt.subplots(2, 1, figsize=(8,6)) # figsize adjusts the figure size

#Plot on the second subplot (axs[0])
axs[0].plot(t, a, color='red')
axs[0].grid()
axs[0].axhline(y = a[-1], color = 'black', linestyle = '--', lw = 0.8)
axs[0].set_title('Raindrop Acceleration')
axs[0].set_xlabel('Time-axis[s]')
axs[0].set_ylabel('Acceleration-axis[m/s^2]')

#Plot on the first subplot (axs[1])
axs[1].plot(t, v)
axs[1].grid()
axs[1].axhline(y = v[-1], color = 'black', linestyle = '--', lw = 0.8)
axs[1].set_title('Raindrop Velocity')
axs[1].set_xlabel('Time-axis[s]')
axs[1].set_ylabel('Velocity-axis[m/s]')

plt.tight_layout() # Adjust layout to prevent overlapping titles/labels
plt.show()
