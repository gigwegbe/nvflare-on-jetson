import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.ndimage import gaussian_filter1d

# Replace with actual file paths
site1_csv = "acc_data/site-1.csv"
site2_csv = "acc_data/site-2.csv"
site3_csv = "acc_data/site-3.csv"

# Load CSVs
df1 = pd.read_csv(site1_csv)
df2 = pd.read_csv(site2_csv)
df3 = pd.read_csv(site3_csv)

# Apply smoothing
sigma = 2  # adjust smoothing strength
df1['Smoothed'] = gaussian_filter1d(df1['Value'], sigma=sigma)
df2['Smoothed'] = gaussian_filter1d(df2['Value'], sigma=sigma)
df3['Smoothed'] = gaussian_filter1d(df3['Value'], sigma=sigma)

# Plotting
plt.figure(figsize=(12, 6))

plt.plot(df1['Step'], df1['Smoothed'], label='client-1', color='#1f77b4')  # blue
plt.plot(df2['Step'], df2['Smoothed'], label='client-2', color='#17becf')  # cyan
plt.plot(df3['Step'], df3['Smoothed'], label='client-3', color='#e377c2')  # pink

plt.title("accuracy_per_epoch")
plt.xlabel("Epoch (Step)")
plt.ylabel("Accuracy")
plt.grid(True, linestyle='--', alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()
