import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math
from utility_functions import Calc_L,d_n, cartesian_to_polar



# ---------------------  Loading Dipole, EEG sensor Cordinates -----------------------
# TODO: Load sensor coordinates data
# data2 = ...

# TODO: Define dipole parameters
# theta_0 = ...
# phi_0 = ...
# radius = ...

# TODO: Convert dipole position from spherical to Cartesian coordinates
# x = ...
# y = ...
# z = ...

# TODO: Define dipole moment vector and position
# q = ...
# rq = ...

# TODO: Extract sensor coordinates
# r_x = ...
# r_y = ...
# r_z = ...

# TODO: Convert sensor coordinates from Cartesian to spherical
# r, theta, phi = ...

# -----------------------------------------------  Constants ---------------------------------------------------------

m = 33       # Number of EEG Sensor
n = 1      # Number of Dipole
R0 = 0.07
R1 = 0.08
R2 = 0.085
R3 = 0.09

sigma = 0.3
sg1 = sigma
sg2 = sigma/80
sg3 = sigma

ep = 8.85 * pow(10, -7)
mu = 4 * math.pi * pow(10, -7)

# --------------------------------------------  Create EEG Laed_Field  -------------------------------------------------------

# TODO: Define function to calculate lead field components for a sensor-dipole pair
# def Calc_L():

    # Calculate the lead field components using the formula
    # return a_ij

# TODO: Define function to calculate d_n coefficient for the three-sphere model
# def d_n():
    # Apply the formula for d_n coefficient
    # return dn

# TODO: Initialize the EEG lead field matrix L
# L = 

# TODO: Define conductivity ratio
# xi = 
# b = 

# TODO: Calculate EEG lead field matrix components
# for i in range():
#     # k =  
#     for j in range():
#     . . .

# ------------------------  Calculate EEG Voltage of sensors  ------------------------

# TODO: Calculate the electric potential at each sensor
# V = ...

# TODO: Save the EEG lead field matrix
# np.savez("EEG_Lead_Field.npz", L=L)


# -------------------------------------  Visiualize EEG sensor ------------------------------------------

fig = plt.figure(figsize=(9, 6))
ax = fig.add_subplot(111, projection='3d')

# Set size of each axis
ax.set_box_aspect([1, 1, 1])  # This will make the axes equally spaced
ax.set_xlim([-0.11, 0.11])
ax.set_ylim([-0.11, 0.11])
ax.set_zlim([-0.11, 0.11])

# Set the grid grading for each axis
ax.set_xticks(np.arange(-0.1, 0.1, 0.04))
ax.set_yticks(np.arange(-0.1, 0.1, 0.04))
ax.set_zticks(np.arange(-0.1, 0.1, 0.04))
plt.title('Voltage value of sensors') 

vmin = np.min(V)
vmax = np.max(V)

# Plotting scatter with actual values
scatter = ax.scatter(r_x, r_y, r_z, c=V, cmap='hot', s=50, vmin=vmin, vmax=vmax)

# Adding color bar
cbar = plt.colorbar(scatter)
cbar.set_label('|V|')

for i in range(m):
    ax.text(r_x[i], r_y[i], r_z[i], f'{i+1}', color='black', fontsize=8)

ax.quiver(rq[0], rq[1], rq[2], q[0], q[1], q[2], color='r', length=0.03,
          normalize=True, arrow_length_ratio=0.5)
# -------------------------------------  Plot the hemisphere surface ------------------------------------------

radius = 0.09
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi / 2, 100)

x_hemisphere = radius * np.outer(np.cos(u), np.sin(v))
y_hemisphere = radius * np.outer(np.sin(u), np.sin(v))
z_hemisphere = radius * np.outer(np.ones(np.size(u)), np.cos(v))

ax.plot_surface(x_hemisphere, y_hemisphere, z_hemisphere, color='g', alpha=0.1)

ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Z (m)')

plt.show()
