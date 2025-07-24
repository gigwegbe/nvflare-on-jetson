import pandas as pd

# Create a sample DataFrame
data = {'timestamp': pd.to_datetime(['2025-07-18 10:00:00',
                                     '2025-07-18 10:05:30',
                                     '2025-07-18 10:12:15',
                                     '2025-07-18 10:20:00']),
        'power_consumption': [100, 110, 105, 120]}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Get the first timestamp
first_timestamp = df['timestamp'].iloc[0]

# Calculate the relative timestamp as Timedelta objects
df['relative_timedelta'] = df['timestamp'] - first_timestamp

# Convert Timedelta to total seconds and then format to HH:MM:SS string
def format_seconds_to_hms(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f'{int(hours):02}:{int(minutes):02}:{int(seconds):02}'

df['relative_timestamp_hms'] = df['relative_timedelta'].dt.total_seconds().apply(format_seconds_to_hms)

print("\nDataFrame with relative timestamp (HH:MM:SS format):")
print(df)
print("\nData type of 'relative_timestamp_hms' column:", df['relative_timestamp_hms'].dtype)