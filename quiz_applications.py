import os

# File paths
QUESTIONS_FILE = "questions.txt"
SCORES_FILE = "scores.txt"

def load_questions():
    """Load questions from the file."""
    questions = []
    if os.path.exists(QUESTIONS_FILE):
        with open(QUESTIONS_FILE, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 6:
                    questions.append({
                        "question": parts[0],
                        "options": parts[1:5],
                        "answer": parts[5]
                    })
    return questions

def ask_questions(questions):
    """Ask questions to the user and calculate the score."""
    score = 0
    for idx, q in enumerate(questions):
        print(f"Question {idx + 1}: {q['question']}")
        print(f"A. {q['options'][0]}  B. {q['options'][1]}  C. {q['options'][2]}  D. {q['options'][3]}")
        user_answer = input("Your Answer (A/B/C/D): ").strip().upper()
        
        if user_answer == q['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.\n")
    return score

def save_score(name, score, total):
    """Save the user's score to the scores file."""
    if not os.path.exists(SCORES_FILE):
        with open(SCORES_FILE, 'w') as file:
            file.write("User Name, Score\n")
    
    with open(SCORES_FILE, 'a') as file:
        file.write(f"{name},{score}/{total}\n")

def main():
    print("Welcome to the Quiz Application!")
    print("Rules:\n- Each question has 4 options.\n- Enter the option (A, B, C, D) as your answer.")
    input("Press Enter to start the quiz!\n")
    
    questions = load_questions()
    if not questions:
        print("No questions found! Please add questions to 'questions.txt'.")
        return
    
    name = input("Enter your name: ").strip()
    score = ask_questions(questions)
    total = len(questions)
    
    print(f"Quiz Complete! Your Score: {score}/{total}")
    save_score(name, score, total)
    print(f"Your score has been saved to '{SCORES_FILE}'.")

if __name__ == "__main__":
    main()

