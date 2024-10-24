import random
import requests


def get_money_interval(difficulty, usd_amount):
    exchange_rate = get_exchange_rate()
    correct_value = usd_amount * exchange_rate
    allowed_delta = 10 - difficulty
    return correct_value - allowed_delta, correct_value + allowed_delta


def get_exchange_rate():
    try:
        # Fetching exchange rate from a free API
        response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
        data = response.json()
        return data['rates']['ILS']
    except Exception as e:
        print(f"Failed to fetch exchange rate: {e}")
        return None


def get_guess_from_user(usd_amount):
    while True:
        try:
            return float(input(f"Guess the value in NIS for {usd_amount} USD: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def compare_results(difficulty, usd_amount):
    interval = get_money_interval(difficulty, usd_amount)
    if interval is None:
        return False
    guess = get_guess_from_user(usd_amount)
    return interval[0] <= guess <= interval[1]


def play(difficulty):
    usd_amount = random.randint(1, 100)
    return compare_results(difficulty, usd_amount)


if __name__ == "__main__":
    difficulty = int(input("Enter difficulty level (1-10): "))
    if play(difficulty):
        print("Congratulations! You won.")
    else:
        print("You loose!")
