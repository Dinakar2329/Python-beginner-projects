import random


while True:
    user = input("What's your choice? Type 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        print(f"Both players selected {user}. It's a tie!")

    elif (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        print(f"You chose {user} and Oppenent chose {computer}. You Won!😍")

    else:
        print(f"You choce {user} and Oppenent chose {computer}. You Lost!😭")

    play_again = input("Do you want to play again  (yes/no):\n")

    if play_again == "yes":
        continue
    else:
        break

