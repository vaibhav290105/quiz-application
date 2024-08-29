import tkinter as tk
from tkinter import messagebox

# Sample data: A list of dictionaries where each dictionary represents a question
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which programming language is known as the backbone of web development?",
        "options": ["Python", "JavaScript", "Java", "C++"],
        "answer": "JavaScript"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["Harper Lee", "Mark Twain", "J.K. Rowling", "George Orwell"],
        "answer": "Harper Lee"
    },
    {
        "question": "What is the smallest prime number?",
        "options": ["0", "1", "2", "3"],
        "answer": "2"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "Mars"
    }
]

# Initialize the main window
root = tk.Tk()
root.title("Quiz Application")

# Variables to keep track of quiz state
current_question_index = 0
score = 0
selected_option = tk.StringVar()

# Function to load the next question
def load_question():
    global current_question_index
    question_data = quiz_data[current_question_index]
    
    question_label.config(text=question_data["question"])
    selected_option.set(None)  # Deselect any previously selected option
    
    for i, option in enumerate(question_data["options"]):
        option_buttons[i].config(text=option, value=option)

# Function to check the answer and provide feedback
def check_answer():
    global current_question_index, score
    
    selected = selected_option.get()
    correct_answer = quiz_data[current_question_index]["answer"]
    
    if selected == correct_answer:
        score += 1
        messagebox.showinfo("Correct!", "You selected the right answer!")
    else:
        messagebox.showinfo("Incorrect", f"The correct answer was: {correct_answer}")
    
    current_question_index += 1
    
    if current_question_index < len(quiz_data):
        load_question()
    else:
        show_final_score()

# Function to show the final score
def show_final_score():
    messagebox.showinfo("Quiz Finished", f"Your final score is: {score}/{len(quiz_data)}")
    root.destroy()

# GUI Layout
question_label = tk.Label(root, text="", font=('Arial', 16), wraplength=400)
question_label.pack(pady=20)

option_buttons = []
for i in range(4):
    btn = tk.Radiobutton(root, text="", font=('Arial', 14), variable=selected_option, value="", indicatoron=0, width=15)
    btn.pack(pady=5)
    option_buttons.append(btn)

next_button = tk.Button(root, text="Next", font=('Arial', 14), command=check_answer)
next_button.pack(pady=20)

# Load the first question
load_question()

# Start the main loop
root.mainloop()
