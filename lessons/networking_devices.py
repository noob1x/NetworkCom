def print_colored_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def print_underlined_colored_title(title, color_code):
    print(print_colored_text("\n=== " + title.upper() + " ===\n", color_code))

def run_lesson():
    print_colored_text("\n\nLet's explore Networking Devices!\n", "95")  # "95" represents a light purple color

    # Introduction to Networking Devices
    print_underlined_colored_title("Introduction to Networking Devices", "94")  # "94" represents a light blue color
    print("Networking devices play a crucial role in the functioning of computer networks.")
    print("They are specialized hardware components that enable communication and data transfer between devices on a network.")

    # Router
    print_underlined_colored_title("Router", "92")  # "92" represents a light green color
    print("A router is a networking device that connects multiple networks and directs data between them.")
    print("It uses IP addresses to determine the best path for data packets to reach their destination.")

    # Real-world analogy: Traffic Intersection
    print("\n   Real-world Analogy: Traffic Intersection")
    print("   - Imagine a router as a traffic intersection directing vehicles (data packets) to different roads (networks).")
    print("   - It uses traffic rules (routing protocols) to efficiently manage the flow of data.")

    # Switch
    print_underlined_colored_title("Switch", "93")  # "93" represents a light yellow color
    print("A switch is a device that connects multiple devices within the same local network.")
    print("It uses MAC addresses to forward data directly to the device it is intended for, improving network efficiency.")

    # Real-world analogy: Post Office Sorting Center
    print("\n   Real-world Analogy: Post Office Sorting Center")
    print("   - Picture a switch as a sorting center at a post office.")
    print("   - It efficiently sorts and sends letters (data) to their specific destinations (devices) based on addresses (MAC addresses).")

    # Hub
    print_underlined_colored_title("Hub", "91")  # "91" represents a light red color
    print("A hub is a basic networking device that connects multiple devices in a network.")
    print("It operates at the physical layer of the OSI model, broadcasting data to all connected devices.")

    # Real-world analogy: Megaphone Announcement
    print("\n   Real-world Analogy: Megaphone Announcement")
    print("   - Think of a hub as a person with a megaphone announcing information to everyone in a room.")
    print("   - It broadcasts data to all connected devices, regardless of whether they need the information.")

    # Modem
    print_underlined_colored_title("Modem", "96")  # "96" represents a light cyan color
    print("A modem (modulator-demodulator) is a device that modulates and demodulates analog signals to enable digital data transmission over communication channels.")
    print("It is commonly used for connecting to the internet over phone lines or cable systems.")

    # Real-world analogy: Translator at a Language Conference
    print("\n   Real-world Analogy: Translator at a Language Conference")
    print("   - Imagine a modem as a translator at a language conference.")
    print("   - It converts digital language (data) into a format suitable for transmission over a specific medium (analog signals).")

    # Firewall
    print_underlined_colored_title("Firewall", "94")  # "94" represents a light blue color
    print("A firewall is a security device that monitors and controls incoming and outgoing network traffic.")
    print("It acts as a barrier between a trusted internal network and untrusted external networks, preventing unauthorized access.")

    # Real-world analogy: Security Checkpoint at Airport
    print("\n   Real-world Analogy: Security Checkpoint at Airport")
    print("   - Consider a firewall as a security checkpoint at an airport.")
    print("   - It checks and controls the flow of passengers (data) to ensure that only authorized individuals (safe data) can pass through.")

    # Access Point
    print_underlined_colored_title("Access Point", "95")  # "95" represents a light purple color
    print("An access point (AP) is a device that allows wireless devices to connect to a wired network using Wi-Fi.")
    print("It acts as a bridge between wireless clients and the wired network infrastructure.")

    # Real-world analogy: Wi-Fi Hotspot in a Cafe
    print("\n   Real-world Analogy: Wi-Fi Hotspot in a Cafe")
    print("   - Visualize an access point as a Wi-Fi hotspot in a cafe.")
    print("   - It enables customers (wireless devices) to connect to the cafe's network (wired infrastructure) wirelessly.")

    # Summary
    print_underlined_colored_title("Summary", "95")  # "95" represents a light purple color
    print("\nNetworking devices are essential for the smooth functioning of computer networks.")
    print("Routers, switches, hubs, modems, firewalls, and access points each serve specific roles in facilitating communication and ensuring network security.")

if __name__ == "__main__":
    run_lesson()
