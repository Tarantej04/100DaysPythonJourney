import random
import time

def winner(user, comp):
    if user-1 == comp:
        return "tie"
    elif (user-1 == 0 and comp == 2) or (user-1 == 1 and comp == 0) or (user-1 == 2 and comp == 1):
        return "user"
    else:
        return "computer"

def game():
    rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

    paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

    scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

    game_images = [rock, paper, scissors]

    print("\nWelcome to the ultimate game of Rock Paper Scissors🥳✨")
    print('''
    Rules are pretty simple:
        1. Rock beats Scissors
        2. Paper beats Rock
        3. Scissors beats Paper
    ''')
    print("Now you will have a showdown with the computer and whoever scores 3 points first wins...")
    user_wins = 0
    comp_wins = 0
    round_no = 1
    while user_wins <= 2 and comp_wins <= 2 :
        print(f"---Round {round_no}---")
        user = int(input("Make a choice: Choose 1 for Rock🪨 , 2 for Paper📃 , and 3 for Scissors✂️\n"))
        if 1 <= user <= 3:
            print("Your choice:")
            print(game_images[user - 1])
            comp = random.randint(0,2)
            print("Computer's choice:")
            time.sleep(0.5)
            print(game_images[comp])
            result = winner(user, comp)
            if result == "tie":
                print("It's a tie!!\n")
            elif result == "user":
                user_wins += 1
                print("User wins!!\n")
            else:
                comp_wins += 1
                print("Computer wins!!\n")
            print(f"Player Score : {user_wins} || Computer Score : {comp_wins}\n")
            round_no += 1
        else:
            print("Invalid input.. Try again😭")
            continue
    if user_wins > comp_wins:
        print("YOU WIN !! 🥳🥳🥳")
    else:
        print("The computer wins!! 😭👌")
game()