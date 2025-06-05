import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from utility_functions import Conv_coordinates

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# ---------------------- Calculate Coordinates of MEG sensors -----------------------

# TODO: Define the number of MEG sensors
# تعداد کل حسگرها ۳۳ عدد است
num_points = 33

# TODO: Define theta angles for all sensors (zenith angle)
# First sensor at zenith (0°), then 4 sensors at each of the 8 longitudinal strips
# و TODO: Define phi angles for all sensors (azimuthal angle)
# آرایه‌های خالی برای نگهداری زوایای تتا و فی به درجه ایجاد می‌شود
theta_degrees = np.zeros(num_points)
phi_degrees = np.zeros(num_points)

# حسگر اول در راس (زاویه تتا = 0) قرار دارد. زاویه فی برای آن مهم نیست.
theta_degrees[0] = 0
phi_degrees[0] = 0

# محاسبه زوایا برای ۳۲ حسگر باقی‌مانده بر اساس ۸ نوار طولی و ۴ حسگر در هر نوار
# i نماینده شماره نوار (از ۰ تا ۷) و j نماینده شماره حسگر در هر نوار (از ۱ تا ۴) است.
for i in range(8):
    for j in range(1, 5):
        # شماره حسگر بر اساس فرمول 4i + j + 1 محاسبه می‌شود
        sensor_number = 4 * i + j + 1
        # شاخص آرایه یکی کمتر از شماره حسگر است
        index = sensor_number - 1
        
        # زاویه تتا بر اساس موقعیت حسگر در نوار تعیین می‌شود
        theta_degrees[index] = j * 22.5
        # زاویه فی بر اساس شماره نوار تعیین می‌شود
        phi_degrees[index] = i * 45

# TODO: Convert degrees to radians for calculations
# تبدیل زوایای تتا و فی از درجه به رادیان برای استفاده در محاسبات مثلثاتی
theta = np.deg2rad(theta_degrees)
phi = np.deg2rad(phi_degrees)

# TODO: Convert spherical coordinates to Cartesian coordinates
# شعاع کره (پوست سر) ۰.۰۹ متر است
radius = 0.09
# استفاده از تابع کمکی برای تبدیل مختصات کروی به دکارتی (x, y, z)
x, y, z = Conv_coordinates(phi, theta, radius)

# TODO: Save the calculated sensor coordinates to a file for later use
# ذخیره مختصات محاسبه‌شده در یک فایل .npz برای استفاده در تسک‌های بعدی
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