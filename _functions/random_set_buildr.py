# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)
#
# Extras:
#
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.
#
# >>>>>>>>>>>>>>>>>>>>>
# WIP
# MAKE INTO FUNCTION

import random

# ----

def random_set_buildr() :
    import random

    set_length = int(input('enter desired length of random number set below\n>>> '))
    set_start = int(input('enter range START, for random number set, below\n>>> '))
    set_end = int(input('enter range END, for random number set, below\n>>> '))
    rand_select = random.randint(set_start, set_end + 1, set_length)

# ----

random_set_buildr()

# ...........................
