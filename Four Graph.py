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
        depart_time = float(trip.get('depart'))
        vehicle_type = trip.get('vType') if trip.get('vType') else 'unknown'

        trip_data.append({
            'Vehicle ID': vehicle_id,
            'Duration': duration,
            'Waiting Time': waiting_time,
            'Depart Time': depart_time,
            'Vehicle Type': vehicle_type
        })

    return pd.DataFrame(trip_data)

def plot_vehicle_flow(df):
    df['Depart Time Bin'] = pd.cut(df['Depart Time'], bins=50)
    vehicle_flow = df.groupby('Depart Time Bin').size()

    plt.figure(figsize=(10, 6))
    vehicle_flow.plot(kind='line')
    plt.title('Vehicle Flow Over Time')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Number of Vehicles Departing')
    plt.grid(True)
    plt.show()

def plot_travel_time_distribution(df):
    plt.figure(figsize=(10, 6))
    plt.hist(df['Duration'], bins=30, color='skyblue', alpha=0.7)
    plt.title('Distribution of Travel Times')
    plt.xlabel('Travel Time (seconds)')
    plt.ylabel('Number of Vehicles')
    plt.grid(True)
    plt.show()

def plot_travel_vs_waiting_time(df):
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Duration'], df['Waiting Time'], alpha=0.6, c='blue')
    plt.title('Travel Time vs Waiting Time')
    plt.xlabel('Travel Time (seconds)')
    plt.ylabel('Waiting Time (seconds)')
    plt.grid(True)
    plt.show()

def plot_vehicle_type_distribution(df):
    vehicle_type_counts = df['Vehicle Type'].value_counts()

    plt.figure(figsize=(8, 8))
    vehicle_type_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['blue', 'green', 'red', 'orange'])
    plt.title('Vehicle Type Distribution')
    plt.ylabel('') 
    plt.show()

if __name__ == "__main__":
    tripinfo_file = r"H:\SUMO- Study Area\tripinfo-output.xml"
    tripinfo_df = parse_tripinfo_data(tripinfo_file)

    plot_vehicle_flow(tripinfo_df)                
    plot_travel_time_distribution(tripinfo_df)   
    plot_travel_vs_waiting_time(tripinfo_df)      
    plot_vehicle_type_distribution(tripinfo_df)
