import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from utility_functions import Conv_coordinates

# -------------------------------------  Calculate Coordinates of MEG sensors ------------------------------------------

# TODO: Define the number of MEG sensors
# num_points = ...

# TODO: Define theta angles for all sensors (zenith angle)
# First sensor at zenith (0°), then 4 sensors at each of the 8 longitudinal strips
# theta_degrees = ...

# TODO: Define phi angles for all sensors (azimuthal angle)
# phi_degrees = ...

# TODO: Convert degrees to radians for calculations
# theta = ...
# phi = ...

# TODO: Convert spherical coordinates to Cartesian coordinates
# radius = ...
# x, y, z = ...

# TODO: Save the calculated sensor coordinates to a file for later use
np.savez("sensor_coordinates.npz", x=x, y=y, z=z)


# -------------------------------------  Visualize MEG sensor ------------------------------------------

# TODO: Create a 3D figure for visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_title('Visualize MEG sensor')

# TODO: Set equal aspect ratio for the 3D plot
ax.set_box_aspect([1, 1, 1])  # This will make the axes equally spaced
ax.set_xlim([-0.11, 0.11])
ax.set_ylim([-0.11, 0.11])
ax.set_zlim([-0.11, 0.11])

# TODO: Set appropriate grid ticks for better visualization
ax.set_xticks(np.arange(-0.1, 0.1, 0.04))
ax.set_yticks(np.arange(-0.1, 0.1, 0.04))
ax.set_zticks(np.arange(-0.1, 0.1, 0.04))

# TODO: Plot each sensor point and add a text label with sensor number
for i, (xi, yi, zi) in enumerate(zip(x, y, z)):
    ax.scatter(xi, yi, zi, color='b')
    ax.text(xi, yi, zi, f'{i+1}', color='black', fontsize=8)

# -------------------------------------  Plot the hemisphere surface ------------------------------------------

# TODO: Create a hemisphere surface using parametric equations
u = np.linspace(0, 2 * np.pi, 100)  # Azimuthal angle
v = np.linspace(0, np.pi / 2, 100)   # Polar angle (only up to pi/2 for hemisphere)

# TODO: Generate the (x,y,z) points of the hemisphere surface
x_hemisphere = radius * np.outer(np.cos(u), np.sin(v))
y_hemisphere = radius * np.outer(np.sin(u), np.sin(v))
z_hemisphere = radius * np.outer(np.ones(np.size(u)), np.cos(v))

# TODO: Plot the hemisphere as a semi-transparent surface
ax.plot_surface(x_hemisphere, y_hemisphere, z_hemisphere, color='g', alpha=0.4)

# TODO: Add axis labels with units
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Z (m)')

# TODO: Display the visualization
plt.show()