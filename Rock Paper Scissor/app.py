"""
WORKFLOW OF PROJECT
1 - Input from user (Rock, Paper, Scissor)
2 - Computer choice (Computer choose rendomly not conditionally)
3 - Result print

Cases:
A - Rock
Rock - Rock = Tie
Rock - Paper = Paper win
Rock - Scissor = Rock win

B - Paper
Paper - Paper = Tie
Paper - Scissor = Scissor win
Paper - Rock = Paper win

C - Scissor
Scissor - Scissor = Tie
Scissor - Paper = Scissor win
Scissor - Rock = Rock win

"""

import random
item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your move = Rock, Paper, Scissor = ")
comp_choice = random.choice(item_list)

print(f"User choice = {user_choice} , Computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both chooses same = Match Tie")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers Rock = Computer win")
    else:
        print("Rock smashes Scissor = You win")

elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts Paper = Computer win")
    else:
        print("Paper covers Rock = You win")

elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissorn cuts Paper = You win")
    else:
        print("Rock smashes Scissor = Computer win")