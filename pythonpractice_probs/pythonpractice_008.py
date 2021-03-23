# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
#
# Remember the rules:
# Rock beats scissors
# Scissors beats paper
# Paper beats rock
#
# >>>>>>>>>>>>>>>>>>>>>

import getpass

# ----

player_one = input('enter name for player one >>> ')
player_two = input('enter name for player two >>> ')

# ----

print('~ HOW TO PLAY ~\nmake a play by entering\n"r" for rock\n"p" for paper\n"s" for scissors\n ROCK beats SCISSORS\n SCISSORS beats PAPER\n PAPER beats ROCK\n')

# ----

p1_score = 0
p2_score = 0
rps_game_dict = {'r':1, 'p':2, 's':3,'R':1, 'P':2, 'S':3}

# ----

while True :
    print('\n~~~~~~~~ NEW GAME ~~~~~~~~\n')
    p1 = getpass.getpass('%s enter your play……\n("r", "p" or "s")\n >>> ' % player_one)
    p2 = getpass.getpass('%s enter your play……\n("r", "p" or "s")\n >>> ' % player_two)
    p1_play = rps_game_dict.get(p1)
    p2_play = rps_game_dict.get(p2)
    game = p1_play - p2_play

    if game == 0 :
        print("DRAW, there is NO winner")
        if str(input('\nwould you like to play again?\nenter Y for yes\nenter N for no\n*CASE SENSITIVE*\n >>> ')) == 'Y' : continue
        else :
            break
    elif game == 1 :
        print(('%s is the winner!' % player_one).upper())
        p1_score += 1
        if str(input('\nwould you like to play again?\nenter Y for yes\nenter N for no\n*CASE SENSITIVE*\n >>> ')) == 'Y' : continue
        else :
            break
    elif game == -1 :
        print(('%s is the winner!' % player_two).upper())
        p2_score += 1
        if str(input('\nwould you like to play again?\nenter Y for yes\nenter N for no\n*CASE SENSITIVE*\n >>> ')) == 'Y' : continue
        else :
            break
    elif game == 2 :
        print(('%s is the winner!' % player_two).upper())
        p2_score += 1
        if str(input('\nwould you like to play again?\nenter Y for yes\nenter N for no\n*CASE SENSITIVE*\n >>> ')) == 'Y' : continue
        else :
            break
    elif game == -2 :
        print(('%s is the winner!' % player_one).upper())
        p1_score += 1
        if str(input('\nwould you like to play again?\nenter Y for yes\nenter N for no\n*CASE SENSITIVE*\n >>> ')) == 'Y' : continue
        else :
            break
    elif game <= -3 or game >= 3 :
        print('invalid input')
        if str(input('\nwould you like to play again?\nenter Y for yes\nenter N for no\n*CASE SENSITIVE*\n >>> ')) == 'Y' : continue
        else:
            break

# ----

print('thank you for playing\n~ GAME OVER ~')

# ...........................
