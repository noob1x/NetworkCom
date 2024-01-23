def print_colored_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def print_underlined_colored_title(title, color_code):
    print(print_colored_text("\n=== " + title.upper() + " ===\n", color_code))

def run_lesson():
    print_colored_text("\n\nLet's explore Wireshark and Packet Analysis!\n", "95")  # "95" represents a light purple color

    # Wireshark: The Network Detective
    print_underlined_colored_title("Wireshark: The Network Detective", "94")  # "94" represents a light blue color
    print("Wireshark is a powerful network protocol analyzer that allows you to capture and inspect the data traveling back and forth on a network.")
    print("It provides insights into network behavior, helps troubleshoot issues, and enhances security by identifying potential threats.")

    # Real-world analogy: Traffic Surveillance Camera
    print("\n   Real-world Analogy: Traffic Surveillance Camera")
    print("   - Think of Wireshark as a traffic surveillance camera on a busy road.")
    print("   - It captures and analyzes the flow of traffic (network data), revealing details about each vehicle (packet) and identifying any irregularities.")

    # Capturing Packets with Wireshark
    print_underlined_colored_title("Capturing Packets with Wireshark", "92")  # "92" represents a light green color
    print("Wireshark captures packets traveling through a network, allowing in-depth analysis of their content and structure.")
    
    # Steps to Capture Packets
    print("\n   Steps to Capture Packets:")
    print("   1. Select the Network Interface: Choose the network interface (e.g., Ethernet, Wi-Fi) to capture packets.")
    print("   2. Start Capturing: Initiate the packet capture, and Wireshark will begin capturing data in real-time.")
    print("   3. Analyze Packets: View and analyze captured packets in the Wireshark interface.")
    print("   4. Stop Capturing: Stop the capture process when sufficient data has been collected.")

    # Real-world analogy: Surveillance Operation Room
    print("\n   Real-world Analogy: Surveillance Operation Room")
    print("   - Imagine the Wireshark interface as a surveillance operation room with screens displaying live feeds of network traffic.")
    print("   - Analysts (users) can scrutinize each feed (packet) for details and anomalies.")

    # Packet Analysis in Wireshark
    print_underlined_colored_title("Packet Analysis in Wireshark", "93")  # "93" represents a light yellow color
    print("Analyzing packets in Wireshark involves understanding the details within each packet, including source, destination, protocols, and payload.")
    
    # Packet Details
    print("\n   Packet Details:")
    print("   - Source and Destination Addresses: Identify the origin and destination of each packet.")
    print("   - Protocols: Determine the protocols used in the communication (e.g., TCP, UDP).")
    print("   - Payload: Examine the payload, which contains the actual data being transmitted.")
    print("   - Time Information: View the timing details of packet transmission.")

    # Real-world analogy: Postal Package Inspection
    print("\n   Real-world Analogy: Postal Package Inspection")
    print("   - Visualize each packet as a sealed postal package.")
    print("   - Analysts inspect the package for sender, recipient, type of content (protocol), and timing details.")

    # Filtering and Searching in Wireshark
    print_underlined_colored_title("Filtering and Searching in Wireshark", "94")  # "94" represents a light blue color
    print("Wireshark provides powerful filtering and searching capabilities to focus on specific packets and extract relevant information.")
    
    # Filter Examples
    print("\n   Filter Examples:")
    print("   - IP Address Filter: Display packets involving a specific IP address.")
    print("   - Protocol Filter: Filter packets based on a specific protocol (e.g., TCP, UDP).")
    print("   - Time Range Filter: Analyze packets transmitted within a specific time range.")
    print("   - Keyword Search: Search for specific keywords within packet contents.")

    # Real-world analogy: Library Catalog System
    print("\n   Real-world Analogy: Library Catalog System")
    print("   - Think of Wireshark filters as a library catalog system.")
    print("   - Users can filter and search for specific books (packets) based on criteria like author (IP address) or genre (protocol).")

    # Practical Applications of Wireshark
    print_underlined_colored_title("Practical Applications of Wireshark", "95")  # "95" represents a light purple color
    print("Wireshark is a versatile tool with numerous practical applications, including network troubleshooting, security analysis, and protocol development.")
    
    # Applications
    print("\n   Applications:")
    print("   - Troubleshooting Network Issues: Identify and analyze network problems for efficient resolution.")
    print("   - Security Analysis: Detect and investigate security threats by examining abnormal network behavior.")
    print("   - Protocol Development: Assist in developing and optimizing network protocols.")
    print("   - Educational Purposes: Learn and teach networking concepts through practical packet analysis.")

    # Real-world analogy: Network Investigation Unit
    print("\n   Real-world Analogy: Network Investigation Unit")
    print("   - Envision Wireshark as a network investigation unit, helping professionals troubleshoot issues, identify threats, and improve network protocols.")

    # Advanced Wireshark Functionalities
    print_underlined_colored_title("Advanced Wireshark Functionalities", "96")  # "96" represents a light cyan color
    print("Wireshark offers advanced functionalities to enhance packet analysis and cater to diverse network scenarios.")
    
    # Advanced Features
    print("\n   Advanced Features:")
    print("   - Follow TCP Stream: Reconstruct and view the entire content of a TCP conversation.")
    print("   - Statistical Analysis: Utilize built-in statistics for a quick overview of network activity.")
    print("   - Coloring Rules: Customize packet coloring based on specific criteria for better visualization.")
    print("   - Exporting Data: Export packet data for further analysis or sharing with colleagues.")

    # Real-world analogy: Crime Scene Investigation Kit
    print("\n   Real-world Analogy: Crime Scene Investigation Kit")
    print("   - Consider advanced Wireshark features as tools in a crime scene investigation kit.")
    print("   - They help investigators reconstruct events, analyze patterns, and present findings effectively.")

    # Wireshark in Cybersecurity
    print_underlined_colored_title("Wireshark in Cybersecurity", "94")  # "94" represents a light blue color
    print("Wireshark plays a crucial role in cybersecurity, providing insights into network activities and aiding in the detection of malicious behavior.")
    
    # Cybersecurity Applications
    print("\n   Cybersecurity Applications:")
    print("   - Malware Analysis: Examine network traffic to identify patterns associated with malware.")
    print("   - Intrusion Detection: Detect and analyze anomalous activities that may indicate a security breach.")
    print("   - Forensic Investigations: Use packet captures as evidence in forensic investigations.")
    print("   - Security Awareness Training: Educate users about potential threats through practical demonstrations.")

    # Real-world analogy: Cybersecurity Surveillance Center
    print("\n   Real-world Analogy: Cybersecurity Surveillance Center")
    print("   - Visualize Wireshark in cybersecurity as a surveillance center equipped with tools for detecting and analyzing cyber threats.")
    print("   - Analysts use Wireshark to monitor and respond to potential security incidents.")

    # Summary
    print_underlined_colored_title("Summary", "95")  # "95" represents a light purple color
    print("Wireshark serves as a valuable tool for capturing and analyzing network packets, offering insights into network behavior and facilitating various applications.")
    print("Understanding packet analysis in Wireshark enhances network troubleshooting, security analysis, and educational endeavors.")

if __name__ == "__main__":
    run_lesson()
