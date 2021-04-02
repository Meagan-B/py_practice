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

print('\n•••••••• HOW TO PLAY ••••••••\nguess a randomly selected number\ninput a NUMBER from 1-9\nenter "exit" to end program\n')

# ----

def random_set_buildr() :
p_guess = 0
game = None

rand_select = random.randint(1, 9)

while game != 'exit' :

    game = input('\nenter your guess below……\nNUMBERs from 1-9 ONLY\n>>> ')

    if game == 'exit' : break

    game = int(game)

    if game is rand_select :
        p_guess += 1
        print('******** WINNER ********\nyour guess ( %s ) is correct!\nit took %s guesses to win' % (game, p_guess))
        break
    elif game < rand_select :
        print('\nyour guess ( %s ) was TOO LOW\n' % game)
        p_guess += 1
        continue
    elif game > rand_select :
        print('\nyour guess ( %s ) was TOO HIGH\n' % game)
        p_guess += 1
        continue

# ----

print('\nthanks for playing!\n++++++++ GAME OVER ++++++++')

# ...........................
