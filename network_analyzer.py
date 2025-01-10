import csv
from scapy.all import sniff
import matplotlib.pyplot as plt
from collections import Counter


#Packet Capturing
def capture_packets(packet_count=50):

    print(f"Capturing {packet_count} packets...")
    packets = sniff(count=packet_count)
    print(f"{packet_count} psckets captured successfully.")
    return packets

#Parsing the Packet Data
def parse_packet_data(packets):
    packet_data = []
    for packet in packets:
        source = packet[0][1].src if hasattr(packet[0][1], 'src') else "Unknown"
        destination = packet[0][1].dst if hasattr(packet[0][1], 'dst') else "Unknown"
        protocol = packet[0][1].name if hasattr(packet[0][1], 'name') else "Unknown"
        packet_data.append({
            "Source IP": source,
            "Destination IP": destination,
            "Protocol": protocol
        })
    print("Packet data parsed successfully.")
    return packet_data

#Writing the Packet Data to a CSV File
def save_to_csv(data, filename="packet_data.csv"):
    keys = data[0].keys()
    with open(filename, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
    print(f"Packet data save to {filename}.")

#Visualise the Data
def visualize_data(packet_data):
    protocols = [packet["Protocol"] for packet in packet_data]
    protocol_counts = Counter(protocols)

    #the Bar Chart
    plt.bar(protocol_counts.keys(), protocol_counts.values(), color='skyblue')
    plt.title("Protocol Distribution")
    plt.xlabel("Protocol")
    plt.ylabel("Count")
    plt.show()

# Main Function
if __name__ == "__main__":
    try:
        packet_count = int(input("Enter the number of packets to capture:"))
        packets = capture_packets(packet_count)

        packet_data = parse_packet_data(packets)

        csv_filename = input("Enter the filename to save the data (default: packet_data.csv)") or "packet_data.csv"
        save_to_csv(packet_data, csv_filename)

        visualize_data(packet_data)
    
    except Exception as e: 
        print(f"An error occured: {e}")