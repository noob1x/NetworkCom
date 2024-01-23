def print_colored_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def print_underlined_colored_title(title, color_code):
    print(print_colored_text("\n=== " + title.upper() + " ===\n", color_code))

def run_lesson():
    print_colored_text("\n\nLet's explore Network Configuration!\n", "95")  # "95" represents a light purple color

    # Network Configuration Overview
    print_underlined_colored_title("Network Configuration Overview", "94")  # "94" represents a light blue color
    print("Network configuration involves setting up and managing various parameters that define how devices communicate within a network.")
    print("It includes configuring IP addresses, subnet masks, gateways, DNS settings, DHCP, and more.")

    # Real-world analogy: City Infrastructure
    print("\n   Real-world Analogy: City Infrastructure")
    print("   - Envision a network as a city with devices representing buildings.")
    print("   - Network configuration is akin to planning roads (communication paths), assigning addresses (IP addresses) to buildings, and managing traffic (data).")

    # IP Addressing in Network Configuration
    print_underlined_colored_title("IP Addressing in Network Configuration", "92")  # "92" represents a light green color
    print("IP addresses are numerical labels assigned to devices in a network to uniquely identify them and enable communication.")
    
    # IPv4 vs. IPv6
    print("\n   IPv4 vs. IPv6:")
    print("   - IPv4: Limited by the number of available addresses (32-bit).")
    print("   - IPv6: Expands the address space significantly (128-bit) to accommodate the growing number of connected devices.")

    # Real-world analogy: Street Address System Upgrade
    print("\n   Real-world Analogy: Street Address System Upgrade")
    print("   - Think of upgrading from IPv4 to IPv6 as expanding the street address system from a small town to a metropolis.")

    # IP Address Classes
    print_underlined_colored_title("IP Address Classes", "93")  # "93" represents a light yellow color
    print("IP addresses are categorized into classes (A, B, C, D, E) based on their range and purpose.")
    
    # Class A
    print("\n   Class A:")
    print("   - Range: 1.0.0.0 to 126.255.255.255")
    print("   - Example: 10.0.0.1")
    print("   - First octet represents the network, and the remaining three octets are for host addresses.")
    
    # Class B
    print("\n   Class B:")
    print("   - Range: 128.0.0.0 to 191.255.255.255")
    print("   - Example: 172.16.0.1")
    print("   - First two octets represent the network, and the remaining two octets are for host addresses.")
    
    # Class C
    print("\n   Class C:")
    print("   - Range: 192.0.0.0 to 223.255.255.255")
    print("   - Example: 192.168.0.1")
    print("   - First three octets represent the network, and the last octet is for host addresses.")

    # Class D and E
    print("\n   Class D and E:")
    print("   - Class D (224.0.0.0 to 239.255.255.255) is reserved for multicast groups.")
    print("   - Class E (240.0.0.0 to 255.255.255.255) is reserved for experimental purposes.")

    # Calculating Subnet Masks
    print_underlined_colored_title("Calculating Subnet Masks", "94")  # "94" represents a light blue color
    print("Subnetting involves dividing a larger network into smaller sub-networks, each with its own subnet mask.")
    
    # Subnet Mask Notation
    print("\n   Subnet Mask Notation:")
    print("   - Written in the same format as an IP address (e.g., 255.255.255.0).")
    print("   - Consists of network and host portions.")
    
    # Subnetting Example
    print("\n   Subnetting Example:")
    print("   - Original IP address: 192.168.1.0")
    print("   - Subnet mask: 255.255.255.0")
    print("   - Resulting subnets: 192.168.1.0, 192.168.1.1, 192.168.1.2, ..., 192.168.1.255")

    # Real-world analogy: Neighborhood Planning
    print("\n   Real-world Analogy: Neighborhood Planning")
    print("   - Imagine subnetting as planning neighborhoods within a city.")
    print("   - Each neighborhood (subnet) has its own infrastructure, making the overall city (network) more organized and secure.")

    # Default Gateway and Routing
    print_underlined_colored_title("Default Gateway and Routing", "95")  # "95" represents a light purple color
    print("The default gateway is a critical element in network configuration, providing a path for devices to reach destinations outside their subnet.")
    
    # Dynamic Routing vs. Static Routing
    print("\n   Dynamic Routing vs. Static Routing:")
    print("   - Dynamic Routing: Automatically adjusts routes based on network changes.")
    print("   - Static Routing: Requires manual configuration of fixed routes.")

    # Real-world analogy: GPS Navigation System
    print("\n   Real-world Analogy: GPS Navigation System")
    print("   - Compare dynamic routing to using a GPS system that adapts to real-time traffic conditions.")
    print("   - Static routing is akin to choosing fixed routes on a map without real-time updates.")

    # DNS (Domain Name System) Configuration
    print_underlined_colored_title("DNS (Domain Name System) Configuration", "96")  # "96" represents a light cyan color
    print("DNS translates human-readable domain names into IP addresses, simplifying communication between devices.")
    
    # Recursive DNS Query
    print("\n   Recursive DNS Query:")
    print("   - When a device queries a DNS server for a domain name, the DNS server recursively navigates through the hierarchy until it finds the IP address.")

    # Real-world analogy: Library Catalog System
    print("\n   Real-world Analogy: Library Catalog System")
    print("   - Imagine DNS as a library catalog system where users look up books (domain names), and the catalog system provides the corresponding aisle (IP address).")

    # DHCP (Dynamic Host Configuration Protocol)
    print_underlined_colored_title("DHCP (Dynamic Host Configuration Protocol)", "93")  # "93" represents a light yellow color
    print("DHCP automates the assignment of IP addresses to devices, simplifying the network configuration process.")
    
    # DHCP Lease Duration
    print("\n   DHCP Lease Duration:")
    print("   - Devices are assigned IP addresses for a specific duration (lease).")
    print("   - Lease renewal or new assignment occurs when the lease expires.")

    # Real-world analogy: Car Rental Service
    print("\n   Real-world Analogy: Car Rental Service")
    print("   - Compare DHCP to a car rental service where users are provided with vehicles (IP addresses) for a specific rental period (lease).")

    # Network Configuration Best Practices
    print_underlined_colored_title("Network Configuration Best Practices", "95")  # "95" represents a light purple color
    print("Following best practices in network configuration ensures a stable, efficient, and secure network environment.")
    
    # Network Documentation
    print("\n   Network Documentation:")
    print("   - Maintain detailed documentation of network configurations, including IP schemes, subnets, and device assignments.")

    # Security Measures
    print("\n   Security Measures:")
    print("   - Implement firewalls, access controls, and encryption to enhance network security.")

    # Regular Audits
    print("\n   Regular Audits:")
    print("   - Conduct periodic audits to identify and address configuration issues, ensuring the network remains optimized.")

    # Redundancy and Failover
    print("\n   Redundancy and Failover:")
    print("   - Introduce redundancy in critical network components to ensure continuous availability in case of failures.")

    # Real-world analogy: City Planning Guidelines
    print("\n   Real-world Analogy: City Planning Guidelines")
    print("   - Network configuration best practices are similar to adhering to city planning guidelines for a well-organized and secure urban environment.")

    # Summary
    print_underlined_colored_title("Summary", "95")  # "95" represents a light purple color
    print("Network configuration involves setting up parameters such as IP addresses, subnets, gateways, DNS, and DHCP.")
    print("Understanding these concepts and best practices ensures an efficient, secure, and well-organized network environment.")

if __name__ == "__main__":
    run_lesson()
