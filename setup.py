import random
import mysql.connector

print("\033[1;36m Welcome to the Quest for Peaceful Kingdom!\n")
print("The peaceful kingdom was overcome by an evil wizard who spawned monsters everywhere.")
print("Only the bravest and smartest hero can overcome them and bring peace, which is you.")

player_name = input("Enter your hero's name: ")
player_health = 100
player_points = 0
level = 1

print(f"Welcome, {player_name}! To beat the game you need to reach Evil Wizard's lair and defeat him, "
      f"but beware it won't be easy ")
print("Correct answer gives you 1 point on level 1 and 2 points on level 2. "
      "Once you collect 10 points you will face the final boss ")

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

num_of_dice = 0

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="")
    print()

for die in dice:
    print(f"total: {die}")


def roll_dice():
    return random.randint(1, 6)

connection = mysql.connector.connect(
    host='localhost',
    port= 3306,
    user="touhid",
    password="MyN3wP4ssw0rd",
    database="trivia_game",
)

cursor = connection.cursor(dictionary=True)

def fetch_trivia_game(questions):
    if questions == 1:
        cursor.execute("SELECT * FROM questions")
    return cursor.fetchall()

monster_database_2 = [
    {
        "name": "Werewolf",
        "question": "Which planet is known as the Red-Planet?",
        "options": ["A: Venus", "B: Earth", "C: Mars", "D: Jupiter"],
        "answer": "C", "attack": random.randint(10, 20)
    },
    {
        "name": "Skeleton",
        "question": "Who wrote the play Romeo and Juliet?",
        "options": ["A: George Orwell", "B: George Orwell", "C: Jane Austen", "D: William Shakespeare"],
        "answer": "D", "attack": random.randint(10, 20)
    },
    {
        "name": "Spider",
        "question": "What is the capital city of Australia?",
        "options": ["A: Sydney", "B: Perth", "C: Canberra", "D: Melbourne"],
        "answer": "C", "attack": random.randint(10, 20)
    },
    {
        "name": "Bat",
        "question": "If y = 3x+7, what is the value of y when x = 2?",
        "options": ["A: 19", "B: 17", "C: 13", "D: 20"],
        "answer": "C", "attack": random.randint(10, 20)
    },
    {
        "name": "Dire Wolf",
        "question": "Solve for x in the equation 5x-3 = 12.",
        "options": ["A: 6", "B: 4", "C: 3", "D: 6"],
        "answer": "C", "attack": random.randint(10, 20)
    },
    {
        "name": "Vampire",
        "question": "If a triangle has angles measuring 90°, 45°, and 45°, what type of triangle is it?",
        "options": ["A: Isosceles Right Triangle", "B: Acute Triangle", "C: Scalene", "D: None of them"],
        "answer": "A", "attack": random.randint(10, 20)
    },
    {
        "name": "Griffin",
        "question": "Which planet is known as the Red-Planet?",
        "options": ["A: Venus", "B: Earth", "C: Mars", "D: Jupiter"],
        "answer": "C", "attack": random.randint(10, 20)
    },
    {
        "name": "Medusa",
        "question": "Who wrote the play Romeo and Juliet?",
        "options": ["A: George Orwell", "B: Jim Orwell", "C: Jane Austen", "D: William Shakespeare"],
        "answer": "D", "attack": random.randint(10, 20)
    },
    {
        "name": "Sphinx",
        "question": "What is the square root of 144?",
        "options": ["A: 10", "B: 11", "C: 12", "D: 14"],
        "answer": "C", "attack": random.randint(10, 20)
    },
    {
        "name": "Minotaur",
        "question": "Which gas is most abundant in Earth's atmosphere?",
        "options": ["A: Oxygen", "B:  Carbon dioxide", "C: Nitrogen", "D: Hydrogen"],
        "answer": "C", "attack": random.randint(10, 20)
    },
    {
        "name": "Cerberus",
        "question": "What is the longest river in the world?",
        "options": ["A: Amazon River", "B: Nile River", "C:  Mississippi River", "D: Yangtze River"],
        "answer": "B", "attack": random.randint(10, 20)
    },
    {
        "name": "Banshee",
        "question": "What does HTML stand for??",
        "options": ["A: Hyper Transfer Markup Language", "B: Hyper Text Markup Language", "C: High Tech Modern Language", "D: Hyperlink and Text Markup Language"],
        "answer": "B", "attack": random.randint(10, 20)
    },
]

level = 1

while player_health > 0:
    print(f"--- Level {level} ---")
    input("Press Enter to roll the dice...")

    dice_result = roll_dice()
    print("Dice Result:")
    for line in dice_art[dice_result]:
        print(line)

    monster_index = dice_result - 1
    if level == 1:
        current_monster = random.choice(fetch_trivia_game(level))
    else:
        current_monster = monster_database_2[monster_index]

    print(f"You encountered a {current_monster['name']}! ")
    answer = input(f"Question: {current_monster['question']}, {current_monster['options']}").strip().lower()

    if answer == current_monster['answer'].lower():
        print("Correct! You defeated the monster and gained 1 point.")
        player_points += 1
    else:
        print(f"Wrong answer! {current_monster['name']} attacks you for {current_monster['attack']} damage.")
        player_health -= current_monster['attack']

    print(f"Your Health: {player_health}")

    if player_points >= 5 and level == 1:
        level += 1
        print("Welcome to Level 2!")

    if player_points >= 12:
        print("Congratulations! You have reached the Evil Wizard's Lair'.")
        answer = input(
            "A boy and a doctor were fishing. The boy is the doctor's son, but the doctor isn't the boy's father. Who "
            "is the doctor? ").strip().lower()
        if answer in ["mother", "mom"]:
            print("You did it! The Evil Wizard is finally defeated, and you saved the kingdom!")
        else:
            print("You were our only hope. Do you want to try again?")
        break

if player_health <= 0:
    print("GAME OVER")

cursor.close()
connection.close()