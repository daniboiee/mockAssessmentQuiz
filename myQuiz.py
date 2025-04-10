import random

questionDictionary = {
    "Which gemstone is reffered to as the king of gemstones?" : "Ruby",
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
    i = 0
    score = 0
    while i < len(questionDictionary):
        questions = list(questionDictionary.keys())         # Puts questions into a list for ease of access
        print(questions[i])                                 # Outputs questions
        correct_answer = questionDictionary[questions[i]]   # Gets the correct answer
        options = get_random_answers(correct_answer)        # Compiles a list of possible incorrect answers
        print(options)
        user_answer = input("").lower()                     # Uses .lower() to remove issues with capitalisation
        if user_answer == correct_answer.lower():
            print("Correct.")
            score +=1
        else:
            print("Your answer was incorrect. The right answer was:", correct_answer)
        i+=1
    print("Your score was:", score)

quiz()
#& C:/Users/daniel.sarruf/AppData/Local/Programs/Python/Python312/python.exe c:/Users/daniel.sarruf/Desktop/school_code/mock_assessment_quiz/mockAssessmentQuiz/myQuiz.py