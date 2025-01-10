# Network-Analyzer
 Network Traffic Analyzer

 Overview
The Network Traffic Analyzer is a Python-based tool designed to capture, analyze, and visualize network traffic in real-time. It utilizes the Scapy library for packet sniffing and the Matplotlib library for data visualization. The tool allows users to inspect network packets, save the data to a CSV file for future analysis, and visualize protocol distributions via bar charts.

---

 Features
1. Packet Capturing
   - Capture a user-specified number of packets in real-time.
2. Packet Analysis
   - Extract relevant details, including:
     - Source IP
     - Destination IP
     - Protocol type
3. Data Export
   - Save captured packet data to a CSV file.
4. Visualization
   - Generate a bar chart displaying the distribution of protocols in the captured packets.

---

 Prerequisites
Before running the project, ensure you have the following:
1. Python 3.8 or later
2. Required Libraries
   - Scapy: For packet sniffing and analysis.
   - Matplotlib: For creating visualizations.
   - CSV (built-in): For saving data to a CSV file.

Install the required libraries using the following commands:
```bash
pip install scapy
pip install matplotlib
```
3. Wireshark (Optional)
   - Wireshark can be installed to compare and validate packet captures.

4. Administrator Privileges
   - On most systems, packet capturing requires elevated privileges.

---

 Usage
1. Clone or Download the Repository
   - Save the script as `network_analyzer.py`.

2. Run the Script
   ```bash
   python network_analyzer.py
   ```

3. Follow the Prompts
   - Enter the number of packets to capture.
   - Provide a filename for saving the data (default: `packet_data.csv`).

4. View Results
   - The script will:
     - Display captured packet summaries.
     - Save the extracted data to a CSV file.
     - Generate a bar chart visualizing protocol distribution.

---

 Output
 CSV File
The CSV file contains the following columns:
| Source IP       | Destination IP  | Protocol     |
|------------------|-----------------|--------------|
| 192.168.1.100   | 192.168.1.1     | TCP          |
| 192.168.1.101   | 8.8.8.8         | UDP          |
| 10.0.0.5        | 10.0.0.1        | ICMP         |

 Visualization
The bar chart displays the distribution of protocols among the captured packets, e.g.:
- TCP: 5 packets
- UDP: 3 packets
- ICMP: 2 packets

---

 Example Walkthrough
1. Start the Script
   ```bash
   python network_analyzer.py
   ```
   Example prompt:
   ```
   Enter the number of packets to capture: 10
   Enter the filename to save the data (default: packet_data.csv):
   ```
2. Captured Data
   ```plaintext
   Capturing 10 packets...
   10 packets captured successfully.
   Packet data saved to packet_data.csv.
   ```
3. Bar Chart Visualization
   The script automatically displays a bar chart of protocol distribution.

---

 Known Issues and Troubleshooting
1. Permission Denied
   - Run the script with administrator privileges:
     ```bash
     sudo python network_analyzer.py   Linux/Mac
     python network_analyzer.py        Run as Administrator on Windows
     ```
2. No Packets Captured
   - Ensure you are connected to an active network.
   - Check firewall settings that may block packet capturing.

---

 Future Improvements
- Add real-time visualization of captured packets.
- Include advanced filtering options (e.g., capture only TCP or UDP packets).
- Implement support for large-scale data storage.
- Enable integration with Wireshark.

---

 License
This project is open-source and licensed under the MIT License.

---

 Contact
For questions or contributions, contact Seyram via [GitHub](https://github.com/seyram7) or email at seyramsepenu51@gmail.com.

---

