import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.animation import FuncAnimation

# Lorentz equation
def lorentz(X, t, B, J):
    v = X[3:6]                      #6 columns 3 spacial positions and 3 velocity components
    drdt = v                        # velocity
    dvdt = J * np.cross(v, B)+J*E       # lorentz equation
    return np.hstack((drdt, dvdt))

# Constants
N = 10  # Number of turns
mu = 1  # Magnetic permeability
I = 1  # Ampere
l = 1  # Meter
B = np.array([0, 0, 1]) * N * mu * I / l
E=np.array([10,0,0])

J = -1.7588*10**1  # e/m not real value
x0 = np.array([0, 0, 0])  # Initial position
v0 = np.array([10, 0, 0])  # Initial velocity

t = np.linspace(0, 3, 90)  # Time

Origin = np.hstack((x0, v0)) 
sol = odeint(lorentz, Origin, t, args=(B, J), mxstep=1000)

# Animation parameters
r = 0.1  # Radius of the particle

fig, ax = plt.subplots(figsize=(16, 6))
particle1 = Circle((0, 0), radius=r, color='b')
ax.add_patch(particle1)
ax.set_xlim([-4, 4*4])
ax.set_ylim([-4, 4])

# Animation function
def animate(frame):
    x, y, z, _, _, _ = sol[frame]
    
    particle1.set_center((x, y))
    return particle1,

# Create the animation
ani = FuncAnimation(fig, animate, frames=len(t), interval=100, blit=True)

plt.show()
