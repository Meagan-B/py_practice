# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
#
# Remember the rules:
# Rock beats scissors
# Scissors beats paper
# Paper beats rock
#
# >>>>>>>>>>>>>>>>>>>>>

player_one = input('enter name for player one >>> ')
player_two = input('enter name for player two >>> ')

# ----

print('~ HOW TO PLAY ~\n using numbers (1,2 or 3), make a play (ROCK, PAPER or SCISSORS)\n ROCK beats SCISSORS\n SCISSORS beats PAPER\n PAPER beats ROCK\n ~ GAME CONTROLS ~\n 1) ROCK\n 2) PAPER\n 3) SCISSORS\n enter x to exit program' )

# ----

def play_compare() :
    p1 = input('%s enter your play……\n' % player_one)
    p2 = input('%s enter your play……\n' % player_two)
    if p1 == p2:
        print("tie, there is NO winner")
    elif p1 == 1 and p2 == 2:
        print('%s is the winner!' % p2)
    elif p1 == 1 and p2 == 3:
        print('%s is the winner!' % p1)
    elif p1 == 2 and p2 == 3:
        print('%s is the winner!' % p2)
    elif p1 == 2 and p2 == 1:
        print('%s is the winner!' % p2)
    elif p1 == 3 and p2 == 2:
        print('%s is the winner!' % p1)
    elif p1 == 3 and p2 == 1:
        print('%s is the winner!' % p2)
    elif p1 > 3 or p1 < 1 or p2 > 3 or p2 < 1 :
        print('invalid input')

# ----

while p1 != 'x' or p2 != 'x' :
    play_compare()

# ----


# ...........................
