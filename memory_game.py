import random
import time
import os
from utils import clear_screen

def generate_sequence(difficulty):
    return [random.randint(1, 101) for _ in range(difficulty)]


def display_sequence(sequence, visible_duration=0.7):
    print("Try to remember this sequence:")
    print(sequence)
    time.sleep(visible_duration)
    clear_screen()


def get_list_from_user(difficulty):
    print(f"Enter the {difficulty} numbers you saw earlier:")
    user_input = input().split()
    try:
        return [int(num) for num in user_input]
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return []


def is_list_equal(seq1, seq2):
    return seq1 == seq2


def play(difficulty):
    sequence = generate_sequence(difficulty)
    display_sequence(sequence)
    user_sequence = get_list_from_user(difficulty)
    return is_list_equal(sequence, user_sequence)


if __name__ == "__main__":
    difficulty = int(input("Enter difficulty level (1-10): "))
    if play(difficulty):
        print("Congratulations! You won.")
    else:
        print("You loose!")

