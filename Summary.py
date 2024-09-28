import xml.etree.ElementTree as ET
import pandas as pd
import matplotlib.pyplot as plt

def parse_summary_output(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        summary_data = []

        for step in root.findall('step'):
            time = float(step.get('time'))
            inserted = int(step.get('inserted'))
            mean_speed = float(step.get('meanSpeed'))
            mean_waiting_time = float(step.get('meanWaitingTime'))

            summary_data.append({
                'time': time,
                'inserted': inserted,
                'mean_speed': mean_speed,
                'mean_waiting_time': mean_waiting_time
            })

        summary_df = pd.DataFrame(summary_data)
        return summary_df
    except ET.ParseError as e:
        print(f"Error parsing XML file: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def plot_mean_speed_over_time(summary_df):
    if summary_df is None or summary_df.empty:
        print("No data available for plotting.")
        return

    plt.figure(figsize=(10, 6))
    plt.plot(summary_df['time'], summary_df['mean_speed'], marker='o', color='blue')
    plt.title('Mean Speed Over Time')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Mean Speed (m/s)')
    plt.grid(True)
    plt.show()

def plot_mean_waiting_time_over_time(summary_df):
    if summary_df is None or summary_df.empty:
        print("No data available for plotting.")
        return

    plt.figure(figsize=(10, 6))
    plt.plot(summary_df['time'], summary_df['mean_waiting_time'], marker='o', color='red')
    plt.title('Mean Waiting Time Over Time')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Mean Waiting Time (seconds)')
    plt.grid(True)
    plt.show()

def plot_vehicles_inserted_over_time(summary_df):
    if summary_df is None or summary_df.empty:
        print("No data available for plotting.")
        return

    plt.figure(figsize=(10, 6))
    plt.plot(summary_df['time'], summary_df['inserted'], marker='o', color='green')
    plt.title('Number of Vehicles Inserted Over Time')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Number of Vehicles')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    summary_file = r"H:\SUMO- Study Area\summary-output.xml"

    summary_df = parse_summary_output(summary_file)

    plot_mean_speed_over_time(summary_df)

    plot_mean_waiting_time_over_time(summary_df)

    plot_vehicles_inserted_over_time(summary_df)
