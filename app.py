
def welcome(username):
    print(f'Hi {username} and welcome to the World of Games: The Epic Journey!')


def start_play():

    def _validate_user_input(user_choice: str, valid_inputs: []) -> bool:
        if user_choice not in valid_inputs:
            print(f'Please select a valid input using numbers {valid_inputs[0]}-{valid_inputs[-1]}')
            return False
        return True

    def _prompt_game_choice() -> str:
        user_game_choice = input("""
        Please choose a game to play:
        1. Memory Game - a sequence of numbers will appear for 1 second, and you have to guess it back.
        2. Guess Game - guess a number and see if you chose like the computer.
        3. Currency Roulette - try and guess the value of a random amount of USD in ILS 
        (to exit enter 'q')
        """)
        if user_game_choice == 'q':
            exit(0)

        is_game_input_valid = _validate_user_input(user_game_choice, ['1', '2', '3'])
        if is_game_input_valid:
            return user_game_choice
        else:
            _prompt_game_choice()

    def _prompt_difficulty_choice() -> str:
        user_difficulty_choice = input("Please choose your game difficulty 1-5 (to exit enter 'q'): ")
        if user_difficulty_choice == 'q':
            exit(0)

        is_difficulty_input_valid = _validate_user_input(user_difficulty_choice, ['1', '2', '3', '4', '5'])
        if is_difficulty_input_valid:
            return user_difficulty_choice
        else:
            _prompt_difficulty_choice()

    game_choice = _prompt_game_choice()
    difficulty_choice = _prompt_difficulty_choice()



