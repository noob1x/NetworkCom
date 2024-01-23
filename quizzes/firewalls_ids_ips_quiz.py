# firewalls_ids_ips_quiz.py

def run_quiz():
    print("\n=== Firewalls, IDS, and IPS Quiz ===")

    # Define quiz questions and answers
    questions = [
        {
            "question": "1. What is the primary purpose of a firewall?\n"
                        "a) Monitoring network traffic\n"
                        "b) Blocking unauthorized access\n"
                        "c) Enhancing internet speed\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "2. What does IDS stand for in the context of network security?\n"
                        "a) Internet Defense System\n"
                        "b) Intrusion Detection System\n"
                        "c) Internal Data Security\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "3. How does an IDS differ from a firewall?\n"
                        "a) IDS is software-based, while firewalls are hardware-based\n"
                        "b) IDS monitors for suspicious activities, while firewalls block unauthorized access\n"
                        "c) IDS is used for internet speed optimization, while firewalls focus on security\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "4. What is the purpose of an IPS in network security?\n"
                        "a) Monitoring internet speed\n"
                        "b) Blocking malicious activities in real-time\n"
                        "c) Managing IP addresses\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "5. How does an IPS differ from an IDS?\n"
                        "a) IPS focuses on monitoring, while IDS focuses on prevention\n"
                        "b) IPS is hardware-based, while IDS is software-based\n"
                        "c) IPS takes action to block malicious activities, while IDS only alerts\n"
                        "Your choice: ",
            "answer": "c"
        },
        {
            "question": "6. What is the purpose of stateful inspection in firewalls?\n"
                        "a) Analyzing network traffic\n"
                        "b) Blocking unauthorized access\n"
                        "c) Keeping track of the state of active connections\n"
                        "Your choice: ",
            "answer": "c"
        },
        {
            "question": "7. What type of traffic does a proxy firewall inspect?\n"
                        "a) Only incoming traffic\n"
                        "b) Both incoming and outgoing traffic\n"
                        "c) Only outgoing traffic\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "8. What is the role of a signature-based detection in IDS/IPS?\n"
                        "a) Analyzing network behavior\n"
                        "b) Identifying patterns associated with known threats\n"
                        "c) Managing IP addresses\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "9. What is the purpose of heuristics-based detection in IDS/IPS?\n"
                        "a) Analyzing internet speed\n"
                        "b) Detecting unknown or emerging threats based on behavior\n"
                        "c) Blocking unauthorized access\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "10. What does DPI (Deep Packet Inspection) do in network security?\n"
                        "a) Monitors internet speed\n"
                        "b) Analyzes the content of data packets for threats\n"
                        "c) Filters network traffic\n"
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
