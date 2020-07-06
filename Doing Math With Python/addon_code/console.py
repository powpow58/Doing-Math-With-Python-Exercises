import os
from time import sleep

# The screen clear function
def screen_clear():
    # For mac and linux(both, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # For Windows
        _ = os.system('cls')
