from memory_game import play as memory_game_play
from guess_game import play as guess_game_play
from currency_roulette_game import play as currency_roulette_play
from score import add_score


def welcome():
    username = input("Please enter your name: ")
    print(f'Hi {username} and welcome to the World of Games: The Epic Journey!')


def validate_user_input(user_choice, valid_inputs: range) -> bool:
    if user_choice.isdigit() and int(user_choice) in valid_inputs:
        return True
    print(f'Please select a valid input using numbers {valid_inputs[0]}-{valid_inputs[-1]}')
    return False


def prompt_game_choice() -> int:
    while True:
        user_game_choice = input("""
        Please choose a game to play:
        1. Memory Game - a sequence of numbers will appear for 1 second, and you have to guess it back.
        2. Guess Game - guess a number and see if you chose like the computer.
        3. Currency Roulette - try and guess the value of a random amount of USD in ILS 
        (to exit enter 'q')
        """)
        if user_game_choice == 'q':
            print("Exiting the game. Goodbye!")
            return -1  # Return a special value to indicate exit
        if validate_user_input(user_game_choice, range(1, 4)):
            return int(user_game_choice)


def prompt_difficulty_choice() -> int:
    while True:
        user_difficulty_choice = input("Please choose your game difficulty 1-5 (to exit enter 'q'): ")
        if user_difficulty_choice == 'q':
            print("Exiting the game. Goodbye!")
            return -1
        if validate_user_input(user_difficulty_choice, range(1, 6)):
            return int(user_difficulty_choice)


def start_play():
    game_choice = prompt_game_choice()
    if game_choice == -1:
        return
    difficulty_choice = prompt_difficulty_choice()
    if difficulty_choice == -1:
        return

    game_functions = {
        1: memory_game_play,
        2: guess_game_play,
        3: currency_roulette_play
    }
    selected_game = game_functions.get(game_choice)
    if selected_game:
        print(f"You have chosen game {game_choice} with difficulty level {difficulty_choice}.")
        has_won = selected_game(difficulty_choice)
        if has_won:
            print('You win!')
            add_score(difficulty_choice)
        else:
            print('You lose!')
    else:
        print("Error: Invalid game choice.")
