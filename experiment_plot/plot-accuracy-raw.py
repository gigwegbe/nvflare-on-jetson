import matplotlib.pyplot as plt
import pandas as pd

# Load CSVs
df1 = pd.read_csv("acc_data_smoothen/site-1.csv")
df2 = pd.read_csv("acc_data_smoothen/site-2.csv")
df3 = pd.read_csv("acc_data_smoothen/site-3.csv")

# Plotting
plt.figure(figsize=(12, 6))

plt.plot(df1['Step'], df1['Value'], label='client-1', color='#1f77b4')  # dark blue
plt.plot(df2['Step'], df2['Value'], label='client-2', color='#17becf')  # cyan
plt.plot(df3['Step'], df3['Value'], label='client-3', color='#e377c2')  # pink

# Labels and layout
plt.title("accuracy_per_epoch")
plt.xlabel("Epoch (Step)")
plt.ylabel("Accuracy")
plt.grid(True, linestyle='--', alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()
