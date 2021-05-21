# Create a program that will play the “cows and bulls” game with the user. The game works like this:
#
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.
# >>>>>>>>>>>>>>>>>>>>>

welcome = '\n@@@@@@@@@@@@@@@@\n~~~~ WELCOME ~~~~\nto "cows & bulls"\n@@@@@@@@@@@@@@@@\n\n'
how_to_play = 'For every correctly guessed digit in the CORRECT placement,\nyou shall receive a COW\nFor every correctly guessed digit in the INCORRECT placement,\nyou shall receive a BULL\n\n!!!!4 COWs wins the game!!!!\n\n'
# print(welcome + how_to_play)

# ----

import random

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

guess = 1

while guess < 10 :
    cow = 0
    bull = 0

    if u_guess == 'quit' : break
    if u_guess_lst == rand_num_gen :
        cow = 4
    else :
        cow = 0
        bull = 0


        for i in range(0, 4) :
            if u_guess_lst[i] == rand_num_gen[i]:
                cow += 1
            elif u_guess_lst[i] in rand_num_gen:
                bull += 1
            else: continue



    if cow == 4 :
        print('!!!!!! YOU WIN !!!!!!')
    else :
        print('you have {0} COW(s) and {1} BULL(s)'.format(cow, bull))

    u_guess = input('\nmake thy next guess\n>>> ')
    guess += 1
# ----

# cowbullgame(u_guess_lst, rand_lst)
print('*end*')

# ...........................
