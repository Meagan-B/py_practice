# Create a program that will play the “cows and bulls” game with the user. The game works like this:
#
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.
# >>>>>>>>>>>>>>>>>>>>>


# ----

def random_set_buildr(set_length) :
    import random

    global set_length
    # set_length = int(input('enter desired length of random number set below\n>>> '))

    rand_select = [random.randint(0, 10) for i in range(set_length)]
    print(rand_select)

# ----

set_length = int(input('enter desired length of random number set below\n>>> '))
random_set_buildr(set_length)

# ----

# ----


# ----




# ...........................
