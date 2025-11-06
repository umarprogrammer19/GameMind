import time

QUESTIONS = [
    {
        "question": "What does 'CPU' stand for?",
        "options": [
            "Central Process Unit",
            "Central Processing Unit",
            "Computer Personal Unit",
            "Central Processor Utility",
        ],
        "answer": 2,
    },
    {
        "question": "Which language is known as the language of the web?",
        "options": ["Python", "C++", "JavaScript", "Java"],
        "answer": 3,
    },
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Lisbon"],
        "answer": 3,
    },
    {
        "question": "Which data type is immutable in Python?",
        "options": ["List", "Dictionary", "Tuple", "Set"],
        "answer": 3,
    },
    {
        "question": "What symbol is used to comment in Python?",
        "options": ["//", "#", "/* */", "--"],
        "answer": 2,
    },
]


def run_quiz():
    score = 0

    print("🎯 Welcome to the CLI Quiz!")
    name = input("Enter your name: ")

    print(f"Hello {name}! Let's start...\n")
    time.sleep(1)

    for i, q in enumerate(QUESTIONS, start=1):
        print(f"Q{i}: {q['question']}")

        for idx, opt in enumerate(q["options"], start=1):
            try:
                choice = int(input("Your answer (1-4): "))
            except ValueError:
                choice = 0

            if choice == q["answer"]:
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! Correct answer: {q['options'][q['answer'] - 1]}\n")
                time.sleep(0.5)

    print("🎉 Quiz Complete!")
    print(f"Your score: {score}/{len(QUESTIONS)}")

    if score == 5:
        print("🏆 Perfect score! Great job!")
    elif score >= 3:
        print("👏 Good effort!")
    else:
        print("💪 Keep practicing!")


if __name__ == "__main__":
    run_quiz()
