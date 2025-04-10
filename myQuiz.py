import tkinter as tk
from tkinter import messagebox
import random

questionDictionary = {
    "Which gemstone is referred to as the king of gemstones?": "Ruby",
    "What gemstone is formed from tree resin and is often found with insects trapped inside?": "Amber",
    "Which gemstone is the softest naturally occurring substance on Earth?": "Talc",
    "What is the most expensive gemstone per carat?": "Blue Diamond",
    "Which gemstone did the ancient greeks believe protected against intoxication?": "Amethyst",
    "Who is the main character of the series Land of the Lustrous?": "Phosphophyllite",
    "What is the rarest gemstone, with only 1 documented sample ever found?": "Kyawthuite",
    "Which gemstone was first discovered in Canada?": "Ammolite",
    "Which gemstone was historically used as a pigment in Renaissance paintings?": "Lapis Lazuli",
    "Which gemstone changes color depending on lighting, appearing green in daylight and red in incandescent light?": "Alexandrite"
}

gemlist = ["Ruby", "Amber", "Diamond", "Blue Diamond", "Amethyst", "Phosphophyllite", "Kyawthuite", "Ammolite", "Lapis Lazuli", "Alexandrite"]

def get_random_answers(correct_answer):
    options = [correct_answer] + random.sample([gem for gem in gemlist if gem != correct_answer], 5)
    random.shuffle(options)
    return options

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gemstone Quiz")
        self.score = 0
        self.question_index = 0
        self.name = ""
        self.questions = list(questionDictionary.items())
        random.shuffle(self.questions)

        self.label = tk.Label(root, text="Please enter your name:")
        self.label.pack(pady=10)
        self.name_entry = tk.Entry(root)
        self.name_entry.pack(pady=5)
        self.submit_name_button = tk.Button(root, text="Submit", command=self.set_name)
        self.submit_name_button.pack(pady=10)

    def set_name(self):
        self.name = self.name_entry.get().strip()
        if not self.name or not all(char.isalpha() or char.isspace() for char in self.name):
            messagebox.showerror("Invalid Name", "Invalid name. Use letters and spaces only.")
            return
        self.name_entry.pack_forget()
        self.submit_name_button.pack_forget()
        self.label.pack_forget()
        self.display_question()

    def display_question(self):
        if self.question_index < len(self.questions):
            question, correct_answer = self.questions[self.question_index]
            options = get_random_answers(correct_answer)

            # Remove previous question and options before displaying new ones
            if hasattr(self, 'question_label'):
                self.question_label.pack_forget()
            if hasattr(self, 'option_buttons'):
                for btn in self.option_buttons:
                    btn.pack_forget()

            self.question_label = tk.Label(self.root, text=f"Question {self.question_index + 1}: {question}")
            self.question_label.pack(pady=10)

            self.option_buttons = []
            for option in options:
                btn = tk.Button(self.root, text=option, command=lambda option=option: self.check_answer(option, correct_answer))
                btn.pack(fill=tk.X, padx=20, pady=2)
                self.option_buttons.append(btn)
        else:
            self.display_score()

    def check_answer(self, selected_answer, correct_answer):
        self.score += (selected_answer == correct_answer)
        messagebox.showinfo("Result", f"{'Correct!' if selected_answer == correct_answer else f'Incorrect. The correct answer was {correct_answer}.'}")
        self.question_index += 1
        self.display_question()

    def display_score(self):
        messagebox.showinfo("Quiz Over", f"{self.name}, you got {self.score} out of {len(questionDictionary)} correct!")
        if messagebox.askyesno("Save Score", "Do you want to save your score?"):
            with open("scores.txt", "a") as file:
                file.write(f"{self.name}: {self.score} out of {len(questionDictionary)}\n")
            messagebox.showinfo("Score Saved", "Your score has been saved!")

        self.root.quit()

def main():
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

#& C:/Users/daniel.sarruf/AppData/Local/Programs/Python/Python312/python.exe c:/Users/daniel.sarruf/Desktop/school_code/mock_assessment_quiz/mockAssessmentQuiz/myQuiz.py