import random

questionDictionary = {
    "Which gemstone is referred to as the king of gemstones?" : "Ruby",
    "What gemstone is formed from tree resin and is often found with insects trapped inside?" : "Amber",
    "Which gemstone is the softest naturally occurring substance on Earth?" : "Talc",
    "What is the most expensive gemstone per carat?" : "Blue Diamond",
    "Which gemstone did the ancient greeks believe protected against intoxication?" : "Amethyst",
    "Who is the main character of the series Land of the Lustrous?" : "Phosphophyllite",
    "What is the rarest gemstone, with only 1 documented sample ever found?" : "Kyawthuite",
    "Which gemstone was first discovered in Canada?" : "Ammolite",
    "Which gemstone was historically used as a pigment in Renaissance paintings?" : "Lapis Lazuli",
    "Which gemstone changes color depending on lighting, appearing green in daylight and red in incandescent light?" : "Alexandrite"
}

gemlist = ["Ruby", "Amber", "Diamond", "Blue Diamond", "Amethyst", "Phosphophyllite", "Kyawthuite", "Ammolite", "Lapis Lazuli", "Alexandrite", "Tanzanite", "Quartz", "Emerald", "Cummingtonite", "Painite", "Bortz", "Aquamarine", "Cinnabar", "Rutile", "Padparadscha", "Opal", "Lonsdaleite", "Carmeltazite", "Jade", "Euclase", "Yellow Diamond", "Pink Diamond", "Red Diamond", "Green Diamond", "Brown Diamond", "Black Diamond", "Zircon", "Antarcticite", "Cairngorm", "Red Beryl", "Benitoite", "Neptunite", "Obsidian", "Watermelon Tourmaline", "Peridot", "Sphene", "Heliodor", "Sapphire", "Zoisite", "Topaz", "Chrysoberyl", "Citrine", "Danburite", "Coral", "Cobaltite", "Celestite", "Bytownite", "Brazilianite", "Apatite", "Apophyllite", "Agate", "Garnet", "Hambergite", "Holtite", "Howlite", "Hyperitdiabas", "Rose Quartz", "Parisite", "Paraíba Tourmaline", "Onyx", "Legrandite", "Laserblue", "Labradorite", "Iolite", "Scheelite", "Simpsonite", "Sodalite", "Sunstone", "Talc", "Whewellite", "Yugawaralite", "Witherite"]


def get_random_answers(correct_answer):
    options = [correct_answer]          # Ensure the correct answer is in the list of options
    incorrect_answers = random.sample([gem for gem in gemlist if gem != correct_answer], 5) #Randomly picks 5 incorrect answers from the list without duplicates
    options.extend(incorrect_answers)   # Add incorrect answers to the options
    random.shuffle(options)             # Shuffle the options so the correct answer is always in different locations
    return options

def get_name():     # Simple function to get user's name
    name = input("Please enter your name: ").strip()
    if not name:    # If the name is empty, repeats the function
        print("Name cannot be empty. Please try again.")
        return get_name()

    if all(char.isalpha() or char.isspace() for char in name):  # Makes sure all the characters are either letters or spaces
        return name
    else:   # If not all characters fall under these conditions, repeats the function
        print("Invalid input. Please use letters and spaces only (no numbers or symbols).")
        return get_name()

def save_score(name, score):
    save_option = input("Do you want to save your score? (yes/no): ").strip().lower()
    if save_option == 'yes':
        with open("scores.txt", "a") as file:
            file.write(f"{name}: {score} out of {len(questionDictionary)}\n")
        print(f"Your score has been saved, {name}!")

def quiz():
    score = 0   # Set user's initial score to 0
    questions = list(questionDictionary.items())    # Convert the dictionary into a list of (question, answer) pairs
    random.shuffle(questions)   # Shuffle question order

    name = get_name()   # Gets the user's name

    # Loop through each question and its correct answer
    for i, (question, correct_answer) in enumerate(questions, 1):
        print(f"\nQuestion {i}: {question}")
        options = get_random_answers(correct_answer)    # Get a randomized list of possible answers (including the correct one)

        # Display answer options
        for idx, option in enumerate(options, 1):
            print(f"  {idx}. {option}")
        
        # Get user input with validation to ensure it's a number between 1 and 6
        while True:
            try:
                user_choice = int(input("Your answer (1-6): "))
                if 1 <= user_choice <= 6:
                    break   # Valid input, exit loop
                else:
                    print("Please choose a number between 1 and 6.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        # Check if the selected answer is correct
        selected_answer = options[user_choice - 1]  # Convert from 1-based to 0-based index
        if selected_answer == correct_answer:
            print("Correct!")
            score += 1  # Increase score when answer is correct
        else:
            print(f"Incorrect. The correct answer was: {correct_answer}")

    # Prints the final score after all questions are answered, and congratulates user on a perfect clear
    print(f"\n{name}, you got {score} out of {len(questionDictionary)} correct!")
    if score == len(questionDictionary):
        print("You answered every question correctly! Well done.")

    save_score(name, score)

quiz()
#& C:/Users/daniel.sarruf/AppData/Local/Programs/Python/Python312/python.exe c:/Users/daniel.sarruf/Desktop/school_code/mock_assessment_quiz/mockAssessmentQuiz/myQuiz.py