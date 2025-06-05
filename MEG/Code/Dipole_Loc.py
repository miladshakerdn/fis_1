import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from utility_functions import sorted, Conv_coordinates


# -------------------------------------  Calculate Coordinates of Diapole  ------------------------------------------
# TODO: Define the number of dipole sources to generate
# num_points = 

# TODO: Initialize a random number generator with the default algorithm
# rng = 

# TODO: Generate random theta values (polar angle) between 0 and π
# theta = 

# TODO: Generate random phi values (azimuthal angle) between 0 and 2π
# phi = 

# TODO
# radius =  # radius of the hemisphere in meters

# TODO: Convert spherical coordinates to Cartesian coordinates using utility_functions
# x, y, z = 

# TODO: Sort the dipole coordinates based on distance from z-axis
# x_sorted, y_sorted, z_sorted = 

np.savez("Dipole_coordinates.npz", x=x_sorted, y=y_sorted, z=z_sorted)
print(x_sorted.shape)  # Should output (105,)

# -------------------------------------  Visiualize Diapole  ------------------------------------------

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_title('Random Generated Dipole')

# # Set size of each axis
ax.set_xlim([-0.08, 0.08])
ax.set_ylim([-0.08, 0.08])
ax.set_zlim([-0.08, 0.08])

# Set the grid grading for each axis
ax.set_xticks(np.arange(-0.08, 0.08, 0.04))
ax.set_yticks(np.arange(-0.08, 0.08, 0.04))
ax.set_zticks(np.arange(-0.08, 0.08, 0.04))

ax.set_box_aspect([1, 1, 1])  # This will make the axes equally spaced

# Scatter plot for MEG sensors with numbers
for i, (xi, yi, zi) in enumerate(zip(x_sorted, y_sorted, z_sorted)):
    ax.scatter(xi, yi, zi, color='b')
    ax.text(xi, yi, zi, f'{i+1}', color='black', fontsize=9)

# -------------------------------------  Plot the hemisphere surface ------------------------------------------

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)

x_hemisphere = radius * np.outer(np.cos(u), np.sin(v))
y_hemisphere = radius * np.outer(np.sin(u), np.sin(v))
z_hemisphere = radius * np.outer(np.ones(np.size(u)), np.cos(v))

ax.plot_surface(x_hemisphere, y_hemisphere, z_hemisphere, color='r', alpha=0.3)

ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Z (m)')

plt.show()
