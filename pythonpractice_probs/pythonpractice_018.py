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


# ----

u_guess = input('enter any 4 digit number\nmake thy first guess\n>>> ')
u_guess_lst = [int(d) for d in str(u_guess)]

# ----

# print(u_guess_lst, type(u_guess_lst))

# ----
     # ----
guess = 0

while guess < 3 :
    guess += 1
    cow = 0
    bull = 0

    if u_guess == 'quit' : break
    if u_guess_lst == rand_num_gen :
        cow = 4
    else :
        cow = 0
        bull = 0


        for i in range(0, 3) :
            if u_guess_lst[i] == rand_num_gen[i]:
                cow += 1
            elif u_guess_lst[i] in rand_num_gen:
                bull += 1


if cow == 4 :
    print('!!!!!! YOU WIN !!!!!!')
else :
    print('you have {0} COW(s) and {1} BULL(s)'.format(cow, bull))

    # for (i, n) in (u_guess_lst, rand_num_gen) :
    #     if i == n :
    #         print('you have found a perfect match, +1 cows')
    #         cow += 1


# matches = [x for x in u_guess_lst if x in rand_num_gen]
# print(matches)

    # ----
# ----

# cowbullgame(u_guess_lst, rand_lst)
print('*end*')

# ----

# ...........................

# import random

# def game(num_digits):
    # generate list of random integers of length num_digits
    # listnum = [random.randint(0,9) for n in range(num_digits)]
    # print("Solution key = " + str(listnum))

    # count=0
    # while True:
        # count+=1
        # print("~~~ Guess: " + str(count) + " ~~~")

        # print("Please guess " + str(num_digits) + "-digit number: ")
        # transform input string (e.g. "1234") to list of integers (e.g. [1,2,3,4])
        # guess = [int(i) for i in str(input())]

#         if guess == listnum:
#             print("You won.")
#             print("It took you "+str(count)+" guess(es).")
#             break
#
#         else:
#             cow=0
#             bull=0
#
#             for x in range(0,num_digits):
#                 if guess[x]==listnum[x]:
#                     cow += 1
#                 elif guess[x] in listnum: # look if digit is somewhere else in the solution key (might already be a cow)
#                     bull += 1
#
#         print("Cows: "+str(cow)+" Bulls: "+str(bull))
#         print("++++++++++++++++")
#
# game(4)
