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

d = 1/500 # mm/lines

df = pd.read_csv('Spectro_data.csv')
color = df['colour'].tolist()
angle = df['Grating Angle (deg)'].tolist()

wavelength = [d * math.sin(math.radians(a)) for a in angle]

Lines = {}

for n in range(0, len(angle)):
    key = f'Line %d' % (n + 1)
    value = [color[n], angle[n], wavelength[n]]
    Lines.update({key: value})

table = PrettyTable(["Grating Angle [deg]","Grating Wavelength [nm]","colour"])

for a, c, w in zip(angle, color, wavelength):
    table.add_row([a, w, c])

print(table)

prism_angle_vector = [1, 2, '', 4, 5, 6 , '', 8, 9]

table.add_column("Prism Angle [deg]", prism_angle_vector)

print(table)
