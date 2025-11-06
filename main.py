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


if __name__ == "__main__":
    run_quiz()
