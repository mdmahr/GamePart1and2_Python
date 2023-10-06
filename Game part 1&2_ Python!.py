import random

print("Assesment = Correct answers (Per question = 1p) + Total point of dice. To unlock the level 2, you have to get at least 7p")

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

dice = []
total = 0
#num_of_dice = int(input("How many dice?: "))
num_of_dice = 1

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

# PRINT VERTICALLY
#for die in range(num_of_dice):
    #for line in dice_art.get(dice[die]):
       #print(line)

# PRINT HORIZONTALLY
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="")
    print()

for die in dice:
    print(f"total: {die}")



questions = ("How many elements are in the periodic table?: ",
            "Which animal lays the largest eggs?: ",
            "What does Newton's first law of motion cover?: ",
            "How many bones are in the human body?: ",
            "What is the value of square root 25?: ",
            "Which planet in the solar system is the hottest?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Gravity", "B. Energy", "C. Inertia", "D. Density"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. 5", "B. 6", "C. 2", "D. 3"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "C", "A", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer.")
    question_num += 1

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score + die)

if score >= 12:
    print("Your score is: 100%")
else:
    print(f"Your score is: {score}")

if score >= 7 or score >= 12:
    print("Congratulations! You've unlocked level 2")
    import random

    print(
        "Assesment = Correct answers (Per question = 1p), Total point of dice. To pass the quiz, either you have to get at from dice 6p or from quiz 6p")

    dice_art = {
        1: ("┌─────────┐",
            "│         │",
            "│    ●    │",
            "│         │",
            "└─────────┘"),
        2: ("┌─────────┐",
            "│  ●      │",
            "│         │",
            "│      ●  │",
            "└─────────┘"),
        3: ("┌─────────┐",
            "│  ●      │",
            "│    ●    │",
            "│      ●  │",
            "└─────────┘"),
        4: ("┌─────────┐",
            "│  ●   ●  │",
            "│         │",
            "│  ●   ●  │",
            "└─────────┘"),
        5: ("┌─────────┐",
            "│  ●   ●  │",
            "│    ●    │",
            "│  ●   ●  │",
            "└─────────┘"),
        6: ("┌─────────┐",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "└─────────┘")
    }

    dice = []
    total = 0
    # num_of_dice = int(input("How many dice?: "))
    num_of_dice = 1

    for die in range(num_of_dice):
        dice.append(random.randint(1, 6))

    # PRINT VERTICALLY
    # for die in range(num_of_dice):
    # for line in dice_art.get(dice[die]):
    # print(line)

    # PRINT HORIZONTALLY
    for line in range(5):
        for die in dice:
            print(dice_art.get(die)[line], end="")
        print()

    for die in dice:
        print(f"total: {die}")

    questions = ("Which planet is known as the Red-Planet?: ",
                 "Who wrote the play Romeo and Juliet?: ",
                 "What is the capital city of Australia?: ",
                 "If y = 3x+7, what is the value of y when x = 2?: ",
                 "Solve for x in the equation 5x-3 = 12.",
                 "If a triangle has angles measuring 90°, 45°, and 45°, what type of triangle is it?: ")

    options = (("A. Venus", "B. Earth", "C. Mars", "D. Jupiter"),
               ("A. George Orwell", "B. George Orwell", "C. Jane Austen", "D. William Shakespeare"),
               ("A. Sydney", "B. Perth", "C. Canberra", "D. Melbourne"),
               ("A. 19", "B. 17", "C. 13", "D. 20"),
               ("A. 6", "B. 4", "C. 3", "D. 6"),
               ("A. Isosceles Right Triangle", "B. Acute Triangle", "C. Scalene", "D. None of them"))

    answers = ("C", "D", "C", "C", "C", "A")
    guesses = []
    score = 0
    question_num = 0

    for question in questions:
        print("----------------------")
        print(question)
        for option in options[question_num]:
            print(option)

        guess = input("Enter (A, B, C, D): ").upper()
        guesses.append(guess)
        if guess == answers[question_num]:
            score += 1
            print("CORRECT!")
        else:
            print("INCORRECT!")
            print(f"{answers[question_num]} is the correct answer.")
        question_num += 1

    print("----------------------")
    print("       RESULTS        ")
    print("----------------------")

    print("answers: ", end="")
    for answer in answers:
        print(answer, end=" ")
    print()

    print("guesses: ", end="")
    for guess in guesses:
        print(guess, end=" ")
    print()

    score = int(score)

    if die == 6:
        print("Congratulations! You won.")
    elif score >= 6:
        print("Congratulations! You won.")
        print("")
    else:
        print("Failed")

print("Thank you!")