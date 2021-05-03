# Create a program that will play the “cows and bulls” game with the user. The game works like this:
#
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.
# >>>>>>>>>>>>>>>>>>>>>

welcome = 'WELCOME\nto "cows & bulls"\n@@@@@@@@@@@@@@@@\n\n'
# print(welcome)

# ----
rand_select = []

def random_set_buildr(num) :
    global rand_select
    import random
    # set_length = int(input('enter desired length of random number set below\n>>> '))

    rand_select = [random.randint(0, 9) for i in range(num)]
    return rand_select
    print(rand_select)

random_set_buildr(4)



# ----
usr_guess = input('enter any 4 digit number to make you first guess\n>>> ').split()
count = 0

while usr_guess != rand_select :
    # for (i, n) in (usr_guess, rand_select) :
    c = [i for i in usr_guess if i == rand_select]
        # if i == n :
            # print(i)
    print(c)

    count += 1
    usr_guess = input('guess again\n>>> ')

    if usr_guess == 'q' : break
    

# ----

# ----


# ----




# ...........................
