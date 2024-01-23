def print_colored_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def print_underlined_colored_title(title, color_code):
    print(print_colored_text("\n=== " + title.upper() + " ===\n", color_code))

def run_lesson():
    print_colored_text("\n\nLet's dive into Network Security Basics!\n", "95")  # "95" represents a light purple color

    # Importance of Network Security
    print_underlined_colored_title("Importance of Network Security", "94")  # "94" represents a light blue color
    print("Network security is crucial to protect sensitive data, maintain user privacy, and ensure the integrity of communication.")
    print("It involves implementing measures to prevent unauthorized access, detect intrusions, and secure data against cyber threats.")

    # Real-world analogy: Home Security System
    print("\n   Real-world Analogy: Home Security System")
    print("   - Think of network security as a home security system.")
    print("   - It includes locks on doors (firewalls), surveillance cameras (monitoring tools), and alarms (intrusion detection) to safeguard the home.")

    # Common Threats to Network Security
    print_underlined_colored_title("Common Threats to Network Security", "92")  # "92" represents a light green color
    print("Understanding potential threats is essential for implementing effective network security measures.")
    
    # Types of Threats
    print("\n   Types of Threats:")
    print("   - Malware: Software designed to harm or exploit systems, including viruses, worms, and ransomware.")
    print("   - Phishing: Deceptive attempts to acquire sensitive information by pretending to be a trustworthy entity.")
    print("   - Denial of Service (DoS): Overloading a system to disrupt or deny services to legitimate users.")
    print("   - Man-in-the-Middle (MitM): Intercepting and manipulating communication between two parties.")

    # Network Security Measures
    print_underlined_colored_title("Network Security Measures", "93")  # "93" represents a light yellow color
    print("Implementing robust network security measures helps mitigate risks and protect against various threats.")
    
    # Security Policies
    print("\n   Security Policies:")
    print("   - Establish clear and comprehensive security policies defining acceptable use, access controls, and incident response.")
    print("   - Regularly update policies to adapt to evolving security threats and technologies.")

    # Firewalls
    print("\n   Firewalls:")
    print("   - Firewalls act as a barrier between internal networks and untrusted external networks, controlling incoming and outgoing traffic.")
    print("   - They can be hardware-based or software-based, and they use rule-based filters to allow or block traffic.")

    # Intrusion Detection Systems (IDS)
    print("\n   Intrusion Detection Systems (IDS):")
    print("   - IDS monitors network and system activities to detect and respond to suspicious behavior or potential security incidents.")
    print("   - It analyzes patterns and anomalies in network traffic, raising alerts when unusual activity is detected.")

    # Virtual Private Network (VPN)
    print("\n   Virtual Private Network (VPN):")
    print("   - VPNs create secure, encrypted connections over the internet, allowing users to access private networks remotely.")
    print("   - They provide confidentiality and protect data from eavesdropping during transmission.")

    # Encryption
    print("\n   Encryption:")
    print("   - Encryption transforms data into a secure format that can only be deciphered with the correct decryption key.")
    print("   - It protects data confidentiality, ensuring that even if intercepted, the information remains unreadable.")

    # Multi-Factor Authentication (MFA)
    print("\n   Multi-Factor Authentication (MFA):")
    print("   - MFA adds an extra layer of security by requiring users to provide multiple forms of identification.")
    print("   - Common factors include passwords, security tokens, and biometrics.")

    # Real-world analogy: Secure Safe
    print("\n   Real-world Analogy: Secure Safe")
    print("   - Envision network security measures as a secure safe.")
    print("   - It requires a combination (MFA), is guarded by a strong door (firewall), and employs surveillance (IDS) to detect any attempts at unauthorized access.")

    # Best Practices for Network Security
    print_underlined_colored_title("Best Practices for Network Security", "96")  # "96" represents a light cyan color
    print("Adhering to best practices enhances overall network security and reduces vulnerabilities.")
    
    # Best Practices
    print("\n   Best Practices:")
    print("   - Regularly update and patch software to address known vulnerabilities.")
    print("   - Educate users on security awareness, including recognizing phishing attempts.")
    print("   - Conduct regular security audits and penetration testing to identify and address weaknesses.")
    print("   - Back up critical data regularly to ensure data recovery in the event of an incident.")

    # Summary
    print_underlined_colored_title("Summary", "95")  # "95" represents a light purple color
    print("\nNetwork security is essential for safeguarding data and maintaining the integrity of communication.")
    print("By understanding threats, implementing security measures, and following best practices, organizations can create a resilient defense against cyber threats.")

if __name__ == "__main__":
    run_lesson()
