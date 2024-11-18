import os
from utils import SCORES_FILE_NAME

POINTS_OF_WINNING = lambda difficulty: (difficulty * 3) + 5

def add_score(difficulty):
    try:
        if os.path.exists(SCORES_FILE_NAME):
            with open(SCORES_FILE_NAME, "r") as file:
                current_score = int(file.read().strip())
        else:
            current_score = 0

        new_score = current_score + POINTS_OF_WINNING(difficulty)
        with open(SCORES_FILE_NAME, "w") as file:
            file.write(str(new_score))
        print(f"Score updated successfully: +{POINTS_OF_WINNING(difficulty)} points. New score: {new_score}")
    except Exception as e:
        print(f"Error: Unable to update the score. {e}")
