# network_configuration_quiz.py

def run_quiz():
    print("\n=== Network Configuration Quiz ===")

    # Define quiz questions and answers
    questions = [
        {
            "question": "1. What is the purpose of an IP address in networking?\n"
                        "a) Enhancing internet speed\n"
                        "b) Identifying a device on the network\n"
                        "c) Managing network connections\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "2. What is DHCP used for in network configuration?\n"
                        "a) Assigning IP addresses dynamically\n"
                        "b) Blocking unauthorized access\n"
                        "c) Encrypting network traffic\n"
                        "Your choice: ",
            "answer": "a"
        },
        {
            "question": "3. What is the purpose of subnetting?\n"
                        "a) Increasing internet speed\n"
                        "b) Dividing a large network into smaller, manageable subnetworks\n"
                        "c) Managing IP addresses\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "4. Which command is commonly used to check the IP configuration of a device in a command-line interface?\n"
                        "a) IPCONFIG\n"
                        "b) NETSTAT\n"
                        "c) PING\n"
                        "Your choice: ",
            "answer": "a"
        },
        {
            "question": "5. What is the purpose of a default gateway in network configuration?\n"
                        "a) Blocking unauthorized access\n"
                        "b) Providing a pathway for data to exit the local network\n"
                        "c) Analyzing internet speed\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "6. What is DNS used for in network configuration?\n"
                        "a) Managing IP addresses\n"
                        "b) Converting domain names to IP addresses\n"
                        "c) Enhancing internet speed\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "7. How does NAT (Network Address Translation) contribute to network configuration?\n"
                        "a) By analyzing internet speed\n"
                        "b) By providing additional security layers\n"
                        "c) By allowing multiple devices to share a single public IP address\n"
                        "Your choice: ",
            "answer": "c"
        },
        {
            "question": "8. What is the purpose of a subnet mask in network configuration?\n"
                        "a) Managing network connections\n"
                        "b) Identifying the network portion of an IP address\n"
                        "c) Blocking unauthorized access\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "9. What is the difference between a static and dynamic IP address?\n"
                        "a) Static addresses are assigned by a DHCP server, while dynamic addresses are manually configured\n"
                        "b) Dynamic addresses change over time, while static addresses remain constant\n"
                        "c) There is no difference\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "10. What is the purpose of the 'ipconfig /release' and 'ipconfig /renew' commands?\n"
                        "a) Encrypting network traffic\n"
                        "b) Releasing and renewing IP addresses obtained through DHCP\n"
                        "c) Managing network connections\n"
                        "Your choice: ",
            "answer": "b"
        },
    ]

    # Initialize score
    score = 0

    # Run the quiz
    for i, question_data in enumerate(questions, 1):
        question = question_data["question"]
        correct_answer = question_data["answer"]

        user_choice = input(question).strip().lower()

        if user_choice == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer.upper()}.\n")

    # Display quiz results
    print(f"You scored {score} out of {len(questions)}.\n")

if __name__ == "__main__":
    run_quiz()
