def welcome():
    username = input("Please enter your name: ")
    print(f'Hi {username} and welcome to the World of Games: The Epic Journey!')


def validate_user_input(user_choice: int, valid_inputs: range) -> bool:
    if user_choice not in valid_inputs:
        print(f'Please select a valid input using numbers {valid_inputs[0]}-{valid_inputs[-1]}')
        return False
    return True


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

        if validate_user_input(int(user_game_choice), range(1, 4)):
            return int(user_game_choice)


def prompt_difficulty_choice() -> int:
    while True:
        user_difficulty_choice = input("Please choose your game difficulty 1-5 (to exit enter 'q'): ")
        if user_difficulty_choice == 'q':
            print("Exiting the game. Goodbye!")
            return -1
        if validate_user_input(int(user_difficulty_choice), range(1, 6)):
            return int(user_difficulty_choice)


def start_play():
    game_choice = prompt_game_choice()
    if game_choice == -1:
        return
    difficulty_choice = prompt_difficulty_choice()
    if difficulty_choice == -1:
        return
    print(f"You have chosen game {game_choice} with difficulty level {difficulty_choice}.")
