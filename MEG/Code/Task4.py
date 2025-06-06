import numpy as np
import matplotlib.pyplot as plt
import math
from utility_functions import Calc_G


# -----------------------------  Loading Dipole, MEG sensor and Unit vector Cordinates------------------------------------

# TODO: Load the coordinate data files for dipoles, sensors and unit vectors
data1 = np.load("Dipole_coordinates.npz")
data2 = np.load("sensor_coordinates.npz")
data3 = np.load("Unit_Vect_coordinates.npz")

# TODO: Extract and organize dipole coordinates into array
# استخراج و سازماندهی مختصات دوقطبی‌ها در یک آرایه (105, 3)
rq_x = data1['x']
rq_y = data1['y']
rq_z = data1['z']
rq = np.vstack((rq_x, rq_y, rq_z)).T

# TODO: Extract and organize sensor coordinates into array
# استخراج و سازماندهی مختصات حسگرها در یک آرایه (33, 3)
r_x = data2['x']
r_y = data2['y']
r_z = data2['z']
r = np.vstack((r_x, r_y, r_z)).T

# TODO: Extract and organize unit vectors into array
# استخراج و سازماندهی بردارهای واحد حسگرها در یک آرایه (33, 3)
er_x = data3['ex']
er_y = data3['ey']
er_z = data3['ez']
er = np.vstack((er_x, er_y, er_z)).T

# -----------------------------------------------  Constants ---------------------------------------------------------

m = 33  # Number of MEG Sensor
n = 105
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

# -----------------------------------------  Calculate Lead Field Matrix -----------------------------------------

# TODO: Initialize the lead field matrix G
# ایجاد یک ماتریس صفر با ابعاد ۳۳ در ۱۰۵ برای نگهداری نتایج
G = np.zeros((m, n))

# TODO: Calculate lead field matrix components
# برای محاسبه ماتریس G، باید یک جهت‌گیری (گشتاور) برای هر دوقطبی فرض کنیم.
# از آنجایی که MEG به منابع مماسی (tangential) حساس‌تر است،
# یک گشتاور مماسی واحد (مثلاً در جهت x) برای همه دوقطبی‌ها فرض می‌کنیم.
q_canonical = np.array([1, 0, 0])

# محاسبه درایه‌های ماتریس G با دو حلقه تو در تو
for i in range(m):      # حلقه روی هر حسگر
    for j in range(n):  # حلقه روی هر دوقطبی
        
        # بردار فاصله از منبع دوقطبی تا حسگر
        R_vec = r[i] - rq[j]
        R_norm = np.linalg.norm(R_vec)
        
        # محاسبه میدان مغناطیسی با استفاده از فرمول ساده‌شده بیو-ساوار برای دوقطبی
        # B = (mu/4pi) * (q x R) / |R|^3
        B_vec = (mu / (4 * np.pi)) * (np.cross(q_canonical, R_vec)) / (R_norm**3)
        
        # جزء شعاعی میدان مغناطیسی، ضرب داخلی بردار میدان در بردار واحد شعاعی حسگر است
        G[i, j] = np.dot(B_vec, er[i])

# -------------------------------------  Visiualize G[:, 75] ----------------------------------------------

G_1 = G[:, 74]
print(G_1.shape)

# Creating the plot
plt.figure(figsize=(8, 6))
plt.plot(G_1, label='Column 75 of G')  

plt.xlabel('Sensor Index') 
plt.ylabel('Value of G[:, 74]')  

plt.title('Column 75 of MEG Laed_Field') 
plt.grid(True)
plt.legend()

plt.show()  


