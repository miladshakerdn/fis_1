import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.special import lpmv, lpmn, lpn
from scipy.special import legendre


def cartesian_to_polar(x, y, z):
    r = np.sqrt(pow(x,2) + pow(y,2) + pow(z,2))
    theta = np.arccos(z / r)
    phi = np.arctan2(y, x)
    return r, theta, phi





