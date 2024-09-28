import xml.etree.ElementTree as ET
import pandas as pd
import matplotlib.pyplot as plt

def parse_vehicle_data(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    vehicle_data = []
    for vehicle in root.findall('vehicle'):
        vehicle_id = vehicle.get('id')
        depart_time = float(vehicle.get('depart'))
        arrival_time = float(vehicle.get('arrival'))
        vehicle_type = vehicle.get('type')
        route_edges = vehicle.find('route').get('edges')

        vehicle_data.append({
            'Vehicle ID': vehicle_id,
            'Vehicle Type': vehicle_type,
            'Depart Time': depart_time,
            'Arrival Time': arrival_time,
            'Route Edges': route_edges
        })
    
    return pd.DataFrame(vehicle_data)

def calculate_travel_time(df):
    df['Travel Time'] = df['Arrival Time'] - df['Depart Time']
    return df

def generate_statistics(df):
    avg_travel_time = df['Travel Time'].mean()
    print(f"Average Travel Time: {avg_travel_time:.2f} seconds")

    travel_time_by_type = df.groupby('Vehicle Type')['Travel Time'].mean()
    print("\nAverage Travel Time by Vehicle Type:")
    print(travel_time_by_type)

    df.boxplot(column='Travel Time', by='Vehicle Type', grid=False)
    plt.title('Travel Time by Vehicle Type')
    plt.xlabel('Vehicle Type')
    plt.ylabel('Travel Time (seconds)')
    plt.show()

vehroute_file = r"H:\SUMO- Study Area\vehroute-output.xml"
vehicle_df = parse_vehicle_data(vehroute_file)
vehicle_df = calculate_travel_time(vehicle_df)

print(vehicle_df.head())

generate_statistics(vehicle_df)
