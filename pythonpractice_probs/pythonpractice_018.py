# Create a program that will play the “cows and bulls” game with the user. The game works like this:
#
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.
# >>>>>>>>>>>>>>>>>>>>>

welcome = '\n@@@@@@@@@@@@@@@@\n~~~~ WELCOME ~~~~\nto "cows & bulls"\n@@@@@@@@@@@@@@@@\n\n'
how_to_play = 'For every correctly guessed digit in the CORRECT placement,\nyou shall receive a COW\nFor every correctly guessed digit in the INCORRECT placement,\nyou shall receive a BULL\n\n!!!!4 COWs wins the game!!!!\n\n'
print(welcome + how_to_play)

# ----

import random

# ----

rand_num_gen = [random.randint(0, 9) for i in range(4)]
num_strs = [str(n) for n in rand_num_gen]
rand_str = int("".join(num_strs))

print('* random number generated: {0} *'.format(rand_str))

# ----

u_guess = int(input('enter any 4 digit number\nmake thy first guess\n>>> '))
print('* user guess #1: {0} *'.format(u_guess))

# ----

# guesses = 1
# cows = 0
# bulls = 0

print(u_guess == rand_str)


# while True :
#     print(u_guess, rand_str)
#     if u_guess == 'quit' : break
# elif u_guess == rand_str True :
#         print('you have {0} COWS!!!'.format(4))
#         break
#     else :
#         print('* else *')
#         break
    # else :
    #     for i in u_guess :
    #     print(i)
    #     if i == rand_num_gen :
    #         print('cool!')
    # cows = 0
    # bulls = 0
    #
    #
    # guesses += 1
    # cows += 1
    #
    # guesses += 1
    # bulls += 1
    #
    # u_guess = input('guess again\n>>> ')


# ----

# ----


# ----




# ...........................
