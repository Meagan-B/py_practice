# Create a program that will play the “cows and bulls” game with the user. The game works like this:
#
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.
# >>>>>>>>>>>>>>>>>>>>>

welcome = 'WELCOME\nto "cows & bulls"\n@@@@@@@@@@@@@@@@\n\n'
# print(welcome)

# ----


def random_set_buildr(num) :
    import random
    # set_length = int(input('enter desired length of random number set below\n>>> '))
    rand_num_gen = [random.randint(0, 9) for i in range(num)]
    print(rand_num_gen)
    return rand_num_gen

random_set_buildr(4)



# ----

usr_guess = input('enter any 4 digit number\n(from 1000-9999)\nmake thy first guess\n>>> ').split()
guesses = 0
cows = 0
bulls = 0

while (u_guess != ('quit', 'q')) and (cows != 4) :
    # for (i, n) in (usr_guess, rand_select) :
        # if i == n :
            # print(i)
    print(c)
    cows = 0
    bulls = 0


    guesses += 1
    cows += 1

    guesses += 1
    bulls += 1

    usr_guess = input('guess again\n>>> ')


# ----

# ----


# ----




# ...........................
