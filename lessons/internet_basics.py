def print_colored_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def print_underlined_colored_title(title, color_code):
    print(print_colored_text("\n=== " + title.upper() + " ===\n", color_code))

def run_lesson():
    print_colored_text("\n\nLet's delve into the basics of the Internet!\n", "95")  # "95" represents a light purple color

    # What is the Internet?
    print_underlined_colored_title("The Internet", "94")  # "94" represents a light blue color
    print("The Internet is a global network of interconnected computers that communicate and share information.")
    print("It allows users to access a vast array of resources, including websites, emails, and online services.")

    # How Does the Internet Work?
    print_underlined_colored_title("How Does the Internet Work?", "92")  # "92" represents a light green color
    print("The internet operates on a client-server model, where users (clients) connect to servers to access information.")
    print("Data is transmitted in packets, small chunks of information, across various networks to reach its destination.")

    # Real-world analogy: Sending Mail
    print("\n   Real-world Analogy: Sending Mail")
    print("   - Think of sending mail as sending data on the internet.")
    print("   - Your letter (data) is broken into smaller envelopes (packets) and sent through a series of postal offices (routers) to reach its destination.")

    # Internet Service Providers (ISPs)
    print_underlined_colored_title("Internet Service Providers (ISPs)", "93")  # "93" represents a light yellow color
    print("ISPs are companies that provide access to the internet for users.")
    print("They offer various types of connections, such as broadband, DSL, or fiber optics, to connect users to the internet.")

    # Real-world analogy: Highway System
    print("\n   Real-world Analogy: Highway System")
    print("   - Imagine the internet as a highway system, and ISPs as on-ramps providing users access to the digital highway.")
    print("   - Each user's connection is like a vehicle on the highway, moving data to and from its destination.")

    # IP Addresses
    print_underlined_colored_title("IP Addresses", "91")  # "91" represents a light red color
    print("IP addresses are unique numerical labels assigned to each device connected to the internet.")
    print("They allow devices to find and communicate with each other.")

    # Real-world analogy: Phone Numbers
    print("\n   Real-world Analogy: Phone Numbers")
    print("   - Consider IP addresses as phone numbers for devices on the internet.")
    print("   - When you want to call someone (send data), you use their phone number (IP address) to connect.")

    # Domain Names and DNS
    print_underlined_colored_title("Domain Names and DNS", "96")  # "96" represents a light cyan color
    print("Domain names, like www.example.com, are human-readable addresses for websites.")
    print("DNS (Domain Name System) translates domain names into IP addresses for computers to locate each other on the internet.")

    # Real-world analogy: Address Book
    print("\n   Real-world Analogy: Address Book")
    print("   - Think of DNS as an address book for the internet.")
    print("   - Instead of memorizing IP addresses (phone numbers), you use domain names (contacts) to access websites (people).")

    # Protocols (HTTP, HTTPS)
    print_underlined_colored_title("Protocols (HTTP, HTTPS)", "94")  # "94" represents a light blue color
    print("Protocols define rules for how data is transmitted on the internet.")
    print("HTTP (Hypertext Transfer Protocol) is used for standard web pages, while HTTPS (Hypertext Transfer Protocol Secure) adds a layer of encryption for secure communication.")

    # Real-world analogy: Language Translation
    print("\n   Real-world Analogy: Language Translation")
    print("   - Imagine protocols as the languages spoken on the internet.")
    print("   - HTTP is like speaking a standard language, while HTTPS is like speaking the same language in a secure, encrypted way.")

    # Browsers and URLs
    print_underlined_colored_title("Browsers and URLs", "95")  # "95" represents a light purple color
    print("Browsers, like Chrome or Firefox, are applications that allow users to access and navigate the internet.")
    print("URLs (Uniform Resource Locators) are web addresses that identify the location of resources on the internet.")

    # Real-world analogy: Travel Guide and Street Addresses
    print("\n   Real-world Analogy: Travel Guide and Street Addresses")
    print("   - Consider browsers as travel guides helping users explore the internet.")
    print("   - URLs are like street addresses, guiding users to specific locations on the internet.")

    # Summary
    print_underlined_colored_title("Summary", "95")  # "95" represents a light purple color
    print("\nThe internet is a vast network connecting devices worldwide, allowing users to access and share information.")
    print("Understand the basics of IP addresses, ISPs, DNS, protocols, and how users interact with the internet through browsers and URLs.")

if __name__ == "__main__":
    run_lesson()
