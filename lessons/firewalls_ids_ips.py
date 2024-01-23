def print_colored_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def print_underlined_colored_title(title, color_code):
    print(print_colored_text("\n=== " + title.upper() + " ===\n", color_code))

def run_lesson():
    print_colored_text("\n\nLet's explore Firewalls, IDS, and IPS!\n", "95")  # "95" represents a light purple color

    # Firewalls: The Digital Barrier
    print_underlined_colored_title("Firewalls: The Digital Barrier", "94")  # "94" represents a light blue color
    print("A firewall acts as a digital barrier between a trusted internal network and untrusted external networks.")
    print("It monitors and controls incoming and outgoing network traffic based on predetermined security rules.")

    # Real-world analogy: Security Checkpoint at Airport
    print("\n   Real-world Analogy: Security Checkpoint at Airport")
    print("   - Imagine a firewall as a security checkpoint at an airport.")
    print("   - It checks and controls the flow of passengers (data) to ensure that only authorized individuals (safe data) can pass through.")

    # Types of Firewalls
    print("\n   Types of Firewalls:")
    print("   - Packet Filtering Firewalls: Filter packets based on pre-defined rules.")
    print("   - Stateful Inspection Firewalls: Keep track of the state of active connections.")
    print("   - Proxy Firewalls: Act as intermediaries between users and external servers.")
    print("   - Next-Generation Firewalls: Combine traditional firewall features with advanced capabilities like intrusion prevention.")

    # Intrusion Detection Systems (IDS)
    print_underlined_colored_title("Intrusion Detection Systems (IDS)", "92")  # "92" represents a light green color
    print("An IDS monitors network and system activities to detect and respond to suspicious behavior or potential security incidents.")
    print("It analyzes patterns and anomalies in network traffic, raising alerts when unusual activity is detected.")

    # Real-world analogy: Surveillance Cameras
    print("\n   Real-world Analogy: Surveillance Cameras")
    print("   - Think of an IDS as surveillance cameras in a shopping mall.")
    print("   - It constantly observes and analyzes activities, raising an alert if it detects any suspicious behavior.")

    # Types of IDS
    print("\n   Types of IDS:")
    print("   - Network-Based IDS (NIDS): Monitors network traffic for suspicious activities.")
    print("   - Host-Based IDS (HIDS): Monitors activities on individual devices.")
    print("   - Signature-Based IDS: Compares patterns against a database of known attack signatures.")
    print("   - Anomaly-Based IDS: Identifies deviations from established baselines of normal behavior.")

    # Intrusion Prevention Systems (IPS)
    print_underlined_colored_title("Intrusion Prevention Systems (IPS)", "93")  # "93" represents a light yellow color
    print("An IPS goes beyond detection and actively prevents or blocks malicious activities on a network.")
    print("It can automatically respond to threats by blocking or filtering traffic based on predefined security rules.")

    # Real-world analogy: Security Guard Intervention
    print("\n   Real-world Analogy: Security Guard Intervention")
    print("   - Imagine an IPS as a security guard who not only detects suspicious behavior but also intervenes to prevent any harmful actions.")
    print("   - It actively blocks or filters network traffic to stop potential threats.")

    # Differences between IDS and IPS
    print("\n   Differences between IDS and IPS:")
    print("   - IDS: Monitors and alerts about suspicious activities.")
    print("   - IPS: Actively prevents or blocks malicious activities in real-time.")
    print("   - IDS is more passive, while IPS is proactive in responding to threats.")

    # Benefits of Firewalls, IDS, and IPS
    print_underlined_colored_title("Benefits of Firewalls, IDS, and IPS", "94")  # "94" represents a light blue color
    print("Implementing firewalls, IDS, and IPS provides several benefits for network security.")
    
    # Benefits
    print("\n   Benefits:")
    print("   - Network Protection: Defends against unauthorized access and potential cyber threats.")
    print("   - Incident Response: Detects and responds to security incidents promptly.")
    print("   - Data Integrity: Ensures the integrity of data by preventing unauthorized modifications.")
    print("   - Privacy Preservation: Safeguards sensitive information from unauthorized access.")

    # Real-world analogy: Security System for a Mansion
    print("\n   Real-world Analogy: Security System for a Mansion")
    print("   - Envision a network with firewalls, IDS, and IPS as a well-secured mansion.")
    print("   - Firewalls act as gates, IDS as surveillance, and IPS as security guards, ensuring the safety and privacy of the mansion.")

    # Considerations for Implementation
    print_underlined_colored_title("Considerations for Implementation", "96")  # "96" represents a light cyan color
    print("When implementing firewalls, IDS, and IPS, consider the following key aspects:")
    
    # Key Considerations
    print("\n   Key Considerations:")
    print("   - Security Policy Alignment: Ensure that security policies align with the organization's overall security goals.")
    print("   - Regular Updates: Keep firewall rules, IDS signatures, and IPS filters updated to address emerging threats.")
    print("   - Integration with Security Architecture: Integrate these systems seamlessly with the overall security architecture.")
    print("   - Monitoring and Analysis: Regularly monitor alerts and logs for continuous analysis of network activities.")

    # Real-world analogy: Maintenance of a Security System
    print("\n   Real-world Analogy: Maintenance of a Security System")
    print("   - Maintaining network security is akin to regularly servicing a security system for optimal performance.")
    print("   - Regular updates and monitoring are essential for a robust defense against evolving threats.")

    # Summary
    print_underlined_colored_title("Summary", "95")  # "95" represents a light purple color
    print("\nFirewalls, IDS, and IPS are essential components of network security, providing defense against unauthorized access and potential threats.")
    print("Understanding their roles, benefits, and implementation considerations enhances the overall security posture of a network.")

if __name__ == "__main__":
    run_lesson()
