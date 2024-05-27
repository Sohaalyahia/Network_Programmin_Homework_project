import json
import csv
​
def load_questions(filename):
    with open(filename, 'r') as file:
        questions = json.load(file)
    return questions
​
def ask_questions(questions):
    correct_answers = 0
    for i, q in enumerate(questions):
        print(f"Q{i + 1}: {q['question']}")
        answer = input("Your answer: ")
        if answer.strip().lower() == q['answer'].strip().lower():
            correct_answers += 1
    return correct_answers
​
def save_results(username, score, total_questions, results_file):
    with open(results_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, score, total_questions])
​
def main():
    questions_file = 'questions.json'
    results_file = 'results.csv'
    
    username = input("Enter your name: ")
    questions = load_questions(questions_file)
    total_questions = len(questions)
    
    print("\nStarting the quiz...\n")
    score = ask_questions(questions)
    
    print(f"\nQuiz completed! {username}, you scored {score} out of {total_questions}.\n")
    
    save_results(username, score, total_questions, results_file)
    print("Your result has been saved.")
​
if __name__ == "__main__":
    main()