# vpns_encryption_quiz.py

def run_quiz():
    print("\n=== VPNs and Encryption Quiz ===")

    # Define quiz questions and answers
    questions = [
        {
            "question": "1. What does VPN stand for?\n"
                        "a) Virtual Private Network\n"
                        "b) Very Powerful Network\n"
                        "c) Verified Personal Network\n"
                        "Your choice: ",
            "answer": "a"
        },
        {
            "question": "2. What is the primary purpose of a VPN?\n"
                        "a) Enhancing internet speed\n"
                        "b) Securing communication over an untrusted network\n"
                        "c) Managing IP addresses\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "3. Which encryption protocol is commonly used in VPNs?\n"
                        "a) DES\n"
                        "b) AES\n"
                        "c) RSA\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "4. What is the role of tunneling in VPNs?\n"
                        "a) Managing network connections\n"
                        "b) Creating a secure pathway for data transmission\n"
                        "c) Analyzing internet speed\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "5. What is the purpose of a VPN client?\n"
                        "a) Blocking network traffic\n"
                        "b) Initiating a connection to the VPN server\n"
                        "c) Managing IP addresses\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "6. How does SSL/TLS contribute to VPN security?\n"
                        "a) Analyzing internet speed\n"
                        "b) Providing a secure communication channel through encryption\n"
                        "c) Blocking unauthorized access\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "7. What is the purpose of IPsec in VPNs?\n"
                        "a) Enhancing user experience\n"
                        "b) Providing a framework for secure communication\n"
                        "c) Managing network connections\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "8. Why is PPTP (Point-to-Point Tunneling Protocol) considered less secure than other VPN protocols?\n"
                        "a) Slower internet speed\n"
                        "b) Lack of encryption for data transmission\n"
                        "c) Difficulty in managing IP addresses\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "9. What is the purpose of split tunneling in VPNs?\n"
                        "a) Managing network connections\n"
                        "b) Diverting only specific traffic through the VPN\n"
                        "c) Analyzing internet speed\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "10. How does a VPN help in bypassing geo-restrictions?\n"
                        "a) By blocking unwanted network traffic\n"
                        "b) By providing a virtual IP address from an allowed region\n"
                        "c) By enhancing internet speed\n"
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
