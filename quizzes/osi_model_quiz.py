# osi_model_quiz.py

def run_quiz():
    print("\n=== OSI Model Quiz ===")

    # Define quiz questions and answers
    questions = [
        {
            "question": "1. How many layers are there in the OSI model?\n"
                        "a) 4\n"
                        "b) 5\n"
                        "c) 7\n"
                        "Your choice: ",
            "answer": "c"
        },
        {
            "question": "2. Which layer is responsible for error detection and correction?\n"
                        "a) Data Link Layer\n"
                        "b) Transport Layer\n"
                        "c) Presentation Layer\n"
                        "Your choice: ",
            "answer": "a"
        },
        {
            "question": "3. What is the primary function of the Network Layer?\n"
                        "a) Physical addressing\n"
                        "b) Error checking\n"
                        "c) Routing and logical addressing\n"
                        "Your choice: ",
            "answer": "c"
        },
        {
            "question": "4. Which layer is responsible for establishing, maintaining, and terminating connections?\n"
                        "a) Session Layer\n"
                        "b) Transport Layer\n"
                        "c) Application Layer\n"
                        "Your choice: ",
            "answer": "a"
        },
        {
            "question": "5. What does the Presentation Layer do?\n"
                        "a) Data encryption and compression\n"
                        "b) Logical addressing\n"
                        "c) Flow control\n"
                        "Your choice: ",
            "answer": "a"
        },
        {
            "question": "6. Which layer is responsible for converting data into a format suitable for transmission?\n"
                        "a) Physical Layer\n"
                        "b) Data Link Layer\n"
                        "c) Presentation Layer\n"
                        "Your choice: ",
            "answer": "c"
        },
        {
            "question": "7. What does the Physical Layer deal with?\n"
                        "a) Logical addressing\n"
                        "b) Hardware specifications\n"
                        "c) Flow control\n"
                        "Your choice: ",
            "answer": "b"
        },
        {
            "question": "8. Which layer is closest to the end user in the OSI model?\n"
                        "a) Application Layer\n"
                        "b) Presentation Layer\n"
                        "c) Session Layer\n"
                        "Your choice: ",
            "answer": "a"
        },
        {
            "question": "9. What is the purpose of the Data Link Layer?\n"
                        "a) Error detection and correction\n"
                        "b) Logical addressing\n"
                        "c) Flow control\n"
                        "Your choice: ",
            "answer": "a"
        },
        {
            "question": "10. Which layer is responsible for addressing and routing?\n"
                        "a) Network Layer\n"
                        "b) Transport Layer\n"
                        "c) Data Link Layer\n"
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
