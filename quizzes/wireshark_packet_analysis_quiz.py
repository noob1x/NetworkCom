# wireshark_packet_analysis_quiz.py

def run_quiz():
    print("\n=== Wireshark Packet Analysis Quiz ===")

    # Define quiz questions and answers
    questions = [
        {
            "question": "1. What is Wireshark used for?\n"
                        "a) Internet speed optimization\n"
                        "b) Packet analysis and network troubleshooting\n"
                        "c) Managing IP addresses\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "2. Which layer of the OSI model does Wireshark primarily operate at?\n"
                        "a) Physical Layer\n"
                        "b) Data Link Layer\n"
                        "c) Network Layer\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "3. What type of information can Wireshark capture?\n"
                        "a) Only IP addresses\n"
                        "b) Only DNS requests\n"
                        "c) All data packets in a network\n"
                        "Your choice: ",
            "answer": "c"
        },
        {
            "question": "4. How does Wireshark display captured packets?\n"
                        "a) In a list format only\n"
                        "b) In a graphical representation only\n"
                        "c) Both in a list and graphical representation\n"
                        "Your choice: ",
            "answer": "c"
        },
        {
            "question": "5. What is the purpose of applying filters in Wireshark?\n"
                        "a) To block unwanted network traffic\n"
                        "b) To focus on specific packets based on criteria\n"
                        "c) To manage IP addresses\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "6. What does the term 'capture filter' refer to in Wireshark?\n"
                        "a) A filter applied after capturing packets\n"
                        "b) A filter used during the capture process\n"
                        "c) A filter for organizing captured data\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "7. Which protocol does Wireshark use to capture packets?\n"
                        "a) TCP/IP\n"
                        "b) UDP\n"
                        "c) ICMP\n"
                        "Your choice: ",
            "answer": "a"
        },
        {
            "question": "8. How can Wireshark help in diagnosing network issues?\n"
                        "a) By enhancing internet speed\n"
                        "b) By identifying abnormal network behavior through packet analysis\n"
                        "c) By blocking unauthorized access\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "9. What is the purpose of Wireshark's 'Follow TCP Stream' feature?\n"
                        "a) To analyze DNS requests\n"
                        "b) To view the content of a TCP connection\n"
                        "c) To manage IP addresses\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "10. Why is Wireshark commonly used in cybersecurity?\n"
                        "a) To improve internet speed\n"
                        "b) To monitor network traffic and identify security threats\n"
                        "c) To encrypt data transmissions\n"
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
