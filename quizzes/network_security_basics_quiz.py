# network_security_basics_quiz.py

def run_quiz():
    print("\n=== Network Security Basics Quiz ===")

    # Define quiz questions and answers
    questions = [
        {
            "question": "1. What is the purpose of a firewall in network security?\n"
                        "a) Monitors network traffic\n"
                        "b) Blocks unauthorized access\n"
                        "c) Enhances internet speed\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "2. What does VPN stand for in the context of network security?\n"
                        "a) Virtual Private Network\n"
                        "b) Very Powerful Network\n"
                        "c) Verified Personal Network\n"
                        "Your choice: ",
            "answer": "a"
        },
        {
            "question": "3. What is the primary purpose of antivirus software?\n"
                        "a) Blocking network traffic\n"
                        "b) Detecting and removing malicious software\n"
                        "c) Managing IP addresses\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "4. What is the purpose of encryption in network security?\n"
                        "a) Amplifying network speed\n"
                        "b) Securing data by converting it into a coded format\n"
                        "c) Blocking network attacks\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "5. What is a common method for securing wireless networks?\n"
                        "a) MAC filtering\n"
                        "b) Disabling firewalls\n"
                        "c) Publicly broadcasting SSID\n"
                        "Your choice: ",
            "answer": "a"
        },
        {
            "question": "6. What is the purpose of multi-factor authentication in network security?\n"
                        "a) Managing network connections\n"
                        "b) Enhancing user experience\n"
                        "c) Adding an extra layer of security\n"
                        "Your choice: ",
            "answer": "c"
        },
        {
            "question": "7. Why is regular software patching important for network security?\n"
                        "a) Improves internet speed\n"
                        "b) Fixes software vulnerabilities\n"
                        "c) Blocks network attacks\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "8. What is the purpose of intrusion detection systems in network security?\n"
                        "a) Enhancing user experience\n"
                        "b) Monitoring and alerting on suspicious activities\n"
                        "c) Providing internet access\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "9. What is phishing in the context of network security?\n"
                        "a) Sending malicious emails\n"
                        "b) Blocking network traffic\n"
                        "c) Encrypting data\n"
                        "Your choice: ",
            "answer": "a"
        },
        {
            "question": "10. What is the purpose of a security policy in network security?\n"
                        "a) Enhancing internet speed\n"
                        "b) Defining rules and guidelines for secure practices\n"
                        "c) Providing wireless connectivity\n"
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
