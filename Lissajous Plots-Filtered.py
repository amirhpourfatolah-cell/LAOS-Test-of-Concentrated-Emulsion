import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.fft import fft, ifft, fftfreq

# 1. CONFIGURE: Set your path and the specific sheet you want to plot right now
file_path = r'D:\TU Delft - MSc Mechanical Engineering - EFPT\Q4\Rheology\Assignment\Amplitude sweep.xlsx'
sheet_name = 'strain = 101'  # Change this string to plot other sheets one-by-one

# 2. LOAD DATA: Skip headers/units and grab Strain (col 1) and Stress (col 2)
data = pd.read_excel(file_path, sheet_name=sheet_name, skiprows=2, usecols=[1, 2], names=['Strain', 'Stress'])

raw_strain = data['Strain'].values
raw_stress = data['Stress'].values

# Sampling parameters (the instrument samples at ~512 Hz)
dt = 0.001953125  
n = len(raw_stress)
freqs = fftfreq(n, d=dt)

# 3. FFT FILTER: Convert to frequency domain, wipe out everything > 5 Hz, convert back
# (This perfectly preserves the 1 Hz fundamental frequency and key lower harmonics)
f_stress = fft(raw_stress)
f_stress[np.abs(freqs) > 5.0] = 0.0
clean_stress = np.real(ifft(f_stress))

f_strain = fft(raw_strain)
f_strain[np.abs(freqs) > 5.0] = 0.0
clean_strain = np.real(ifft(f_strain))

clean_stress = clean_stress - np.mean(clean_stress)
clean_strain = clean_strain - np.mean(clean_strain)

# 4. NORMALIZE: Scale perfectly between -1 and +1
norm_strain = clean_strain / np.max(np.abs(clean_strain))
norm_stress = clean_stress / np.max(np.abs(clean_stress))

# 5. PLOT LISSAJOUS
plt.figure(figsize=(6, 6))  # Square window prevents geometric stretching
plt.plot(norm_strain, norm_stress, color='#d62728', linewidth=2, label='FFT Filtered (< 5 Hz)')

plt.xlabel('Normalized Strain [-]')
plt.ylabel('Normalized Stress [-]')
plt.title(f'Lissajous Plot -  ${{\gamma}} = 101$', fontsize=12, pad=10)
plt.grid(True, which='both', linestyle='--', alpha=0.5)

# Force the aspect ratio to be equal so the ellipse geometry is true to physics
plt.gca().set_aspect('equal', adjustable='box')
plt.xlim([-1.1, 1.1])
plt.ylim([-1.1, 1.1])
plt.axhline(0, color='black', linewidth=1.5, zorder=2)  # X-axis spine at y=0
plt.axvline(0, color='black', linewidth=1.5, zorder=2)

plt.show()