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

def quiz():
    score = 0
    questions = list(questionDictionary.items())
    random.shuffle(questions)

    for i, (question, correct_answer) in enumerate(questions, 1):
        print(f"\nQuestion {i}: {question}")
        options = get_random_answers(correct_answer)

        for idx, option in enumerate(options, 1):
            print(f"  {idx}. {option}")
        
        while True:
            try:
                user_choice = int(input("Your answer (1-6): "))
                if 1 <= user_choice <= 6:
                    break
                else:
                    print("Please choose a number between 1 and 6.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        selected_answer = options[user_choice - 1]
        if selected_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer was: {correct_answer}")

    print(f"\nYou got {score} out of {len(questionDictionary)} correct!")

quiz()
#& C:/Users/daniel.sarruf/AppData/Local/Programs/Python/Python312/python.exe c:/Users/daniel.sarruf/Desktop/school_code/mock_assessment_quiz/mockAssessmentQuiz/myQuiz.py