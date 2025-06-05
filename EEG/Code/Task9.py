import numpy as np
import matplotlib.pyplot as plt
import math
from utility_functions import Calc_L,d_n, cartesian_to_polar

# -----------------------  Loading Dipole, EEG sensor Cordinates ---------------------

# TODO: Load the coordinate data files for dipoles and sensors
# data1 = 
# data2 = 

# TODO: Extract dipole coordinates
# rq_x = 
# rq_y = 
# rq_z = 

# TODO: Convert dipole coordinates from Cartesian to spherical
# r_0, theta_0, phi_0 = 

# TODO: Extract sensor coordinates
# r_x = 
# r_y = 
# r_z = 

# TODO: Convert sensor coordinates from Cartesian to spherical
# r, theta, phi = 

# -----------------------------------------------  Constants ---------------------------------------------------------

m = 33       # Number of EEG Sensor
n = 105      # Number of Dipole
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

# --------------------------------------------  Create EEG Laed_Field  -------------------------------------------------------

# TODO: Define function to calculate lead field components for a sensor-dipole pair
# def Calc_L():

#     # Calculate the lead field components using the formula
    # return a_ij

# TODO: Define function to calculate d_n coefficient for the three-sphere model
# def d_n():
    # Apply the formula for d_n coefficient
    # return dn

# TODO: Initialize the EEG lead field matrix L
# L = 

# TODO: Define conductivity ratio
# xi = 
# b = 

# TODO: Calculate EEG lead field matrix components
# for i in range():
    # k =  
    # for j in range():
	# . . .


# ----------------------------------------------  Visiualize L[:, 74] ---------------------------------------------------

L_1 = L[:, 74]
print(L_1.shape)

# Creating the plot
plt.figure(figsize=(10, 7))
plt.plot(L_1, label='Column 75 of G')

plt.xlabel('Sensor Index')
plt.ylabel('Value of L[:, 74]')

plt.title('Column 75 of EEG Laed_Field')
plt.grid(True)
plt.legend(loc='upper right', fontsize='large', fancybox=True, frameon=True, facecolor='lightgray', edgecolor='red')


plt.show()
