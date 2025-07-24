import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("jetson-data-2g.csv")

# Convert 'timestamp' column to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Step 1: Create timedelta from first timestamp
df['relative_timedelta'] = df['timestamp'] - df['timestamp'].iloc[0]
df['seconds'] = df['relative_timedelta'].dt.total_seconds()
df['timedelta'] = pd.to_timedelta(df['seconds'], unit='s')

# Set timedelta as index for resampling
df.set_index('timedelta', inplace=True)

# Step 2: Resample every 5 seconds — keep only numeric columns for mean
numeric_df = df.select_dtypes(include='number')  # filters only numeric columns
df_downsampled = numeric_df.resample('5s').mean().dropna()

# Step 3: Restore readable timestamp index for plotting
df_downsampled['timestamp'] = df_downsampled.index.total_seconds().map(
    lambda x: f"{int(x // 3600):02}:{int((x % 3600) // 60):02}:{int(x % 60):02}"
)
df_downsampled.set_index('timestamp', inplace=True)

# Convert RAM to MB (Jetson 4GB = 4096MB)
df_downsampled['RAM_MB'] = df_downsampled['RAM'] * 2048

# Prepare ticks
xtick_interval = max(len(df_downsampled) // 20, 1)
xticks = df_downsampled.index[::xtick_interval]

# Plot 1: CPU
plt.figure(figsize=(12, 6))
for cpu in ['CPU1', 'CPU2', 'CPU3', 'CPU4']:
    if cpu in df_downsampled:
        plt.plot(df_downsampled.index, df_downsampled[cpu], label=cpu)
plt.title("CPU Utilization (%) - 2GB")
plt.xlabel("Time")
plt.ylabel("Usage (%)")
plt.legend()
plt.xticks(xticks, rotation=45)
plt.tight_layout()
plt.show()

# Plot 2: RAM
plt.figure(figsize=(12, 4))
plt.plot(df_downsampled.index, df_downsampled['RAM_MB'], label='RAM (MB)', color='purple')
plt.title("RAM Usage (MB) - 2GB")
plt.xlabel("Time")
plt.ylabel("MB")
plt.xticks(xticks, rotation=45)
plt.tight_layout()
plt.show()

# Plot 3: GPU
plt.figure(figsize=(12, 4))
if 'GPU' in df_downsampled:
    plt.plot(df_downsampled.index, df_downsampled['GPU'], label='GPU Usage', color='green')
plt.title("GPU Utilization (%) - 2GB")
plt.xlabel("Time")
plt.ylabel("Usage (%)")
plt.xticks(xticks, rotation=45)
plt.tight_layout()
plt.show()

# Plot 4: Temperature
plt.figure(figsize=(12, 6))
for sensor in ['Temp CPU', 'Temp GPU']:
    if sensor in df_downsampled:
        plt.plot(df_downsampled.index, df_downsampled[sensor], label=sensor)
plt.title("Temperature (°C)")
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.xticks(xticks, rotation=45)
plt.tight_layout()
plt.show()

# Plot 5: Power
plt.figure(figsize=(12, 6))
for power in ['Power POM_5V_CPU', 'Power POM_5V_GPU', 'Power TOT']:
    if power in df_downsampled:
        plt.plot(df_downsampled.index, df_downsampled[power], label=power)
plt.title("Power Consumption (mW)")
plt.xlabel("Time")
plt.ylabel("Power (mW)")
plt.legend()
plt.xticks(xticks, rotation=45)
plt.tight_layout()
plt.show()
