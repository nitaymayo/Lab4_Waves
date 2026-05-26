import numpy as np 				# math functions
import scipy					# scientific functions
import matplotlib.pyplot as plt 			# for plotting figures and setting their properties
import pandas as pd 				# handling data structures (loaded from files)
from scipy.stats import linregress 		# contains linregress (for linear regression)
from scipy.optimize import curve_fit as cfit 	# non-linear curve fitting
from sklearn.metrics import r2_score 		# import function that calculates R^2 score
from prettytable import PrettyTable 		# display data in visually table format
import scipy.ndimage as ndimage   		# import Multidimensional Image processing package
from scipy.signal import find_peaks        	             # for find local peaks in a signal
import math

df_mw = pd.read_csv("microwave_waveguide_data.csv")

# Again, assuming column names here based on typical lab setups
theta_deg = df_mw['theta(deg)'].values
Intensity1 = df_mw['power_1'].values
Intensity2 = df_mw['power_2'].values

# 2. Convert degrees to radians (plt.polar requires radians)
theta_rad = np.radians(theta_deg)

# 3. Plot the Polar Graph
plt.figure(figsize=(6, 6))
plt.polar(theta_rad, Intensity1)
plt.title("Microwave Polarization for case 1 - linear polarization")
plt.show()

plt.figure(figsize=(6, 6))
plt.polar(theta_rad, Intensity2)
plt.title("Microwave Polarization for case 2 - circular polarization")
plt.show()
