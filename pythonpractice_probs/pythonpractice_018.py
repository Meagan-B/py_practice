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

# u_guess_1 = int(input('enter any 4 digit number\nmake thy first guess\n>>> '))
# print('* user guess #1: {0} *'.format(u_guess_1))

u_guess = int(input('enter any 4 digit number\nmake thy first guess\n>>> '))
print('* user guess #1: {0} *'.format(u_guess))

# ----

def numOfBullsCows(num,guess):
    bull_cow = [0,0]
    num_li = getDigits(num)
    guess_li = getDigits(guess)

    for i,j in zip(num_li,guess_li):

        # common digit present
        if j in num_li:

            # common digit exact match
            if j == i:
                bull_cow[0] += 1

            # common digit match but in wrong position
            else:
                bull_cow[1] += 1

    return bull_cow


def cowbullgame() :
    cow_bull = [0,0]
    rand_num_gen
    u_guess


    if u_guess == rand_str :
        cow_bull[0] = 4
        return cow_bull
    else : continue


    for i, n in (u_guess, rand_num_gen) :

        if i in rand_num_gen :

            cow += 1
        elif u_guess[i] in rand_str[i] :
            bull += 1
        else :
            print('WHOPPSIES')


while (u_guess != 'quit') and (u_guess != rand_str) :
    cows = 0
    bulls = 0
    guesses = 1

    x = (u_guess == rand_str)
    # print(x)

    if x == True :
        print('!!!! YOU WIN !!!!\nyou have {0} COWS, in {1} turns'.format(4, guesses))
        break
    elif x == False : continue

    for i in u_guess :
        if u_guess[i] == rand_str[i] :
            cow += 1
        elif u_guess[i] in rand_str[i] :
            bull += 1
        else :
            print('WHOPPSIES')

    u_guess = input('guess again\n>>> ')


# ----

# ----

# ----

# ...........................
