import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as cfit
from sklearn.metrics import r2_score

# 1. Load Data
df_buzz = pd.read_csv("2_buzzers_data.csv")
x_data = df_buzz['x_1 (cm)'].values # distance from buzzer
y_data = df_buzz['Amplitude'].values # measured amplitude

L = 1

def f(x, a, lam, phi):
    return np.abs(2 * a * np.cos((np.pi / lam) * (2 * x - L) + phi / 2))

p0 = [2.4, 6, -1.5]
params, cov = cfit(f, x_data, y_data, p0=p0)

y_pred = f(x_data, *params)
Rsq = r2_score(y_data, y_pred)

errors = np.sqrt(np.diag(cov))

print(f"Fitted [a, lam, phi]: {params}")
print(f"Parameter Errors: {errors}")
print(f"R^2 Score: {Rsq:.4f}")

# 6. Plotting
plt.figure(figsize=(8, 5))
plt.plot(x_data, y_data, 'ro', label='Measured Data')
plt.plot(x_data, y_pred, 'b-', label='Fitted Curve')
plt.xlabel('Distance (x)')
plt.ylabel('Amplitude')
plt.title('Two Buzzers Interference')
plt.legend()
plt.grid(True)
plt.show()
