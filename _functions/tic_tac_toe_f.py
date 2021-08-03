# tic-tac-toe re-write
#---->>>>>>>>>>>>-------->>>>>>>>>>>>----#
import random
import numpy
#----••••••••----••••••••----••••••••----#
# game board
# NEEDS: better formatting once a play has been made

def board_print(b):
    print(b[:3])
    print(b[3:6])
    print(b[6:])
    
#board_print(board)
#----••••••••----••••••••----••••••••----#
# player select
# NEEDS:
        # a way to randomly select who goes first (player_1 & player_2)
        # asking for player preferences (will AI be necessary or not)

def char_select():
    usr_char = input('would you like X or O ?\n>>> ').capitalize()
    (p1, p2) = '',''
    
    if usr_char != 'X' and usr_char != 'O':
        (p1, p2) = ('X','O')
        print('INCORRECT character input\nyou have been automatically assigned X')
        
    if usr_char == 'X' :
        (p1, p2) = ('X','O')
    else :
        (p1, p2) = ('O','X')
     
    return (p1, p2) 
      
player_1, player_2 = char_select()
print('PLAYER 1: {0}\nPLAYER 2: {1}'.format(player_1, player_2))       
#----••••••••----••••••••----••••••••----#
# character replacement

def char_replace(arr, find, replace):
    #print('ORIGINAL array: {0}\nfind: {1}\nreplacement: {2}'.format(arr, find, replace))
    for cnt in range(arr.count(find)):
        arr[find - 1] = replace
        #print('MODIFIED array: {0}'.format(arr))
        board_print(arr)
#----••••••••----••••••••----••••••••----#
# win check
# NEEDS: a lot of work, currently NOT functional

                    ######START HERE#######
def win_chk(p) :
    wins = [(1,2,3),(1,5,9),(1,4,7),(2,5,8),(3,6,9),(3,5,7),(4,5,6),(7,8,9)]
    w = None
    
    if len(p) > 2 :
        ply_set = set(p)
    
        for d in wins :
            d_set = set(d)
    
            if d_set == ply_set :
                 w = True
                 print('{0} WINS the game'.format(p))
                 return w
            else :
                 w = False
        
        if w == False :
            return w

#def win_chk(p)    
#----••••••••----••••••••----••••••••----#
# RANDOM computer play,
# NEEDS:
        # AI for more advanced game strategy
        # block to ask if there will be 1 or 2 human players
    
            
def computer_ply(arr) :
    arr_clean = []
    
    for i in arr :
        if i == 'X' or i == 'O' : continue
        else :
            arr_clean.append(i)

    computer_play = random.choice(arr_clean)
    
    return computer_play

#computer_ply(board)
#----••••••••----••••••••----••••••••----#
# game play
# NEEDS:
        # element to begin play with pre-selected player (who goes first)
        # add text block for in between plays
        
def play(p1, p2) :
    plyr_1_count = 0
    plyr_1_track = []
    
    plyr_2_count = 0
    plyr_2_track = []
    
    board = [i for i in range(1,10)]
    board_print(board)
    
    while plyr_1_count < 9 :
        move = input('make your move, input digit from 1-9\n>>> ')
        
        x = move.isnumeric()
        if x is True :
            
            move = int(move)
            
            for i in board :
                if move == i :
                    #player move
                    plyr_1_count += 1
                    plyr_1_track.append(move)
                    print("\nPLAYER 1 move >>>")
                    char_replace(board, move, p1)
                    
                    #checking for winner
                    win_chk(plyr_1_track)
                    
                    #computer move
                    c_move = computer_ply(board)
                    plyr_2_count += 1
                    plyr_2_track.append(c_move)
                    print("\nPLAYER 2 move >>>")
                    char_replace(board, (computer_ply(board)), p2)
                    
                    #checking for winner
                    win_chk(plyr_2_track)
                    
                    continue
                
                elif move != i : continue    
                
                else :
                    print('invalid play')
                    continue   
             
        else:
            print('INCORRECT character input\n')
            continue        
               
play(player_1, player_2)    
#---->>>>>>>>>>>>-------->>>>>>>>>>>>----#


### tic-tac-toe ORIGINAL, https://hackr.io/blog/python-projects ###

#def print_board():
 #   x=1
  #  for i in board:
   #     end = ' | '
    #    if x%3 == 0:
     #       end = ' \n'
      #      if i != 1: end+='---------\n';
       # char=' '
        #if i in ('X','O'): char=i;
        #x+=1
        #print(char,end=end)
        
#def can_win(brd, player, move):
 #   places=[]
  #  x=0
   # for i in brd:
    #    if i == player: places.append(x);
     #   x+=1
    #win=True
    #for tup in winners:
     #   win=True
      #  for ix in tup:
       #     if brd[ix] != player:
        #        win=False
         #       break
        #if win == True:
         #   break
    #return win

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
##AI goes here
def computer_move():
    move=-1
##If I can win, others do not matter.
    for i in range(1,10):
        if make_move(board, computer, i, True)[1]:
            move=i
            break
    if move == -1:
##If player can win, block him.
        for i in range(1,10):
            if make_move(board, player, i, True)[1]:
                move=i
                break
    if move == -1:
##Otherwise, try to take one of desired places.
        for tup in moves:
            for mv in tup:
                if move == -1 and can_move(board, computer, mv):
                    move=mv
                    break
    return make_move(board, computer, move)

def space_exist():
    return board.count('X') + board.count('O') != 9

player, computer = select_char()
print('Player is [%s] and computer is [%s]' % (player, computer))
result='%%% Deuce ! %%%'

while space_exist():
    print_board()
    print('#Make your move ! [1-9] : ', end='')
    move = int(input())
    moved, won = make_move(board, player, move)
    if not moved:
        print(' >> Invalid number ! Try again !')
        continue

    if won:
        result='*** Congratulations ! You won ! ***'
        break
    elif computer_move()[1]:
        result='=== You lose ! =='
        break;
print_board()
print(result)