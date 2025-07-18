import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Load the CSV
df = pd.read_csv("jetson-data.csv")

# Convert 'timestamp' to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Optional: Set as index for time-based plotting
df.set_index('timestamp', inplace=True)

# Plot 1: CPU Usage
plt.figure(figsize=(12, 6))
for cpu in ['CPU1', 'CPU2', 'CPU3', 'CPU4']:
    plt.plot(df.index, df[cpu], label=cpu)
plt.title("CPU Utilization (%)")
plt.xlabel("Time")
plt.ylabel("Usage (%)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot 2: RAM Usage
plt.figure(figsize=(12, 4))
plt.plot(df.index, df['RAM'], label='RAM', color='purple')
plt.title("RAM Usage (fraction of total)")
plt.xlabel("Time")
plt.ylabel("Usage")
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot 3: GPU Usage
plt.figure(figsize=(12, 4))
plt.plot(df.index, df['GPU'], label='GPU Usage', color='green')
plt.title("GPU Utilization (%)")
plt.xlabel("Time")
plt.ylabel("Usage (%)")
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot 4: Temperatures
plt.figure(figsize=(12, 6))
for temp_sensor in ['Temp CPU', 'Temp GPU']:
    plt.plot(df.index, df[temp_sensor], label=temp_sensor)
plt.title("Temperature (°C)")
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot 5: Power Consumption
plt.figure(figsize=(12, 6))
for power_field in ['Power POM_5V_CPU', 'Power POM_5V_GPU', 'Power TOT']:
    plt.plot(df.index, df[power_field], label=power_field)
plt.title("Power Consumption (mW)")
plt.xlabel("Time")
plt.ylabel("Power (mW)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# pip3 install pandas matplotlib
