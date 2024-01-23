# network_basics_quiz.py

def run_quiz():
    print("\n=== Network Basics Quiz ===")

    # Define quiz questions and answers
    questions = [
        {
            "question": "1. What does IP stand for?\n"
                        "a) Internet Protocol\n"
                        "b) Internet Provider\n"
                        "c) Intranet Protocol\n"
                        "Your choice: ",
            "answer": "a"
        },
        {
            "question": "2. Which of the following is a layer 2 device?\n"
                        "a) Router\n"
                        "b) Hub\n"
                        "c) Switch\n"
                        "Your choice: ",
            "answer": "c"
        },
        {
            "question": "3. What is the purpose of DNS in networking?\n"
                        "a) Dynamic Naming Service\n"
                        "b) Domain Name System\n"
                        "c) Digital Network Server\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "4. What is the default subnet mask for an IP address like 192.168.1.1?\n"
                        "a) 255.0.0.0\n"
                        "b) 255.255.0.0\n"
                        "c) 255.255.255.0\n"
                        "Your choice: ",
            "answer": "c"
        },
        {
            "question": "5. Which protocol is used for secure communication over the web?\n"
                        "a) HTTP\n"
                        "b) FTP\n"
                        "c) HTTPS\n"
                        "Your choice: ",
            "answer": "c"
        },
        {
            "question": "6. What is the purpose of a firewall in network security?\n"
                        "a) Monitor network traffic\n"
                        "b) Block unauthorized access\n"
                        "c) Amplify network speed\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "7. What is the role of a gateway in networking?\n"
                        "a) Connects two different networks\n"
                        "b) Manages network cables\n"
                        "c) Filters spam emails\n"
                        "Your choice: ",
            "answer": "a"
        },
        {
            "question": "8. What does DHCP stand for in networking?\n"
                        "a) Dynamic Host Configuration Protocol\n"
                        "b) Domain Hosting Control Panel\n"
                        "c) Distributed Host Configuration Process\n"
                        "Your choice: ",
            "answer": "a"
        },
        {
            "question": "9. In networking, what is a MAC address?\n"
                        "a) Media Access Control address\n"
                        "b) Master Access Configuration address\n"
                        "c) Multi-layered Authentication Code address\n"
                        "Your choice: ",
            "answer": "a"
        },
        {
            "question": "10. What is a VLAN in networking?\n"
                        "a) Virtual Local Area Network\n"
                        "b) Very Large Area Network\n"
                        "c) Volatile Local Access Node\n"
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
