import os  # Import the os module

from lessons import (
    introduction,
    osi_model,
    tcp_ip,
    internet_basics,
    http_https,
    networking_devices,
    network_security_basics,
    firewalls_ids_ips,
    vpns_encryption,
    wireshark_packet_analysis,
    network_configuration,
    cybersecurity_best_practices
)

from quizzes import (
    network_basics_quiz,
    osi_model_quiz,
    tcp_ip_quiz,
    internet_basics_quiz,
    http_https_quiz,
    networking_devices_quiz,
    network_security_basics_quiz,
    firewalls_ids_ips_quiz,
    vpns_encryption_quiz,
    wireshark_packet_analysis_quiz,
    network_configuration_quiz,
    cybersecurity_best_practices_quiz
)

def print_colored_banner():
    # ANSI escape codes for colored text
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'

    print(f"\n{RED}========================")
    print(f"     {GREEN}NetworkCom ")
    print(f"   {YELLOW}Created by Commander X")
    print(f"{RED}========================{RESET}")

def clear_screen():
    # Clear screen based on the operating system
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/MacOS
        os.system('clear')

def run_application():
    print_colored_banner()
    print("Welcome to the Networking learning tool for beginners in cybersecurity!")

    # Display a menu for lessons and quizzes
    while True:
        print("\nChoose an option:")
        print("1. Lessons")
        print("2. Quizzes")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            clear_screen()  # Clear screen before displaying lessons menu
            run_lessons_menu()
        elif choice == "2":
            clear_screen()  # Clear screen before displaying quizzes menu
            run_quizzes_menu()
        elif choice == "3":
            print("Exiting the Tool. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def run_lessons_menu():
    print("\nLessons Menu:")
    print("1. Introduction to Networks")
    print("2. OSI Model")
    print("3. TCP/IP Basics")
    print("4. Internet Basics")
    print("5. HTTP and HTTPS")
    print("6. Networking Devices")
    print("7. Basics of Network Security")
    print("8. Firewalls and IDS/IPS")
    print("9. VPNs and Encryption")
    print("10. Wireshark and Packet Analysis")
    print("11. Network Configuration and Hardening")
    print("12. Cybersecurity Best Practices")
    print("0. Back to main menu")

    lesson_choice = input("Enter your choice (1/2/.../0): ")

    if lesson_choice == "1":
        introduction.run_lesson()
    elif lesson_choice == "2":
        osi_model.run_lesson()
    elif lesson_choice == "3":
        tcp_ip.run_lesson()
    elif lesson_choice == "4":
        internet_basics.run_lesson()
    elif lesson_choice == "5":
        http_https.run_lesson()
    elif lesson_choice == "6":
        networking_devices.run_lesson()
    elif lesson_choice == "7":
        network_security_basics.run_lesson()
    elif lesson_choice == "8":
        firewalls_ids_ips.run_lesson()
    elif lesson_choice == "9":
        vpns_encryption.run_lesson()
    elif lesson_choice == "10":
        wireshark_packet_analysis.run_lesson()
    elif lesson_choice == "11":
        network_configuration.run_lesson()
    elif lesson_choice == "12":
        cybersecurity_best_practices.run_lesson()
    elif lesson_choice == "0":
        pass
    else:
        print("Invalid choice. Please enter a valid option.")

def run_quizzes_menu():
    print("\nQuizzes Menu:")
    print("1. Network Basics Quiz")
    print("2. OSI Model Quiz")
    print("3. TCP/IP Quiz")
    print("4. Internet Basics Quiz")
    print("5. HTTP and HTTPS Quiz")
    print("6. Networking Devices Quiz")
    print("7. Network Security Basics Quiz")
    print("8. Firewalls and IDS/IPS Quiz")
    print("9. VPNs and Encryption Quiz")
    print("10. Wireshark and Packet Analysis Quiz")
    print("11. Network Configuration Quiz")
    print("12. Cybersecurity Best Practices Quiz")
    print("0. Back to main menu")

    quiz_choice = input("Enter your choice (1/2/.../0): ")

    if quiz_choice == "1":
        network_basics_quiz.run_quiz()
    elif quiz_choice == "2":
        osi_model_quiz.run_quiz()
    elif quiz_choice == "3":
        tcp_ip_quiz.run_quiz()
    elif quiz_choice == "4":
        internet_basics_quiz.run_quiz()
    elif quiz_choice == "5":
        http_https_quiz.run_quiz()
    elif quiz_choice == "6":
        networking_devices_quiz.run_quiz()
    elif quiz_choice == "7":
        network_security_basics_quiz.run_quiz()
    elif quiz_choice == "8":
        firewalls_ids_ips_quiz.run_quiz()
    elif quiz_choice == "9":
        vpns_encryption_quiz.run_quiz()
    elif quiz_choice == "10":
        wireshark_packet_analysis_quiz.run_quiz()
    elif quiz_choice == "11":
        network_configuration_quiz.run_quiz()
    elif quiz_choice == "12":
        cybersecurity_best_practices_quiz.run_quiz()
    elif quiz_choice == "0":
        pass
    else:
        print("Invalid choice. Please enter a valid option.")

if __name__ == '__main__':
    run_application()
