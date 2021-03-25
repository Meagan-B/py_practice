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

    game = input()
    rand_select = random.randint(1, 9)

    if game == 'exit' : break
elif game is rand_select :
    print('~~~~~~~~ WINNER ~~~~~~~~\nyour guess ( %s ) is correct!' % game)
    # if game == 0 :
    #     print('\n<<<< DRAW, there is NO winner >>>>')
    #     if input('\nwould you like to play again?\n"Y" for yes\nenter to QUIT\n*CASE SENSITIVE*\n >>> ') == 'Y' : continue
    #     else :
    #         break
# ----

print('\nxxXXXXxx GAME OVER xxXXXXxx')

# ...........................
