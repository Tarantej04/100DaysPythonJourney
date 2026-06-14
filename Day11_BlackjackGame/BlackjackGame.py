import random
from art import logo

def deal_card():
    # Function to get a random card for both user and computer
    cards = [11, 2, 3, 4, 5, 6, 7, 8 ,9 , 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    # Function to calculate the sum of cards with them.
    if sum(cards) == 21 and len(cards) == 2:  # Blackjack condition
        return 0
    if 11 in cards and sum(cards) > 21:       # Replace an ace card's value of 11 with 1 when score crosses 21
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare_scores(u_score, c_score):
    # Function to find the winner of the game
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "You lose.. Opponent has a blackjack.🤧"
    elif u_score == 0:
        return "You WIN with a Blackjack.😎"
    elif u_score > 21:
        return "You went over. You lose..😭"
    elif c_score > 21:
        return "Opponent went over. You WIN🥳🥳"
    elif u_score > c_score:
        return "You Win😁"
    else:
        return "You Lose🥲"

def blackjack_game():
    # Function to play the game
    print(logo)
    user_cards = []
    comp_cards = []
    user_score = -1
    comp_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        comp_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(comp_cards)
        print(f"Your cards: {user_cards}, Current score: {user_score}")
        print(f"Opponent's first card: {comp_cards[0]}")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            is_game_over = True

        else:
            while True:
                user_deal = input("Type 'y' to pick a card or 'n' to pass: ").lower()
                if user_deal in ['y', 'n']:
                    break
                else:
                    print("Enter valid input 'y' or 'n'.")
            if user_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while comp_score != 0 and comp_score < 17:   # If computer score is less than 17 and not a blackjack then deal cards
        comp_cards.append(deal_card())
        comp_score = calculate_score(comp_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Opponent's final hand: {comp_cards}, final score: {comp_score}")
    print(compare_scores(user_score, comp_score))

while True:
    play_game = input("Do you want to play a game of Blackjack? Enter 'y' to play, 'n' to exit: ").lower()

    if play_game == 'y':
        print("\n" * 20)
        blackjack_game()
    elif play_game == 'n':
        break
    else:
        print("Invalid input. Please enter either 'y' or 'n'.")
