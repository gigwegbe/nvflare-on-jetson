import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("jetson-data-4g.csv")

# Convert 'timestamp' to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Set timestamp as index for time-based plotting
df.set_index('timestamp', inplace=True)

# Convert RAM usage to MB (Jetson 4GB = 4096 MB)
df['RAM_MB'] = df['RAM'] * 4096

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

# Plot 2: RAM Usage in MB
plt.figure(figsize=(12, 4))
plt.plot(df.index, df['RAM_MB'], label='RAM Usage (MB)', color='purple')
plt.title("RAM Usage (MB)")
plt.xlabel("Time")
plt.ylabel("MB")
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

# Plot 4: Temperatures (CPU & GPU)
plt.figure(figsize=(12, 6))
for sensor in ['Temp CPU', 'Temp GPU']:
    plt.plot(df.index, df[sensor], label=sensor)
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
