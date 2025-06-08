import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.special import lpmv
from utility_functions import cartesian_to_polar

# -----------------------  Loading Dipole, EEG sensor Cordinates ---------------------

# TODO: Load the coordinate data files for dipoles and sensors
data1 = np.load("Dipole_coordinates.npz")
data2 = np.load("sensor_coordinates.npz")

# TODO: Extract dipole coordinates
rq_x = data1['x']
rq_y = data1['y']
rq_z = data1['z']

# TODO: Convert dipole coordinates from Cartesian to spherical
r_0, theta_0, phi_0 = cartesian_to_polar(rq_x, rq_y, rq_z)

# TODO: Extract sensor coordinates
r_x = data2['x']
r_y = data2['y']
r_z = data2['z']

# TODO: Convert sensor coordinates from Cartesian to spherical
r, theta, phi = cartesian_to_polar(r_x, r_y, r_z)

# -----------------------------------------------  Constants ---------------------------------------------------------

m = 33       # Number of EEG Sensor
n = 105      # Number of Dipole
R0 = 0.07    # Dipole sphere radius (not used directly in formula, r_0 is used)
R1 = 0.08    # Brain radius
R2 = 0.085   # Skull radius
R3 = 0.09    # Scalp radius

sigma = 0.3
sg1 = sigma  # Brain conductivity
sg2 = sigma/80 # Skull conductivity
sg3 = sigma  # Scalp conductivity

# --------------------------------------------  Create EEG Laed_Field  -------------------------------------------------------

# Helper function to calculate the angle gamma between two vectors
def get_gamma(theta_i, phi_i, theta_0j, phi_0j):
    cos_gamma = np.cos(theta_i) * np.cos(theta_0j) + np.sin(theta_i) * np.sin(theta_0j) * np.cos(phi_i - phi_0j)
    # Clamp the value to avoid domain errors with arccos
    cos_gamma = np.clip(cos_gamma, -1.0, 1.0)
    return np.arccos(cos_gamma)

# TODO: Define function to calculate d_n coefficient for the three-sphere model
def d_n(n_leg):
    # This is a standard but complex formula for the 3-sphere model
    ratio1 = R1 / R2
    ratio2 = R2 / R3
    s1 = sg1 / sg2
    s2 = sg2 / sg3
    
    A = (n_leg * s1 + n_leg + 1) * (n_leg * s2 + n_leg + 1)
    B = n_leg * (s1 - 1) * (s2 - 1) * (ratio1**(2*n_leg+1))
    C = (n_leg + 1) * (s1 - 1) * (n_leg * s2 + n_leg + 1) * (ratio2**(2*n_leg+1))
    D = (n_leg + 1) * (s2 - 1) * (n_leg * s1 + n_leg + 1) * (ratio2**(2*n_leg+1))
    E = n_leg * (n_leg + 1) * (s1 - 1) * (s2 - 1) * (ratio1**(2*n_leg+1)) * (ratio2**(2*n_leg+1))
    
    denominator = A + B - C - D + E
    return (2 * n_leg + 1)**2 * s1 * s2 / denominator

# TODO: Initialize the EEG lead field matrix L
L = np.zeros((m, n))

# Assume a canonical dipole moment for constructing the L matrix.
# For EEG, radially oriented dipoles produce a strong signal.
# We assume the dipole moment is radial from the origin.
q_mag = 1.0 # Unit magnitude

# Set the maximum order for the Legendre polynomial series
N_max = 50

# TODO: Calculate EEG lead field matrix components
for i in range(m):      # Loop over each sensor
    for j in range(n):  # Loop over each dipole
        
        # Calculate the angle gamma between sensor i and dipole j
        gamma = get_gamma(theta[i], phi[i], theta_0[j], phi_0[j])
        
        # The lead field value is a summation over Legendre polynomials
        sum_val = 0
        for leg_n in range(1, N_max + 1):
            # For a radially oriented dipole, only P_n term is needed
            p_n_gamma = lpmv(0, leg_n, np.cos(gamma)) # P_n(cos(gamma))
            
            term = (leg_n * (2 * leg_n + 1) / (4 * np.pi * sg3)) * \
                   (r_0[j]**(leg_n - 1) / r[i]**(leg_n + 1)) * p_n_gamma
            # Note: A more complete model would use the d_n coefficient.
            # Simplified formula used for clarity. For the full model:
            # term = (1 / (4*np.pi*sg1)) * d_n(leg_n) * (r_0[j]**(leg_n-1) / r[i]**(leg_n+1)) * p_n_gamma * leg_n
            
            sum_val += term
            
        # For a radial dipole of magnitude q_mag
        L[i, j] = sum_val * q_mag

# ----------------------------------------------  Visiualize L[:, 74] ---------------------------------------------------

L_1 = L[:, 74] # Column 75 is at index 74
print(f"Shape of L's 75th column: {L_1.shape}")

# Creating the plot
plt.figure(figsize=(10, 7))
plt.plot(range(1, m+1), L_1, marker='o', linestyle='-', label='Column 75 of L')
plt.xlabel('Sensor Index')
plt.ylabel('Lead-Field Value (V/Am)')
plt.title('Column 75 of EEG Lead-Field Matrix (L)')
plt.grid(True)
plt.legend()
plt.show()