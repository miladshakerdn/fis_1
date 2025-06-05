import numpy as np
import matplotlib.pyplot as plt
import math
from utility_functions import Calc_G


# -----------------------------  Loading Dipole, MEG sensor and Unit vector Cordinates------------------------------------

# TODO: Load the coordinate data files for dipoles, sensors and unit vectors
# data1 = 
# data2 = 
# data3 = 

# TODO: Extract and organize dipole coordinates into array
# rq_x = 
# rq_y = 
# rq_z = 
# rq = 

# TODO: Extract and organize sensor coordinates into array
# r_x = 
# r_y = 
# r_z = 
# r = 

# TODO: Extract and organize unit vectors into array
# er_x = 
# er_y = 
# er_z = 
# er = 

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
# G = 

# TODO: Calculate lead field matrix components
# for i in range(m):
#     k = 0
#     for j in range(n):
#         ...

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


