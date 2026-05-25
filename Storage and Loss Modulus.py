import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

file_path = r'D:\TU Delft - MSc Mechanical Engineering - EFPT\Q4\Rheology\Assignment\Amplitude sweep.xlsx'

data = pd.read_excel(file_path, sheet_name='First harmonic analysis', skiprows=2 , usecols=[0,1,4], names=['Strain', 'Stress','phase'])
strain = data['Strain'].values
strain = strain / 100  # Convert percentage to decimal
stress = data['Stress'].values
phase = data['phase'].values

G_star = stress / strain
G_prime = G_star * np.cos(phase)
G_second = G_star * np.sin(phase)

plt.figure(figsize=(8, 5))
plt.loglog(strain, G_prime, label='Storage Modulus (G$^{\prime}$)', color='blue')
plt.loglog(strain, G_second, label='Loss Modulus (G$^{\prime\prime}$)', color='red')
plt.xlabel('Strain $\gamma$')
plt.ylabel('Modulus [Pa]')
plt.ylim(1e1, 1e3)
plt.title('Storage and Loss Modulus vs Strain')
plt.legend()
plt.grid(True, which='both', linestyle='-', linewidth=0.5)
plt.show()



