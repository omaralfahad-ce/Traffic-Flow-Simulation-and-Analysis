import xml.etree.ElementTree as ET
import pandas as pd
import matplotlib.pyplot as plt

def parse_tripinfo_data(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    trip_data = []
    for trip in root.findall('tripinfo'):
        vehicle_id = trip.get('id')
        duration = float(trip.get('duration'))
        waiting_time = float(trip.get('waitingTime'))
        depart_delay = float(trip.get('departDelay'))

        trip_data.append({
            'Vehicle ID': vehicle_id,
            'Duration': duration,
            'Waiting Time': waiting_time,
            'Departure Delay': depart_delay
        })

    return pd.DataFrame(trip_data)

tripinfo_file = r"H:\SUMO- Study Area\tripinfo-output.xml"
tripinfo_df = parse_tripinfo_data(tripinfo_file)

print(tripinfo_df.head())

def plot_travel_waiting_time(df):
    plt.figure(figsize=(10, 6))
    df[['Duration', 'Waiting Time']].boxplot(grid=False)
    plt.title('Travel and Waiting Time Distribution')
    plt.ylabel('Time (seconds)')
    plt.show()

plot_travel_waiting_time(tripinfo_df)
