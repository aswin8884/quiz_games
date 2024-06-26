import tkinter as tk
from tkinter import messagebox
from quiz_questions import questions_data

class Question:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

class QuizGame(tk.Tk):
    def __init__(self, questions):
        super().__init__()

        self.title("Quiz Game")
        self.geometry("600x550")

        self.questions = [Question(q, opts, ans) for q, opts, ans in questions]
        self.score = 0
        self.current_question = 0

        self.configure_gui()
        self.create_widgets()
        self.display_question()

    def configure_gui(self):
        self.configure(bg="#95D2B3")

    def create_widgets(self):
        self.question_label = tk.Label(self, text="", wraplength=480, justify="center", font=("Arial", 16,"bold"),
                                       bg="#95D2B3", fg="#219C90")
        self.question_label.pack(pady=20)

        self.option_var = tk.IntVar()

        self.option_buttons = []
        for i in range(4):
            btn_frame = tk.Frame(self, bg="#95D2B3")
            btn_frame.pack(anchor="w", padx=20, pady=5)

            option_value = i + 1
            btn = tk.Radiobutton(btn_frame, text="", variable=self.option_var, value=option_value, font=("Arial", 20,"bold"),
                                 bg="#95D2B3", fg="#102C57")
            btn.pack(side=tk.LEFT)

            label = tk.Label(btn_frame, text="", font=("Arial", 14,"bold"), bg="#95D2B3", fg="#219C90")
            label.pack(side=tk.LEFT, padx=10)

            self.option_buttons.append((btn, label))

        self.submit_button = tk.Button(self, text="Submit", command=self.submit_answer, font=("Arial", 14),
                                       bg="#219C90", fg="white",border="0")
        self.submit_button.pack(pady=10)

        self.score_label = tk.Label(self, text="Score: 0", font=("Arial", 24), bg="#95D2B3", fg="white")
        self.score_label.pack(pady=10)


    def display_question(self):
        question = self.questions[self.current_question]
        self.question_label.config(text=question.question)

        for i, (option, (btn, label)) in enumerate(zip(question.options, self.option_buttons)):
            label.config(text=option)
            btn.config(text="")

        self.option_var.set(0)

    def submit_answer(self):
        selected_option = self.option_var.get()

        if selected_option == 0:
            messagebox.showwarning("Warning", "Please select an option!")
            return

        correct_answer = self.questions[self.current_question].correct_answer

        if selected_option == correct_answer:
            self.score += 4
            messagebox.showinfo("Result", "Correct answer!")
        else:
            self.score -= 1
            correct_option_text = self.questions[self.current_question].options[correct_answer - 1]
            messagebox.showinfo("Result", f"Incorrect!\nCorrect answer: {correct_option_text}")

        self.score_label.config(text=f"Score: {self.score}")

        if self.current_question < len(self.questions) - 1:
            self.current_question += 1
            self.display_question()
        else:
            self.end_game()

    def end_game(self):
        if self.score >= 25:
            messagebox.showinfo("Congratulations!", f"Final score: {self.score}\nYou won the match!")
        else:
            messagebox.showinfo("Game Over", f"Final score: {self.score}\nYou lost the match.\nBetter luck next time")

        self.quit()



if __name__ == "__main__":
    quiz_app = QuizGame(questions_data)
    quiz_app.mainloop()
