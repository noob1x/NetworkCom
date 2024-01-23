# internet_basics_quiz.py

def run_quiz():
    print("\n=== Internet Basics Quiz ===")

    # Define quiz questions and answers
    questions = [
        {
            "question": "1. What does URL stand for?\n"
                        "a) Uniform Resource Locator\n"
                        "b) Universal Resource Locator\n"
                        "c) Unified Resource Locator\n"
                        "Your choice: ",
            "answer": "a"
        },
        {
            "question": "2. Which protocol is commonly used for secure data transmission over the web?\n"
                        "a) HTTP\n"
                        "b) FTP\n"
                        "c) HTTPS\n"
                        "Your choice: ",
            "answer": "c"
        },
        {
            "question": "3. What is the primary purpose of DNS (Domain Name System) in internet communication?\n"
                        "a) Assigning IP addresses\n"
                        "b) Resolving domain names to IP addresses\n"
                        "c) Ensuring data encryption\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "4. Which device is used to connect multiple computers within a local network?\n"
                        "a) Router\n"
                        "b) Hub\n"
                        "c) Modem\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "5. What is the purpose of an IP address in internet communication?\n"
                        "a) Identifying a device on the network\n"
                        "b) Ensuring secure data transmission\n"
                        "c) Managing internet speed\n"
                        "Your choice: ",
            "answer": "a"
        },
        {
            "question": "6. What does ISP stand for?\n"
                        "a) Internet Service Provider\n"
                        "b) Internet Security Protocol\n"
                        "c) Internal System Process\n"
                        "Your choice: ",
            "answer": "a"
        },
        {
            "question": "7. Which of the following is not a web browser?\n"
                        "a) Chrome\n"
                        "b) Python\n"
                        "c) Firefox\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "8. What is the purpose of a firewall in internet security?\n"
                        "a) Monitoring network traffic\n"
                        "b) Blocking unauthorized access\n"
                        "c) Enhancing internet speed\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "9. What does HTML stand for?\n"
                        "a) Hyperlink Text Markup Language\n"
                        "b) Hypertext Transfer Markup Language\n"
                        "c) High-Level Text Management Language\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "10. Which protocol is used for sending and receiving emails?\n"
                        "a) SMTP\n"
                        "b) FTP\n"
                        "c) HTTP\n"
                        "Your choice: ",
            "answer": "a"
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
