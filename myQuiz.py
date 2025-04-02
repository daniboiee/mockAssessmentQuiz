import random

questionDictionary = {
    "Which gemstone is reffered to as the king of gemstones?" : "Ruby",
    "What gemstone is formed from tree resin and is often found with insects trapped inside?" : "Amber",
    "Which gemstone is the hardest naturally occurring substance on Earth?" : "Diamond",
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
    incorrect_answers = random.sample([gem for gem in gemlist if gem != correct_answer, 3]) #Randomly picks 3 incorrect answers from the list without duplicates
    options.extend(incorrect_answers)   # Add incorrect answers to the options
    random.shuffle(options)             # Shuffle the options so the correct answer is always in different locations
    return options

while True:
