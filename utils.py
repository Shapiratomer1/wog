import os

SCORES_FILE_NAME = 'scores.txt'
BAD_RETURN_CODE = 1

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear') # win/linux

