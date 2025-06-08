import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math
from utility_functions import Conv_coordinates

# -----------------------------  Loading Dipole, MEG sensor and Unit vector Cordinates------------------------------------

# بارگذاری فایل‌های مختصات حسگرها و بردارهای واحد آنها
data2 = np.load("sensor_coordinates.npz")
data3 = np.load("Unit_Vect_coordinates.npz")

# استخراج و سازماندهی مختصات حسگرها در یک آرایه (33, 3)
r_x = data2['x']
r_y = data2['y']
r_z = data2['z']
r = np.vstack((r_x, r_y, r_z)).T

# استخراج و سازماندهی بردارهای واحد حسگرها در یک آرایه (33, 3)
er_x = data3['ex']
er_y = data3['ey']
er_z = data3['ez']
er = np.vstack((er_x, er_y, er_z)).T

# --- تعریف پارامترهای دوقطبی واحد ---

# تعریف موقعیت دوقطبی به صورت کروی
theta_dipole = np.deg2rad(45)
phi_dipole = np.deg2rad(45)
radius_dipole = 0.07 # 7cm in meters

# تبدیل موقعیت کروی دوقطبی به مختصات دکارتی
x_dipole, y_dipole, z_dipole = Conv_coordinates(phi_dipole, theta_dipole, radius_dipole)

# ایجاد بردار موقعیت برای دوقطبی
rq = np.array([x_dipole, y_dipole, z_dipole])

# تعریف گشتاورهای پایه واحد در سه جهت x, y, z
q_x = np.array([1, 0, 0])
q_y = np.array([0, 1, 0])
q_z = np.array([0, 0, 1])
unit_moments = [q_x, q_y, q_z]

# -----------------------------------------------  Constants ---------------------------------------------------------

m = 33  # Number of MEG Sensor
n_components = 3 # Number of dipole moment components (qx, qy, qz)
mu = 4 * math.pi * 1e-7

# ---------------------------  Calculate Lead Field Matrix ---------------------------

# TODO: Initialize the lead field matrix G
# ماتریس G باید ابعاد (تعداد سنسور, تعداد مولفه‌های گشتاور) را داشته باشد
G = np.zeros((m, n_components))

# TODO: Calculate lead field matrix components
# حلقه روی هر حسگر
for i in range(m):
    # حلقه روی هر یک از سه مولفه گشتاور (x, y, z)
    for j in range(n_components):
        
        q_unit = unit_moments[j]
        
        # بردار فاصله از دوقطبی تا حسگر i
        R_vec = r[i] - rq
        R_norm = np.linalg.norm(R_vec)
        
        # محاسبه بردار میدان مغناطیسی با فرمول بیو-ساوار برای دوقطبی واحد
        B_vec = (mu / (4 * np.pi)) * np.cross(q_unit, R_vec) / (R_norm**3)
        
        # محاسبه و ذخیره جزء شعاعی میدان در ستون مربوطه ماتریس G
        # G[:, 0] -> اثر qx
        # G[:, 1] -> اثر qy
        # G[:, 2] -> اثر qz
        G[i, j] = np.dot(B_vec, er[i])

# برای نمایش، می‌توانیم میدان ناشی از یک جهت خاص (مثلاً z) را انتخاب کنیم
# یا میدان کل را با فرض یک گشتاور خاص (مثلاً q=[0,0,1]) بازسازی کنیم.
# در اینجا برای حفظ ساختار قبلی، میدان ناشی از qz را نمایش می‌دهیم.
B_r = G[:, 2] # میدان ناشی از گشتاور در جهت z

# TODO: Save the lead field matrix
# ذخیره ماتریس G با ابعاد صحیح (33, 3)
np.savez("MEG_Lead_Field_Single_Dipole.npz", G=G, rq=rq)
print("Shape of the saved G matrix:", G.shape) # باید (33, 3) باشد

# -------------------------------------  Visiualize MEG sensor ------------------------------------------

fig = plt.figure(figsize=(9, 6))
ax = fig.add_subplot(111, projection='3d')
plt.title('Radial magnetic field for q_z component') 

# ... بقیه کد نمایش بدون تغییر باقی می‌ماند و B_r (میدان ناشی از q_z) را نمایش می‌دهد ...
ax.set_box_aspect([1, 1, 1])
ax.set_xlim([-0.11, 0.11])
ax.set_ylim([-0.11, 0.11])
ax.set_zlim([-0.11, 0.11])
ax.set_xticks(np.arange(-0.1, 0.1, 0.04))
ax.set_yticks(np.arange(-0.1, 0.1, 0.04))
ax.set_zticks(np.arange(-0.1, 0.1, 0.04))

if np.any(B_r):
    Bmin = np.min(B_r)
    Bmax = np.max(B_r)
else:
    Bmin, Bmax = -1e-15, 1e-15

scatter = ax.scatter(r_x, r_y, r_z, c=B_r, cmap='viridis', s=50, vmin=Bmin, vmax=Bmax)
cbar = plt.colorbar(scatter, ax=ax, shrink=0.6)
cbar.set_label('|B_r| from q_z (T)')

# نمایش بردار موقعیت دوقطبی و جهت z
q_to_visualize = np.array([0, 0, 1])
ax.quiver(rq[0], rq[1], rq[2], q_to_visualize[0], q_to_visualize[1], q_to_visualize[2], color='r', length=0.03,
          normalize=True, arrow_length_ratio=0.5, label='Dipole Position & Z-axis')

radius_surf = 0.09
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi / 2, 100)
x_hemisphere = radius_surf * np.outer(np.cos(u), np.sin(v))
y_hemisphere = radius_surf * np.outer(np.sin(u), np.sin(v))
z_hemisphere = radius_surf * np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(x_hemisphere, y_hemisphere, z_hemisphere, color='y', alpha=0.2)

ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Z (m)')
plt.show()