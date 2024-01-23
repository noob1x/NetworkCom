def print_colored_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def print_underlined_colored_title(title, color_code):
    print(print_colored_text("\n=== " + title.upper() + " ===\n", color_code))

def run_lesson():
    print_colored_text("\n\nLet's dive into the OSI model!\n", "95")  # "95" represents a light purple color

    # What is the OSI Model?
    print_underlined_colored_title("The OSI Model", "94")  # "94" represents a light blue color
    print("The OSI (Open Systems Interconnection) model is a conceptual framework that standardizes the functions of a telecommunication or computing system into seven abstraction layers.")
    print("It helps us understand how different network protocols work together to enable communication between devices.")

    # OSI Model Layers
    print_underlined_colored_title("OSI Model Layers", "92")  # "92" represents a light green color

    # Layer 7: Application
    print("\nLayer 7: Application")
    print("   - The Application layer is where users interact with the software and network.")
    print("   - It provides network services directly to end-users or applications.")
    print("   - Examples: Web browsers, email clients, and file transfer applications.")
    
    # Real-world analogy: Sending a Letter
    print("\n   Real-world Analogy: Sending a Letter")
    print("   - Imagine writing a letter (data) to your friend. The way you write and the language you use is similar to the Application layer.")
    print("   - The letter contains information for the recipient, just like data sent by applications.")

    # Layer 6: Presentation
    print("\nLayer 6: Presentation")
    print("   - The Presentation layer deals with data translation and encryption.")
    print("   - It ensures that data is properly formatted and readable for the Application layer.")
    
    # Real-world analogy: Language Translation
    print("\n   Real-world Analogy: Language Translation")
    print("   - If you write a letter in English (data), but your friend speaks French, a translator is needed.")
    print("   - The Presentation layer is like a translator, ensuring data is understood by both sender and receiver.")

    # Layer 5: Session
    print("\nLayer 5: Session")
    print("   - The Session layer manages sessions or connections between applications.")
    print("   - It establishes, maintains, and terminates communication sessions.")
    
    # Real-world analogy: Phone Call Management
    print("\n   Real-world Analogy: Phone Call Management")
    print("   - When you make a phone call, you initiate the call, talk, and end the call. The Session layer manages this communication session.")
    print("   - It ensures that data is sent and received in the correct order.")

    # Layer 4: Transport
    print("\nLayer 4: Transport")
    print("   - The Transport layer ensures reliable data transfer between devices.")
    print("   - It breaks down large messages into smaller segments and handles error correction and flow control.")
    
    # Real-world analogy: Postal Service
    print("\n   Real-world Analogy: Postal Service")
    print("   - Imagine sending a big package (data) through the postal service. The Transport layer is like packaging the content securely, tracking the delivery, and handling any issues.")

    # Layer 3: Network
    print("\nLayer 3: Network")
    print("   - The Network layer is responsible for logical addressing and routing.")
    print("   - It determines the best path for data to travel from source to destination.")
    
    # Real-world analogy: GPS Navigation
    print("\n   Real-world Analogy: GPS Navigation")
    print("   - When you use GPS to find the best route to your destination, the Network layer is similar, deciding the optimal path for data.")
    print("   - It works with logical addresses (IP addresses) to guide data to its destination.")

    # Layer 2: Data Link
    print("\nLayer 2: Data Link")
    print("   - The Data Link layer deals with physical addressing and error detection.")
    print("   - It frames the data for transmission over the physical medium (e.g., Ethernet).")
    
    # Real-world analogy: Enveloping a Letter
    print("\n   Real-world Analogy: Enveloping a Letter")
    print("   - Before sending a letter, you put it in an envelope. The Data Link layer is like enveloping data for secure delivery.")
    print("   - It adds physical addresses (MAC addresses) to the data frames.")

    # Layer 1: Physical
    print("\nLayer 1: Physical")
    print("   - The Physical layer deals with the actual hardware and transmission of raw binary data.")
    print("   - It defines the characteristics of the hardware, such as cables, switches, and connectors.")
    
    # Real-world analogy: Building a Road
    print("\n   Real-world Analogy: Building a Road")
    print("   - If data transfer is a journey, the Physical layer is like building the road. It focuses on the actual hardware and transmission medium.")
    print("   - It deals with electrical signals, voltage levels, and physical connections.")

    # Summary
    print_underlined_colored_title("Summary", "95")  # "95" represents a light purple color
    print("\nThe OSI model helps us understand how different layers work together to ensure reliable and secure communication between devices.")
    print("Remember the seven layers: Physical, Data Link, Network, Transport, Session, Presentation, and Application.")
    print("Each layer has specific responsibilities, contributing to the efficient flow of data across a network.")

if __name__ == "__main__":
    run_lesson()
