# networking_devices_quiz.py

def run_quiz():
    print("\n=== Networking Devices Quiz ===")

    # Define quiz questions and answers
    questions = [
        {
            "question": "1. What is the primary function of a router in a network?\n"
                        "a) Connects multiple devices within a local network\n"
                        "b) Filters and forwards data between different networks\n"
                        "c) Amplifies network speed\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "2. Which networking device operates at the Data Link Layer of the OSI model?\n"
                        "a) Router\n"
                        "b) Switch\n"
                        "c) Hub\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "3. What is the purpose of a hub in networking?\n"
                        "a) Filters network traffic\n"
                        "b) Amplifies network signals\n"
                        "c) Connects devices within a local network\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "4. Which device is used to connect multiple devices within a local network and broadcast data to all devices?\n"
                        "a) Router\n"
                        "b) Switch\n"
                        "c) Hub\n"
                        "Your choice: ",
            "answer": "c"
        },
        {
            "question": "5. What is the primary function of a switch in networking?\n"
                        "a) Connects different networks\n"
                        "b) Filters and forwards data within a local network\n"
                        "c) Provides wireless connectivity\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "6. Which device is used to extend the range of a wireless network?\n"
                        "a) Switch\n"
                        "b) Router\n"
                        "c) Access Point\n"
                        "Your choice: ",
            "answer": "c"
        },
        {
            "question": "7. What is the purpose of a modem in networking?\n"
                        "a) Connects multiple devices within a local network\n"
                        "b) Converts digital signals to analog signals for transmission\n"
                        "c) Filters network traffic\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "8. What is the role of an access point in a wireless network?\n"
                        "a) Connects different networks\n"
                        "b) Provides secure access to the network\n"
                        "c) Filters and forwards data within a local network\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "9. Which device is responsible for assigning IP addresses to devices in a network?\n"
                        "a) Modem\n"
                        "b) Router\n"
                        "c) DHCP Server\n"
                        "Your choice: ",
            "answer": "c"
        },
        {
            "question": "10. What does VLAN stand for in networking?\n"
                        "a) Very Large Area Network\n"
                        "b) Virtual Local Area Network\n"
                        "c) Volatile Local Access Node\n"
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
