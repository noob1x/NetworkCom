# cybersecurity_best_practices_quiz.py

def run_quiz():
    print("\n=== Cybersecurity Best Practices Quiz ===")

    # Define quiz questions and answers
    questions = [
        {
            "question": "1. What is the purpose of a strong password?\n"
                        "a) Enhancing internet speed\n"
                        "b) Protecting against unauthorized access\n"
                        "c) Managing IP addresses\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "2. Why is it important to keep software up-to-date for cybersecurity?\n"
                        "a) To improve internet speed\n"
                        "b) To fix software vulnerabilities and security flaws\n"
                        "c) To manage network connections\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "3. What is multi-factor authentication, and why is it recommended?\n"
                        "a) Enhancing user experience\n"
                        "b) Using multiple methods to verify identity, adding an extra layer of security\n"
                        "c) Blocking unauthorized access\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "4. How can social engineering attacks be prevented?\n"
                        "a) By blocking unwanted network traffic\n"
                        "b) By educating users and promoting awareness\n"
                        "c) By encrypting network traffic\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "5. Why is it important to backup data regularly for cybersecurity?\n"
                        "a) To improve internet speed\n"
                        "b) To ensure data recovery in case of data loss or cyber attacks\n"
                        "c) To manage IP addresses\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "6. What is the purpose of antivirus software in cybersecurity?\n"
                        "a) Blocking network traffic\n"
                        "b) Detecting and removing malicious software\n"
                        "c) Enhancing internet speed\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "7. How can public Wi-Fi networks pose a security risk?\n"
                        "a) By slowing down internet speed\n"
                        "b) By exposing sensitive data to potential attackers\n"
                        "c) By blocking unauthorized access\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "8. What is the purpose of a VPN in cybersecurity?\n"
                        "a) To manage IP addresses\n"
                        "b) To provide a secure and encrypted connection over the internet\n"
                        "c) To enhance internet speed\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "9. How can physical security measures contribute to overall cybersecurity?\n"
                        "a) By improving internet speed\n"
                        "b) By preventing unauthorized physical access to devices\n"
                        "c) By blocking network traffic\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "10. Why is user education and awareness crucial for cybersecurity?\n"
                        "a) To manage network connections\n"
                        "b) To help users recognize and avoid security threats\n"
                        "c) To encrypt network traffic\n"
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
