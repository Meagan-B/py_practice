# Create a program that will play the “cows and bulls” game with the user. The game works like this:
#
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.
# >>>>>>>>>>>>>>>>>>>>>

welcome = '\n@@@@@@@@@@@@@@@@\n~~~~ WELCOME ~~~~\nto "cows & bulls"\n@@@@@@@@@@@@@@@@\n\n'
how_to_play = 'For every correctly guessed digit in the CORRECT placement,\nyou shall receive a COW\nFor every correctly guessed digit in the INCORRECT placement,\nyou shall receive a BULL\n\n!!!!4 COWs wins the game!!!!\n\n'
# print(welcome + how_to_play)

# ----

import random
import collections
from collections import Counter

# ----

# need to address occasional 3 digit numbers
rand_num_gen = [random.randint(0, 9) for i in range(4)]
print(rand_num_gen, type(rand_num_gen))
# rand_lst = list(rand_num_gen)
# print(rand_lst, type(rand_lst))
# num_strs = [str(n) for n in rand_num_gen]
# print(num_strs, type(num_strs))
# rand_str = int("".join(num_strs))
# print(rand_str, type(rand_str))

print('* random number generated: {0} *'.format(rand_num_gen))

# ----

u_guess = input('enter any 4 digit number\nmake thy first guess\n>>> ')
print('* user guess #1: {0} *'.format(u_guess))
u_guess_lst = [int(d) for d in str(u_guess)]

print(u_guess_lst, type(u_guess_lst))

# ----

# cow_bull = [0,0]
#
# def cowbullgame(guess, random_lst) :
#     # cow_bull = [0,0]
#     global cow_bull
#
#     for i, n in zip(guess, random_lst) :
#
#         if i in random_lst :
#
#             if i == n :
#                 cow_bull[0] += 1
#             else :
#                 cow_bull[1] += 1
#
#     # COWS
#     if cow_bull[0] > 1 or cow_bull[0] == 0 :
#         print('you have {0} COWS'.format(cow_bull[0]))
#     elif cow_bull[0] == 1 :
#         print('you have {0} COW'.format(cow_bull[0]))
#     # BULLS
#     elif cow_bull[1] > 1 or cow_bull[1] == 0 :
#         print('\n& {0} BULLS'.format(cow_bull[1]))
#     elif cow_bull[1] == 1 :
#         print('you have {0} BULL'.format(cow_bull[1]))
#     # WIN
#     elif cow_bull[0] == 4 :
#         print('!!!!!! YOU WIN !!!!!!')
#
# # ----
#
# guesses = 0
#
# while (u_guess != 'quit'):
#     print('GUESS #{0}\n'.format(guesses))
#     cowbullgame(u_guess, rand_lst)
#
# # RESULTS
# # COWS
#     if cow_bull[0] > 1 or cow_bull[0] == 0 :
#         print('step 4a')
#         print('you have {0} COWS'.format(cow_bull[0]))
#     elif cow_bull[0] == 1 :
#         print('step 4b')
#         print('you have {0} COW'.format(cow_bull[0]))
# # BULLS
#     elif cow_bull[1] > 1 or cow_bull[1] == 0 :
#         print('step 4c')
#         print('\n& {0} BULLS'.format(cow_bull[1]))
#     elif cow_bull[1] == 1 :
#         print('step 4d')
#         print('you have {0} BULL'.format(cow_bull[1]))
# # WIN
#     elif cow_bull[0] == 4 :
#         print('!!!!!! YOU WIN !!!!!!')
#
#
#     if cow_bull[0] == 4 :
#         u_guess = 'quit'
#
#     u_guess = input('guess again\n>>> ')
#     u_guess = list(u_guess.split())
#
#     guesses += 1

# ----
     # ----
cow = 0
bull = 0

print(collections.Counter(u_guess) == collections.Counter(rand_num_gen))
print(collections.Counter(u_guess), collections.Counter(rand_num_gen))

if collections.Counter(u_guess) == collections.Counter(rand_num_gen) :

    for i, n in zip(u_guess, rand_num_gen) :

        print('step 1', i, n)
        if i in rand_num_gen :
            print('step 2', i)
            if i == n :
                cow += 1
                print('step 3a', cow)
            else :
                bull += 1
                print('step 3b', bull)
        print(cow, bull)
    # ----
# ----

# cowbullgame(u_guess_lst, rand_lst)
print('*end*')

# ----

# ...........................

# Geeks for Geek code that saved me,
#
# def numOfBullsCows(num,guess):
#     bull_cow = [0,0]
#     num_li = getDigits(num)
#     guess_li = getDigits(guess)
#
#     for i,j in zip(num_li,guess_li):
#
#         # common digit present
#         if j in num_li:
#
#             # common digit exact match
#             if j == i:
#                 bull_cow[0] += 1
#
#             common digit match but in wrong position
#             else:
#                 bull_cow[1] += 1
#
#     return bull_cow
