import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("jetson-data.csv")
df['timestamp'] = pd.to_datetime(df['timestamp'])
df.set_index('timestamp', inplace=True)

# Plot: GPU Utilization vs Power Consumption
plt.figure(figsize=(14, 6))
plt.plot(df.index, df['GPU'], label='GPU Utilization (%)', color='green')
plt.plot(df.index, df['Power POM_5V_GPU'], label='GPU Power (mW)', color='red')
plt.plot(df.index, df['Power TOT'], label='Total Power (mW)', color='orange', linestyle='--')
plt.title("GPU Utilization vs Power Consumption")
plt.xlabel("Time")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot: GPU Utilization vs GPU Temperature
plt.figure(figsize=(14, 6))
plt.plot(df.index, df['GPU'], label='GPU Utilization (%)', color='green')
plt.plot(df.index, df['Temp GPU'], label='GPU Temperature (°C)', color='blue')
plt.title("GPU Utilization vs Temperature")
plt.xlabel("Time")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
