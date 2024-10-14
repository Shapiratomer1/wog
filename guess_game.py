from random import Random


def generate_number(difficulty):
    secret_number = Random.random(difficulty)
    return secret_number


def get_guess_from_user(difficulty):
    guessed_number = input(f'Guess a number between 0 and {difficulty}!')
    return guessed_number


def compare_results(guessed_number, secret_number):
    return True if secret_number == guessed_number else False


def play(user_difficulty):
    secret_number = generate_number(user_difficulty)
    guessed_number = get_guess_from_user(user_difficulty)
    result = compare_results(guessed_number, secret_number)
    if result:
        print('You win!')
    else:
        print('You lose!')
    return result
