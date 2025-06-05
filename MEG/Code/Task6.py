import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------- Calculate W(t) -------------------------------------------------

# TODO: Define the periodic function w(t) as specified
# def w(t):
#     return ...
# TODO: Create a time vector with 1000 samples over 2 seconds
# t = 
# TODO: Calculate w(t) values for each time point
# w_values =


# ----------------------------- Calculate radial component of magnetic flux density for sensor 30  -------------------------------

# TODO: Load the lead field matrix
# data = 
# G = 
# TODO: Define the dipole orientation vector
# q = 
# q1 = 
# TODO: Calculate the constant magnetic field at sensor 30
# B_r = 
# TODO: Calculate the time-varying magnetic field at sensor 30
# B_r_new = 


# -------------------------------------  Visiualize MEG Sensor Number 30 ------------------------------------------
# Plot
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(13, 7))

ax1.plot(t, w_values, label=r'w(t)', color='r')
ax1.set_title('Plot of w(t)')
ax1.set_xlabel('t')
ax1.set_ylabel('w(t)')
ax1.legend()
ax1.grid(True)

# Plot B_r
ax2.plot(t,np.full(t.shape,(B_r)), label=r'B')
ax2.set_title('Constant Sensor Number 30')
ax2.set_xlabel('Time(s)')
ax2.set_ylabel('B')
ax2.legend()
ax2.grid(True)


# Plot B_r
ax3.plot(t, B_r_new, label=r'B')
ax3.set_title('Variable Sensor Number 30')
ax3.set_xlabel('Time(s)')
ax3.set_ylabel('B')
ax3.legend()
ax3.grid(True)

plt.tight_layout()
plt.show()


