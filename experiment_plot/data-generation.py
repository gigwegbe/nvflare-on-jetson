import csv
import time
from jtop import jtop
from datetime import datetime

# Define output CSV file
csv_filename = "jetson-data.csv"

# Flatten nested dictionaries
def flatten(d, parent_key='', sep='_'):
    items = {}
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten(v, new_key, sep=sep))
        else:
            items[new_key] = v
    return items

# Start jtop logging
with jtop() as jetson:
    if jetson.ok():
        # Grab first set of stats to get the keys
        stats = flatten(jetson.stats)
        fieldnames = ['timestamp'] + list(stats.keys())

        with open(csv_filename, mode='w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            print(f"Logging stats to {csv_filename} every second... Press Ctrl+C to stop.")

            try:
                while jetson.ok():
                    stats = flatten(jetson.stats)
                    stats['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    writer.writerow(stats)
                    f.flush()
                    time.sleep(1)

            except KeyboardInterrupt:
                print("Logging stopped.")
