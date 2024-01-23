def print_colored_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def print_underlined_colored_title(title, color_code):
    print(print_colored_text("\n=== " + title.upper() + " ===\n", color_code))

def run_lesson():
    print_colored_text("\n\nLet's explore the TCP/IP model in depth!\n", "95")  # "95" represents a light purple color

    # What is the TCP/IP Model?
    print_underlined_colored_title("The TCP/IP Model", "94")  # "94" represents a light blue color
    print("The TCP/IP (Transmission Control Protocol/Internet Protocol) model is a robust and widely used suite of protocols that serves as the foundation for internet communication.")
    print("It consists of four layers, each playing a specific role in facilitating the flow of data between devices on a network.")

    # TCP/IP Model Layers
    print_underlined_colored_title("TCP/IP Model Layers", "92")  # "92" represents a light green color

    # Layer 4: Application
    print("\nLayer 4: Application")
    print("   - The Application layer in TCP/IP is responsible for end-user services and communication.")
    print("   - It provides network services directly to applications and enables interaction between the user and the network.")
    
    # Real-world analogy: Post Office Services
    print("\n   Real-world Analogy: Post Office Services")
    print("   - Think of the Application layer as the post office providing various services to the public.")
    print("   - Services include sending and receiving mail (data) through different channels like letters, packages, and express delivery.")

    # Examples of Application Layer Protocols
    print("\n   Examples of Application Layer Protocols:")
    print("   - HTTP (Hypertext Transfer Protocol) for web browsing.")
    print("   - SMTP (Simple Mail Transfer Protocol) for email communication.")
    print("   - FTP (File Transfer Protocol) for file exchange.")

    # Layer 3: Transport
    print("\nLayer 3: Transport")
    print("   - The Transport layer in TCP/IP ensures reliable data transfer between devices.")
    print("   - It manages end-to-end communication, error detection, and flow control.")
    
    # Real-world analogy: Freight Shipping Company
    print("\n   Real-world Analogy: Freight Shipping Company")
    print("   - Picture the Transport layer as a freight shipping company ensuring secure and reliable transportation of goods (data) between locations.")
    print("   - It breaks down large shipments (messages) into manageable containers (segments) for efficient delivery.")

    # Examples of Transport Layer Protocols
    print("\n   Examples of Transport Layer Protocols:")
    print("   - TCP (Transmission Control Protocol) for reliable, connection-oriented communication.")
    print("   - UDP (User Datagram Protocol) for faster, connectionless communication.")

    # Layer 2: Internet
    print("\nLayer 2: Internet")
    print("   - The Internet layer in TCP/IP handles logical addressing and routing.")
    print("   - It determines the best path for data packets to travel from source to destination across different networks.")
    
    # Real-world analogy: GPS Navigation System
    print("\n   Real-world Analogy: GPS Navigation System")
    print("   - Imagine navigating through cities using a GPS system that guides you through different roads and intersections.")
    print("   - The Internet layer guides data packets through various networks based on logical addresses (IP addresses).")

    # Examples of Internet Layer Protocols
    print("\n   Examples of Internet Layer Protocols:")
    print("   - IP (Internet Protocol) for logical addressing.")
    print("   - ICMP (Internet Control Message Protocol) for network diagnostics.")

    # Layer 1: Link
    print("\nLayer 1: Link")
    print("   - The Link layer in TCP/IP corresponds to both the Data Link and Physical layers in the OSI model.")
    print("   - It deals with hardware addressing, framing, and the physical transmission medium.")
    
    # Real-world analogy: Physical Mail Delivery System
    print("\n   Real-world Analogy: Physical Mail Delivery System")
    print("   - Envision the Link layer as a physical mail delivery system that handles the actual transfer of packages (data) between locations.")
    print("   - It adds hardware addresses (MAC addresses) to data frames and ensures reliable transmission over the physical medium.")

    # Examples of Link Layer Protocols
    print("\n   Examples of Link Layer Protocols:")
    print("   - Ethernet for wired networks.")
    print("   - Wi-Fi for wireless networks.")

    # Summary
    print_underlined_colored_title("Summary", "95")  # "95" represents a light purple color
    print("\nThe TCP/IP model is a comprehensive suite of protocols designed to facilitate communication on the internet.")
    print("Remember the four layers: Application, Transport, Internet, and Link.")
    print("Each layer plays a distinct role, contributing to the seamless exchange of data between devices on a network.")

if __name__ == "__main__":
    run_lesson()
