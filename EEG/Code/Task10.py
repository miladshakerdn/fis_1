import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math
from scipy.special import lpmv

# تابع کمکی برای تبدیل دکارتی به کروی
def cartesian_to_polar(x, y, z):
    r = np.sqrt(x**2 + y**2 + z**2)
    theta = np.arccos(z / r)
    phi = np.arctan2(y, x)
    return r, theta, phi

# ---------------------  Loading and Defining Coordinates -----------------------

# TODO: Load sensor coordinates data
data2 = np.load("sensor_coordinates.npz")

# --- تعریف پارامترهای دوقطبی ---
# برای سازگاری، از همان موقعیت تسک ۵ استفاده می‌کنیم
# TODO: Define dipole parameters
theta_0_dipole = np.deg2rad(45)
phi_0_dipole = np.deg2rad(45)
radius_0_dipole = 0.07 # 7cm in meters

# تابع کمکی برای تبدیل کروی به دکارتی
def conv_coordinates_single(phi, theta, radius):
    x = radius * np.sin(theta) * np.cos(phi)
    y = radius * np.sin(theta) * np.sin(phi)
    z = radius * np.cos(theta)
    return x, y, z

# TODO: Convert dipole position from spherical to Cartesian coordinates
x_d, y_d, z_d = conv_coordinates_single(phi_0_dipole, theta_0_dipole, radius_0_dipole)

# TODO: Define dipole moment vector and position
rq = np.array([x_d, y_d, z_d])
# برای EEG، منابع شعاعی سیگنال قوی تولید می‌کنند.
# فرض می‌کنیم گشتاور دوقطبی در راستای شعاعی و به سمت بیرون است.
q_mag = 1.0 # قدرت واحد
q = (rq / np.linalg.norm(rq)) * q_mag # بردار گشتاور شعاعی واحد

# --- استخراج و تبدیل مختصات حسگر ---
# TODO: Extract sensor coordinates
r_x = data2['x']
r_y = data2['y']
r_z = data2['z']

# TODO: Convert sensor coordinates from Cartesian to spherical
r, theta, phi = cartesian_to_polar(r_x, r_y, r_z)

# -----------------------------------------------  Constants ---------------------------------------------------------
m = 33       # Number of EEG Sensor
n = 1        # Number of Dipole
R1 = 0.08    # Brain radius
R2 = 0.085   # Skull radius
R3 = 0.09    # Scalp radius
sg1 = 0.3    # Brain conductivity
sg2 = 0.3 / 80 # Skull conductivity
sg3 = 0.3    # Scalp conductivity

# --------------------------------------------  Create EEG Lead_Field  -------------------------------------------------------

# تابع کمکی برای محاسبه زاویه گاما بین حسگر و دوقطبی
def get_gamma(theta_i, phi_i, theta_0j, phi_0j):
    cos_gamma = np.cos(theta_i) * np.cos(theta_0j) + np.sin(theta_i) * np.sin(theta_0j) * np.cos(phi_i - phi_0j)
    return np.arccos(np.clip(cos_gamma, -1.0, 1.0))

# TODO: Define function to calculate lead field components for a sensor-dipole pair
def Calc_L(sensor_r, sensor_theta, sensor_phi, dipole_r, dipole_theta, dipole_phi):
    # این تابع پتانسیل را برای یک دوقطبی شعاعی واحد محاسبه می‌کند
    gamma = get_gamma(sensor_theta, sensor_phi, dipole_theta, dipole_phi)
    N_max = 50 # حد بالای سری لژاندر
    
    sum_val = 0
    # محاسبه پتانسیل با استفاده از بسط سری لژاندر
    for leg_n in range(1, N_max + 1):
        p_n_gamma = lpmv(0, leg_n, np.cos(gamma)) # محاسبه P_n(cos(gamma))
        term = (leg_n * (2 * leg_n + 1) / (4 * np.pi * sg3)) * \
               (dipole_r**(leg_n - 1) / sensor_r**(leg_n + 1)) * p_n_gamma
        sum_val += term
    return sum_val

# ------------------------  Calculate EEG Voltage of sensors  ------------------------

# TODO: Calculate the electric potential at each sensor
V = np.zeros(m) # آرایه برای نگهداری پتانسیل در هر حسگر

for i in range(m):
    # محاسبه پتانسیل برای حسگر i ناشی از دوقطبی واحد
    potential_from_unit_dipole = Calc_L(r[i], theta[i], phi[i], radius_0_dipole, theta_0_dipole, phi_0_dipole)
    V[i] = potential_from_unit_dipole * q_mag

# TODO: Save the EEG lead field matrix/vector
# ذخیره نتایج
np.savez("EEG_Single_Dipole_Potential.npz", V=V, rq=rq, q=q)

# -------------------------------------  Visiualize EEG sensor ------------------------------------------

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# ... (بقیه کد نمایش که در فایل اصلی شما موجود است، بدون تغییر باقی می‌ماند) ...

ax.set_box_aspect([1, 1, 1])
ax.set_xlim([-0.11, 0.11])
ax.set_ylim([-0.11, 0.11])
ax.set_zlim([-0.11, 0.11])

ax.set_xticks(np.arange(-0.1, 0.1, 0.04))
ax.set_yticks(np.arange(-0.1, 0.1, 0.04))
ax.set_zticks(np.arange(-0.1, 0.1, 0.04))
plt.title('Voltage value of sensors')

vmin = np.min(V)
vmax = np.max(V)

scatter = ax.scatter(r_x, r_y, r_z, c=V, cmap='coolwarm', s=60, vmin=vmin, vmax=vmax, edgecolors='k')

cbar = plt.colorbar(scatter, ax=ax, shrink=0.6)
cbar.set_label('Voltage (V)')

for i in range(m):
    ax.text(r_x[i], r_y[i], r_z[i], f'{i+1}', color='black', fontsize=8)

ax.quiver(rq[0], rq[1], rq[2], q[0], q[1], q[2], color='r', length=0.03,
          normalize=True, arrow_length_ratio=0.5)

radius_surf = 0.09
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi / 2, 100)
x_hemisphere = radius_surf * np.outer(np.cos(u), np.sin(v))
y_hemisphere = radius_surf * np.outer(np.sin(u), np.sin(v))
z_hemisphere = radius_surf * np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(x_hemisphere, y_hemisphere, z_hemisphere, color='y', alpha=0.15)

ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Z (m)')
plt.show()