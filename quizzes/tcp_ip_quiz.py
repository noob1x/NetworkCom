# tcp_ip_quiz.py

def run_quiz():
    print("\n=== TCP/IP Quiz ===")

    # Define quiz questions and answers
    questions = [
        {
            "question": "1. What does TCP stand for?\n"
                        "a) Transmission Control Protocol\n"
                        "b) Technical Control Protocol\n"
                        "c) Transport Control Protocol\n"
                        "Your choice: ",
            "answer": "a"
        },
        {
            "question": "2. Which protocol operates at the Network Layer of the OSI model?\n"
                        "a) TCP\n"
                        "b) IP\n"
                        "c) UDP\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "3. What is the purpose of ARP (Address Resolution Protocol) in TCP/IP?\n"
                        "a) Assigning IP addresses\n"
                        "b) Resolving MAC addresses to IP addresses\n"
                        "c) Ensuring reliable delivery of data\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "4. Which port is commonly used for HTTP (Hypertext Transfer Protocol) communication?\n"
                        "a) 80\n"
                        "b) 21\n"
                        "c) 443\n"
                        "Your choice: ",
            "answer": "a"
        },
        {
            "question": "5. What is the primary purpose of ICMP (Internet Control Message Protocol) in TCP/IP?\n"
                        "a) Error reporting\n"
                        "b) Data encryption\n"
                        "c) File transfer\n"
                        "Your choice: ",
            "answer": "a"
        },
        {
            "question": "6. Which TCP/IP protocol is used for sending emails?\n"
                        "a) SMTP\n"
                        "b) FTP\n"
                        "c) SNMP\n"
                        "Your choice: ",
            "answer": "a"
        },
        {
            "question": "7. What does NAT (Network Address Translation) do in TCP/IP?\n"
                        "a) Encrypts network traffic\n"
                        "b) Translates private IP addresses to public IP addresses\n"
                        "c) Allocates IP addresses to devices\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "8. Which protocol is connectionless and suitable for real-time applications?\n"
                        "a) TCP\n"
                        "b) UDP\n"
                        "c) IP\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "9. In TCP, what does the three-way handshake involve?\n"
                        "a) Establishing a connection\n"
                        "b) Closing a connection\n"
                        "c) Data transmission\n"
                        "Your choice: ",
            "answer": "a"
        },
        {
            "question": "10. What is the primary function of DNS (Domain Name System) in TCP/IP?\n"
                        "a) Assigning IP addresses\n"
                        "b) Resolving domain names to IP addresses\n"
                        "c) Ensuring data integrity\n"
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
