import xml.etree.ElementTree as ET
import pandas as pd
import matplotlib.pyplot as plt

def parse_queue_output(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        queue_data = []
        for data in root.findall('data'):
            timestep = float(data.get('timestep'))
            for lane in data.findall('lanes/lane'):
                lane_id = lane.get('id')
                queueing_time = float(lane.get('queueing_time'))
                queueing_length = float(lane.get('queueing_length'))

                queue_data.append({
                    'timestep': timestep,
                    'lane_id': lane_id,
                    'queueing_time': queueing_time,
                    'queueing_length': queueing_length
                })

        queue_df = pd.DataFrame(queue_data)
        return queue_df
    except ET.ParseError as e:
        print(f"Error parsing XML file: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def display_queue_stats(queue_df):
    if queue_df is None or queue_df.empty:
        print("No data available.")
        return

    total_queues = queue_df['queueing_length'].sum()
    avg_queue_length = queue_df['queueing_length'].mean()
    avg_queue_time = queue_df['queueing_time'].mean()

    print("\n--- Queue Length Analysis ---")
    print(f"Total Queue Length: {total_queues:.2f} vehicles")
    print(f"Average Queue Length: {avg_queue_length:.2f} vehicles")
    print(f"Average Queue Time: {avg_queue_time:.2f} seconds")

def plot_queue_length_over_time(queue_df):
    if queue_df is None or queue_df.empty:
        print("No data available for plotting.")
        return

    grouped_df = queue_df.groupby('timestep')['queueing_length'].sum()

    plt.figure(figsize=(10, 6))
    plt.plot(grouped_df.index, grouped_df.values, marker='o', color='blue')
    plt.title('Total Queue Length Over Time')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Queue Length (vehicles)')
    plt.grid(True)
    plt.show()

def plot_avg_queue_length_per_lane(queue_df):
    if queue_df is None or queue_df.empty:
        print("No data available for plotting.")
        return

    lane_avg_queue = queue_df.groupby('lane_id')['queueing_length'].mean()

    plt.figure(figsize=(12, 6))
    lane_avg_queue.plot(kind='bar', color='green')
    plt.title('Average Queue Length Per Lane')
    plt.xlabel('Lane ID')
    plt.ylabel('Average Queue Length (vehicles)')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    queue_file = r"H:\SUMO- Study Area\queue-output.xml"
    queue_df = parse_queue_output(queue_file)

    display_queue_stats(queue_df)
    plot_queue_length_over_time(queue_df)
    plot_avg_queue_length_per_lane(queue_df)
