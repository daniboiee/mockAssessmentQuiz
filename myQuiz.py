import tkinter as tk
from tkinter import messagebox
import random

# Dictionary containing questions and their corresponding correct answers
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

# List of possible answers
gemlist = ["Ruby", "Amber", "Diamond", "Blue Diamond", "Amethyst", "Phosphophyllite", "Kyawthuite", "Ammolite", "Lapis Lazuli", "Alexandrite", "Tanzanite", "Quartz", "Emerald", "Cummingtonite", "Painite", "Bortz", "Aquamarine", "Cinnabar", "Rutile", "Padparadscha", "Opal", "Lonsdaleite", "Carmeltazite", "Jade", "Euclase", "Yellow Diamond", "Pink Diamond", "Red Diamond", "Green Diamond", "Brown Diamond", "Black Diamond", "Zircon", "Antarcticite", "Cairngorm", "Red Beryl", "Benitoite", "Neptunite", "Obsidian", "Watermelon Tourmaline", "Peridot", "Sphene", "Heliodor", "Sapphire", "Zoisite", "Topaz", "Chrysoberyl", "Citrine", "Danburite", "Coral", "Cobaltite", "Celestite", "Bytownite", "Brazilianite", "Apatite", "Apophyllite", "Agate", "Garnet", "Hambergite", "Holtite", "Howlite", "Hyperitdiabas", "Rose Quartz", "Parisite", "Paraíba Tourmaline", "Onyx", "Legrandite", "Laserblue", "Labradorite", "Iolite", "Scheelite", "Simpsonite", "Sodalite", "Sunstone", "Talc", "Whewellite", "Yugawaralite", "Witherite"]

# Function to generate a list of random answer choices, including the correct one
def get_random_answers(correct_answer):
    # Generate random options and shuffle them
    options = [correct_answer] + random.sample([gem for gem in gemlist if gem != correct_answer], 5)
    random.shuffle(options)
    return options

class QuizApp:
    def __init__(self, root):
        # Initialize the app with the root window and quiz state
        self.root = root
        self.root.title("Gemstone Quiz")  # Set the window title
        self.score = 0  # Initialize score
        self.question_index = 0  # Keep track of the current question index
        self.name = ""  # Placeholder for user's name
        self.questions = list(questionDictionary.items())  # List of questions from the dictionary
        random.shuffle(self.questions)  # Shuffle questions for randomness

        # Create and pack the name input components
        self.label = tk.Label(root, text="Please enter your name:")
        self.label.pack(pady=10)
        self.name_entry = tk.Entry(root)
        self.name_entry.pack(pady=5)
        self.submit_name_button = tk.Button(root, text="Submit", command=self.set_name)
        self.submit_name_button.pack(pady=10)

    def set_name(self):
        # Get the name input by the user and validate it
        self.name = self.name_entry.get().strip()
        if not self.name or not all(char.isalpha() or char.isspace() for char in self.name):
            messagebox.showerror("Invalid Name", "Invalid name. Use letters and spaces only.")
            return
        # Hide name input and show the first question
        self.name_entry.pack_forget()
        self.submit_name_button.pack_forget()
        self.label.pack_forget()
        self.display_question()

    def display_question(self):
        # Display a new question if there are still questions left
        if self.question_index < len(self.questions):
            question, correct_answer = self.questions[self.question_index]
            options = get_random_answers(correct_answer)  # Get random answers

            # Remove previous question and options before displaying new ones
            if hasattr(self, 'question_label'):
                self.question_label.pack_forget()
            if hasattr(self, 'option_buttons'):
                for btn in self.option_buttons:
                    btn.pack_forget()

            # Display the new question and options
            self.question_label = tk.Label(self.root, text=f"Question {self.question_index + 1}: {question}")
            self.question_label.pack(pady=10)

            # Create buttons for the answer choices
            self.option_buttons = []
            for option in options:
                btn = tk.Button(self.root, text=option, command=lambda option=option: self.check_answer(option, correct_answer))
                btn.pack(fill=tk.X, padx=20, pady=2)  # Fill horizontally with padding
                self.option_buttons.append(btn)
        else:
            # If all questions are answered, display the final score
            self.display_score()

    def check_answer(self, selected_answer, correct_answer):
        # Check if the selected answer is correct and update the score
        self.score += (selected_answer == correct_answer)
        messagebox.showinfo("Result", f"{'Correct!' if selected_answer == correct_answer else f'Incorrect. The correct answer was {correct_answer}.'}")
        self.question_index += 1  # Move to the next question
        self.display_question()  # Display the next question

    def display_score(self):
        # Display the final score when the quiz is over
        messagebox.showinfo("Quiz Over", f"{self.name}, you got {self.score} out of {len(questionDictionary)} correct!")
        # Ask if the user wants to save their score
        if messagebox.askyesno("Save Score", "Do you want to save your score?"):
            with open("scores.txt", "a") as file:
                file.write(f"{self.name}: {self.score} out of {len(questionDictionary)}\n")
            messagebox.showinfo("Score Saved", "Your score has been saved!")

        self.root.quit()  # Quit the application after the quiz is over

def main():
    # Initialize the Tkinter root window and run the quiz app
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()

#& C:/Users/daniel.sarruf/AppData/Local/Programs/Python/Python312/python.exe c:/Users/daniel.sarruf/Desktop/school_code/mock_assessment_quiz/mockAssessmentQuiz/myQuiz.py