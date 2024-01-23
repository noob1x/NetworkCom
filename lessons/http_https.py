def print_colored_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def print_underlined_colored_title(title, color_code):
    print(print_colored_text("\n=== " + title.upper() + " ===\n", color_code))

def run_lesson():
    print_colored_text("\n\nLet's explore HTTP and HTTPS!\n", "95")  # "95" represents a light purple color

    # What is HTTP?
    print_underlined_colored_title("HTTP (Hypertext Transfer Protocol)", "94")  # "94" represents a light blue color
    print("HTTP is the foundation of data communication on the World Wide Web.")
    print("It is an application layer protocol used for transferring hypertext, like HTML documents, between clients and servers.")

    # How Does HTTP Work?
    print_underlined_colored_title("How Does HTTP Work?", "92")  # "92" represents a light green color
    print("HTTP operates as a request-response protocol, where clients (browsers) send requests to servers, and servers respond with the requested information.")
    
    # Real-world analogy: Ordering at a Restaurant
    print("\n   Real-world Analogy: Ordering at a Restaurant")
    print("   - Think of making an HTTP request as placing an order at a restaurant.")
    print("   - The client (you) sends a request (order) to the server (chef), and the server responds with the requested data (meal).")

    # Components of an HTTP Request
    print("\n   Components of an HTTP Request:")
    print("   - HTTP Method: Specifies the type of request (GET, POST, etc.)")
    print("   - URL: The address of the resource being requested.")
    print("   - Headers: Additional information about the request.")
    print("   - Body: Data sent with the request (for methods like POST).")

    # Components of an HTTP Response
    print("\n   Components of an HTTP Response:")
    print("   - Status Code: Indicates the success or failure of the request.")
    print("   - Headers: Additional information about the response.")
    print("   - Body: The requested data or information.")

    # What is HTTPS?
    print_underlined_colored_title("HTTPS (Hypertext Transfer Protocol Secure)", "93")  # "93" represents a light yellow color
    print("HTTPS is the secure version of HTTP, adding a layer of encryption to ensure secure communication between clients and servers.")
    print("It uses SSL/TLS protocols to encrypt data and protect it from being intercepted or tampered with by attackers.")

    # How Does HTTPS Work?
    print_underlined_colored_title("How Does HTTPS Work?", "96")  # "96" represents a light cyan color
    print("HTTPS follows the same request-response model as HTTP but adds a layer of security through SSL/TLS encryption.")
    
    # Real-world analogy: Sending a Secret Message
    print("\n   Real-world Analogy: Sending a Secret Message")
    print("   - Imagine sending a secret message that only the recipient can understand.")
    print("   - HTTPS is like using a secure envelope (SSL/TLS) to send the message, making it unreadable to anyone who intercepts it.")

    # SSL/TLS Handshake
    print("\n   SSL/TLS Handshake:")
    print("   - ClientHello: The client initiates the handshake by sending a request to the server.")
    print("   - ServerHello: The server responds, acknowledging the request and agreeing on encryption parameters.")
    print("   - Key Exchange: Both parties exchange cryptographic keys to establish a secure connection.")
    print("   - Finished: The handshake is completed, and secure communication begins.")

    # Benefits of HTTPS
    print_underlined_colored_title("Benefits of HTTPS", "94")  # "94" represents a light blue color
    print("   - Data Encryption: Protects sensitive information from eavesdroppers.")
    print("   - Data Integrity: Ensures that data remains unchanged during transmission.")
    print("   - Authentication: Verifies the identity of the server, preventing man-in-the-middle attacks.")

    # Migrating from HTTP to HTTPS
    print_underlined_colored_title("Migrating from HTTP to HTTPS", "95")  # "95" represents a light purple color
    print("   - Obtain an SSL/TLS Certificate: Purchase or acquire a certificate for your domain.")
    print("   - Install the Certificate: Configure the server to use the certificate for encryption.")
    print("   - Update URLs and References: Ensure all resources are loaded using the secure 'https://' protocol.")
    print("   - Update Redirects: Set up redirects from HTTP to HTTPS to ensure all traffic is secure.")

    # Summary
    print_underlined_colored_title("Summary", "95")  # "95" represents a light purple color
    print("\nUnderstanding HTTP and HTTPS is crucial for secure and efficient communication on the web.")
    print("HTTP is the standard protocol for web communication, while HTTPS adds encryption to protect data and ensure secure connections.")

if __name__ == "__main__":
    run_lesson()
