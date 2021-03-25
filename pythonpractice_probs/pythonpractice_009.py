# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)
#
# Extras:
#
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.
#
# >>>>>>>>>>>>>>>>>>>>>

import random

# ----

print('\n•••••••• HOW TO PLAY ••••••••\nguess a randomly selected number from 1-9\ninput a NUMBER from 1-9\nenter "exit" to end program\n')

# ----

p_guess = 0

# ----

rand_select = random.randint(1, 9)

# ----

while True :

    game = input('\nenter your guess below……\nNUMBERs from 1-9 ONLY\n>>> ')

    if game != 'exit' :
        game = int(game)
    elif game == 'exit' : break

    if game is rand_select :
        print('******** WINNER ********\nyour guess ( %s ) is correct!' % game)
        p_guess += 1
        break
    elif game < rand_select :
        print('\nyour guess ( %s ) was TOO LOW\nthe random number was……%s' % game rand_select)
        p_guess += 1
        if input('\nenter another number to continue guessing\nenter "exit" to QUIT\n*CASE SENSITIVE*\n >>> ') != 'exit' : continue
    elif game > rand_select :
        print('\nyour guess ( %s ) was TOO HIGH\nthe random number was……%s' % game rand_select)
        p_guess += 1
        if input('\nenter another number to continue guessing\nenter "exit" to QUIT\n*CASE SENSITIVE*\n >>> ') != 'exit' : continue

# ----

print('\nthanks for playing!\n++++++++ GAME OVER ++++++++')

# ...........................
