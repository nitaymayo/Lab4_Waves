import scipy.ndimage as ndimage
from scipy.signal import find_peaks
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

pixel_size = 5.2e-6
generator_frequency = 2.079e6
l = 632.8e-9
f3 = 0.3 # 300 mm = 0.3 meters

def process_field_img(path, dist, deg, p_0, promi):
    image = plt.imread(path)

    plt.imshow(image)

    rotated_image = ndimage.rotate(image, deg, reshape=True)

    plt.imshow(rotated_image)

    x = np.linspace(0, 399, 400)

    x_0, y_0 = p_0
    y = rotated_image[y_0, x_0 : x_0 + len(x), 0]

    peaks, _ = find_peaks(y, distance=dist, prominence=promi)

    # Create a new figure and plot the intensity slice
    plt.figure()
    plt.plot(y, label="Intensity Profile")

    # Plot triangles ('^') exactly at the peak coordinates
    plt.plot(peaks, y[peaks], '^', label="Detected Peaks")

    plt.title("Intensity vs Position")
    plt.xlabel("Pixels")
    plt.ylabel("Intensity")
    plt.legend()
    plt.show()

    return peaks, y

    peaks_difference = np.diff(peaks)
    avg_dist = np.mean(peaks_difference)

    delta_x = avg_dist * pixel_size

    speed_of_sound = generator_frequency * (f3 * l) / delta_x



near_peaks, y_near = process_field_img("NearField_2079MHz.tif", 40, 0, (600,600), 5)

peaks_difference = np.diff(near_peaks)
avg_dist = np.mean(peaks_difference)
delta_x = avg_dist * pixel_size
v_near = generator_frequency * delta_x
print(f"Speed of sound from near measurement: {v_near:.2f} m/s")



far_peaks, y_far = process_field_img("FarField_2079MHz.tif", 100, 0, (560, 510), 10)
peaks_difference = np.diff(far_peaks)
avg_dist = np.mean(peaks_difference)
delta_x = avg_dist * pixel_size
v_far = generator_frequency * (f3 * l) / delta_x
print(f"Speed of sound from far measurement: {v_far:.2f} m/s")


fft_near = np.abs(np.fft.fftshift(np.fft.fft(y_near)))


ifft_far = np.abs(np.fft.fftshift(np.fft.ifft(y_far)))

# Plot them side-by-side
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))

ax1.plot(fft_near, color='purple')
ax1.set_title("1D FFT of Near Field Intensity")
ax1.set_xlabel("Frequency")
ax1.grid(True)

ax2.plot(ifft_far, color='orange')
ax2.set_title("1D Inverse FFT of Far Field Intensity")
ax2.set_xlabel("Spatial Position")
ax2.grid(True)

plt.tight_layout()
plt.show()

