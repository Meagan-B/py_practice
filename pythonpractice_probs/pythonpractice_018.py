# Create a program that will play the “cows and bulls” game with the user. The game works like this:
#
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.
# >>>>>>>>>>>>>>>>>>>>>

welcome = 'WELCOME\nto "cows & bulls"\n@@@@@@@@@@@@@@@@\n\n'
# print(welcome)

# ----
import random
# ----
rand_num_gen = [random.randint(0, 9) for i in range(4)]
num_strs = [str(n) for n in rand_num_gen]
rand_str = int("".join(num_strs))

print('* random number generated: {0} *'.format(rand_str))
# ----

u_guess = input('enter any 4 digit number\nmake thy first guess\n>>> ')
g_lst = [str(i) for i in u_guess]
g_str = int("".join(g_lst))

for i in u_guess :
    g_lst.append(i)
print('* user guess: {0}'.format(g_lst))
print(type(g_lst))

# ----

# guesses = 0
# cows = 0
# bulls = 0

# while (u_guess != 'quit') and (cows != 4) :
#     if u_guess == rand_str :
#         print('you have {0} COWS!!!'.format(4))
#     for i in u_guess :
#         print(i)
#         if i == rand_num_gen :
#             print('cool!')
#     # cows = 0
#     # bulls = 0
#     #
#     #
#     # guesses += 1
#     # cows += 1
#     #
#     # guesses += 1
#     # bulls += 1
#     #
#     u_guess = input('guess again\n>>> ')


# ----

# ----


# ----




# ...........................
