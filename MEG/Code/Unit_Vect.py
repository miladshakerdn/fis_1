import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


# -------------------------------------  Calculate Coordinates of Unit Vector ------------------------------------------

# np.savez("Unit_Vect_coordinates.npz", ex=ex, ey=ey, ez=ez)

# # TODO: Load the sensor coordinates from the previously saved file
# data = np.load("sensor_coordinates.npz")
# # x = 
# # y = 
# # z = 
# # radius = # radius of the hemisphere

# # TODO: Initialize arrays for unit vector components
# # ex = 
# # ey = 
# # ez = 
# print(ex.shape)  # Should output (33,)

# # TODO: Calculate unit vectors for each sensor
# for i in range(33):
#     # TODO: Calculate the magnitude of the position vector    
#     # TODO: Normalize each component by div iding by the magnitude

# # TODO: Save the unit vector components to a file for later use
# np.savez("Unit_Vect_coordinates.npz", ex=ex, ey=ey, ez=ez)


# TODO: Load the sensor coordinates from the previously saved file
# بارگذاری مختصات دکارتی حسگرها که در تسک ۱ ذخیره شده بود
data = np.load("sensor_coordinates.npz")
x = data['x']
y = data['y']
z = data['z']
# شعاع کره که حسگرها روی آن قرار دارند ۰.۰۹ متر است
radius = 0.09 # radius of the hemisphere

# TODO: Initialize arrays for unit vector components
# ایجاد آرایه‌های خالی برای نگهداری مولفه‌های x, y, z بردارهای واحد
ex = np.zeros(33)
ey = np.zeros(33)
ez = np.zeros(33)

# TODO: Calculate unit vectors for each sensor
# محاسبه بردار واحد برای هر حسگر
for i in range(33):
    # برای یک کره با مرکز در مبدا، بردار موقعیت (x, y, z) بر سطح عمود است.
    # برای به دست آوردن بردار واحد، کافی است هر مولفه را بر اندازه بردار (شعاع) تقسیم کنیم.
    
    # TODO: Calculate the magnitude of the position vector
    # اندازه بردار موقعیت برای تمام نقاط روی کره برابر با شعاع کره است.
    magnitude = radius # یا می‌توان از np.sqrt(x[i]**2 + y[i]**2 + z[i]**2) استفاده کرد
    
    # TODO: Normalize each component by dividing by the magnitude
    # نرمال‌سازی هر مولفه برای به دست آوردن بردار واحد
    ex[i] = x[i] / magnitude
    ey[i] = y[i] / magnitude
    ez[i] = z[i] / magnitude

# TODO: Save the unit vector components to a file for later use
# ذخیره مولفه‌های بردار واحد در یک فایل جدید
np.savez("Unit_Vect_coordinates.npz", ex=ex, ey=ey, ez=ez)

# این بخش برای اطمینان از ابعاد صحیح آرایه است و باید (33,) را چاپ کند
print(ex.shape)


# -------------------------------------  Visiualize Unit Vector ---------------------------------------------

fig = plt.figure()
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

ax.quiver(x, y, z, ex, ey, ez, color='r', length=0.015,
          normalize=True, arrow_length_ratio=0.5)
ax.set_title('Visiualize Unit Vector')

# -------------------------------------  Plot the hemisphere surface ------------------------------------------

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi / 2, 100)

x_hemisphere = radius * np.outer(np.cos(u), np.sin(v))
y_hemisphere = radius * np.outer(np.sin(u), np.sin(v))
z_hemisphere = radius * np.outer(np.ones(np.size(u)), np.cos(v))

ax.plot_surface(x_hemisphere, y_hemisphere, z_hemisphere, color='y', alpha=0.4)

ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Z (m)')

plt.show()
