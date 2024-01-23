# http_https_quiz.py

def run_quiz():
    print("\n=== HTTP and HTTPS Quiz ===")

    # Define quiz questions and answers
    questions = [
        {
            "question": "1. What does HTTP stand for?\n"
                        "a) HyperText Transfer Protocol\n"
                        "b) HyperText Transport Protocol\n"
                        "c) High-Level Text Protocol\n"
                        "Your choice: ",
            "answer": "a"
        },
        {
            "question": "2. Which port is commonly used for HTTP communication?\n"
                        "a) 80\n"
                        "b) 443\n"
                        "c) 21\n"
                        "Your choice: ",
            "answer": "a"
        },
        {
            "question": "3. What is the primary purpose of HTTPS?\n"
                        "a) Handling file transfers\n"
                        "b) Securing communication with encryption\n"
                        "c) Managing network connections\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "4. How does HTTPS ensure secure communication?\n"
                        "a) by compressing data\n"
                        "b) by encrypting data\n"
                        "c) by increasing internet speed\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "5. What is the significance of the 'S' in HTTPS?\n"
                        "a) Secure\n"
                        "b) Speed\n"
                        "c) Standard\n"
                        "Your choice: ",
            "answer": "a"
        },
        {
            "question": "6. Which encryption protocol is commonly used in HTTPS?\n"
                        "a) DES\n"
                        "b) AES\n"
                        "c) RSA\n"
                        "Your choice: ",
            "answer": "c"
        },
        {
            "question": "7. What is the purpose of a digital certificate in HTTPS?\n"
                        "a) Compression of data\n"
                        "b) Authentication and encryption\n"
                        "c) Managing network traffic\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "8. In HTTP, what does the 'Referer' header indicate?\n"
                        "a) The server's location\n"
                        "b) The previous webpage\n"
                        "c) The client's IP address\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "9. What type of request does the HTTP method 'POST' represent?\n"
                        "a) Retrieve data\n"
                        "b) Send data to be processed\n"
                        "c) Delete data\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "10. What is the purpose of the 'Cache-Control' header in HTTP?\n"
                        "a) Controlling internet speed\n"
                        "b) Managing network connections\n"
                        "c) Specifying caching behavior\n"
                        "Your choice: ",
            "answer": "c"
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
