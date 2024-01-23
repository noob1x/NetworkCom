def print_colored_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def print_underlined_colored_title(title, color_code):
    print(print_colored_text("\n=== " + title.upper() + " ===\n", color_code))

def run_lesson():
    print_colored_text("\n\nLet's learn about networks!\n", "95")  # "95" represents a light purple color

    # What is a Network?
    print_underlined_colored_title("Introduction to Networks", "94")  # "94" represents a light blue color
    print("A network is like a digital playground where computers, tablets, and phones talk to each other.")
    
    # Real-world analogy: Friends in a Playground
    print("\nImagine a playground where friends share toys and information. Similarly, in a network, devices share data.")

    # Types of Networks
    print_underlined_colored_title("Types of Networks", "92")  # "92" represents a light green color
    # Real-world analogy: LAN is like a Home, WAN is like the City
    print("\n1. LAN (Local Area Network) is like your home. Devices inside your home, like computers and printers, can easily talk to each other.")
    print("   For example, when you play a game with your friends at home using tablets or computers, that's like a small LAN.")
    print("\n2. WAN (Wide Area Network) is like a city. It connects different homes (LANs) together, often using the internet.")
    print("   Just like how you can send a message to a friend in another part of the city, devices on a WAN can communicate across long distances.")

    # The Internet
    print_underlined_colored_title("The Internet", "93")  # "93" represents a light yellow color
    # Real-world analogy: Internet is like Mail
    print("\nThink of the Internet as a giant postal system. You send and receive information, just like sending and receiving letters.")
    print("   When you watch videos on YouTube or play online games with friends, you're using the Internet.")

    # IP Addresses
    print_underlined_colored_title("IP Addresses", "91")  # "91" represents a light red color
    # Real-world analogy: IP Address is like a Home Address
    print("\nAn IP address is like a home address. It helps data find its way to the right device, just like mail goes to the correct home.")
    print("   For instance, when you visit a website, your device uses an IP address to find the server where the website is hosted.")

    # Protocols
    print_underlined_colored_title("Protocols", "96")  # "96" represents a light cyan color
    # Real-world analogy: Protocols are like Speaking the Same Language
    print("\nImagine if friends spoke different languages on the playground. It would be confusing! Protocols ensure devices 'speak' the same language.")
    print("   When you open a website, your web browser and the website server use protocols to understand each other.")
    
    # Wireless Networks
    print_underlined_colored_title("Wireless Networks", "94")  # "94" represents a light blue color
    # Real-world analogy: Wi-Fi is like Magic
    print("\nNowadays, many networks are wireless, like Wi-Fi.")
    print("   Wi-Fi is like magic! You can connect your devices to the internet without any physical cables.")
    print("   Just like using a remote control to change channels on the TV, Wi-Fi lets you connect to the internet from anywhere in your home.")

    # Summary
    print_underlined_colored_title("Summary", "95")  # "95" represents a light purple color
    print("Understanding networks is like exploring a digital playground where devices communicate and share information.")
    print("Key concepts include:")
    print("   - Different types of networks, such as LANs (like homes) and WANs (like cities).")
    print("   - The Internet as a vast postal system for sending and receiving information.")
    print("   - IP addresses serving as home addresses for devices.")
    print("   - Protocols ensuring devices 'speak' the same language.")
    print("   - The magic of wireless networks, like Wi-Fi, enabling cable-free connectivity.")
    print("Embark on this digital adventure to grasp the foundations of how our connected world operates!")

if __name__ == "__main__":
    run_lesson()
