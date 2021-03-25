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

# print('\n~~~~~~~~ HOW TO PLAY ~~~~~~~~\n\n\n')

# ----

# = input('')

# ----

# p_score = 0

# ----

while True :
    print('\n•••••••• NEW GAME ••••••••\n')

    game = input('\nenter your guess below……\nNUMBERs from 1-9 ONLY\n>>> ')
    rand_select = random.randint(1, 9)

    if game == 'exit' : break
    elif game is rand_select :
        print('******** WINNER ********\nyour guess ( %s ) is correct!' % game)
        if input('\nenter another number to continue playing\nenter "exit" to QUIT\n*CASE SENSITIVE*\n >>> ') != 'exit' : continue
    elif game is < rand_select :
        print('\nyour guess ( %s ) is TOO LOW' % game)
        if input('\nenter another number to continue playing\nenter "exit" to QUIT\n*CASE SENSITIVE*\n >>> ') != 'exit' : continue
    elif game is > rand_select :
        print('\nyour guess ( %s ) is TOO HIGH' % game)
        if input('\nenter another number to continue playing\nenter "exit" to QUIT\n*CASE SENSITIVE*\n >>> ') != 'exit' : continue

# ----

print('\nxxXXXXxx GAME OVER xxXXXXxx')

# ...........................
