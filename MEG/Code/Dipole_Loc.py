import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from utility_functions import sorted, Conv_coordinates


# ---------------------- Calculate Coordinates of Diapole -----------------------

# TODO: Define the number of dipole sources to generate
# تعداد منابع دوقطبی ۱۰۵ عدد است
num_points = 104

# TODO: Initialize a random number generator with the default algorithm
# یک مولد عدد تصادفی برای تولید مقادیر یکنواخت ایجاد می‌شود
rng = np.random.default_rng()

# TODO: Generate random theta values (polar angle) between 0 and π
# تولید ۱۰۵ زاویه تتا به صورت تصادفی و یکنواخت بین ۰ و پی برای پوشش کل کره
theta = rng.uniform(0, np.pi, num_points)

# TODO: Generate random phi values (azimuthal angle) between 0 and 2π
# تولید ۱۰۵ زاویه فی به صورت تصادفی و یکنواخت بین ۰ و دو پی
phi = rng.uniform(0, 2 * np.pi, num_points)

# TODO: Convert spherical coordinates to Cartesian coordinates
# شعاع کره ۷ سانتی‌متر (۰.۰۷ متر) است
radius = 0.07  # radius of the sphere in meters
# تبدیل مختصات کروی تولید شده به مختصات دکارتی
x, y, z = Conv_coordinates(phi, theta, radius)

# TODO: Sort the dipole coordinates based on distance from z-axis
# مرتب‌سازی دوقطبی‌ها بر اساس فاصله از محور z با استفاده از تابع کمکی
x_sorted, y_sorted, z_sorted = sorted(x, y, z)

# ذخیره مختصات مرتب‌شده دوقطبی‌ها در یک فایل برای استفاده‌های بعدی
np.savez("Dipole_coordinates.npz", x=x_sorted, y=y_sorted, z=z_sorted)
print(x_sorted.shape)  # خروجی باید (105,) باشد

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
