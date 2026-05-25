import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

file_path = r'D:\TU Delft - MSc Mechanical Engineering - EFPT\Q4\Rheology\Assignment\Amplitude sweep.xlsx'
# Change the sheet name to match the one you want to analyze
sheet_name = 'strain = 101'
data = pd.read_excel(file_path, sheet_name=sheet_name, skiprows=2 , usecols=[1,2,3], names=['Strain', 'Stress','time'])
strain = data['Strain'].values
max_strain = np.max(np.abs(strain))
strain = strain / (100 * max_strain)  # Convert percentage to decimal and normalize by max strain
stress = data['Stress'].values
max_stress = np.max(np.abs(stress))
stress = stress / max_stress  # Normalize stress by max stress
time = data['time'].values


fig, axs = plt.subplots(figsize=(10, 8))
axs.plot(time, stress, label='Stress', color='blue')
axs.set_xlabel('Time [s]')
axs.set_ylabel('Stress [Pa]')
axs.set_title('Stress & Strain against Time ($\gamma=101$)')


axs2 = axs.twinx()  # Create a second y-axis for strain

axs2.plot(time, strain, label='Strain', color='red')
axs2.set_ylabel('Strain $\gamma$')

lines = axs.get_lines() + axs2.get_lines()
labels = [line.get_label() for line in lines]
axs.legend(lines, labels, loc='upper right')
plt.grid(True, which='both', linestyle='-', linewidth=0.5)
plt.show()



