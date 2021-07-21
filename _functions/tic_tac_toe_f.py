# tic-tac-toe re-write
#---->>>>>>>>>>>>-------->>>>>>>>>>>>----#
import random
import numpy
#----••••••••----••••••••----••••••••----#
# game board

def board_print(b):
    print(b[:3])
    print(b[3:6])
    print(b[6:])
    
#board_print(board)
#----••••••••----••••••••----••••••••----#
# player select

def char_select():
    usr_char = input('would you like X or O ?\n>>> ').capitalize()
    (h, c) = '',''
    
    if usr_char != 'X' and usr_char != 'O':
        (h, c) = ('X','O')
        print('INCORRECT character input\nyou have been automatically assigned X')
        
    if usr_char == 'X' :
        (h, c) = ('X','O')
    else :
        (h, c) = ('O','X')
     
    return (h, c) 
      
human, comp = char_select()
print('PLAYER: {0}\nCOMP: {1}'.format(human, comp))       
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

def win_chk(h, c) :
    wins = [(1,2,3),(1,5,9),(1,4,7),(2,5,8),(3,6,9),(3,5,7),(4,5,6),(7,8,9)]
    ply = [int(m) for m in ply]
    print(ply)
    
    for l in wins :
        l = set(l)
        p = set(p)
        if l == p :
            print('win')

#def win_chk(,)    
#----••••••••----••••••••----••••••••----#
# RANDOM computer play,
# needs AI to make something more advanced
            
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

def play(h, c) :
    h_ply_count = 0
    c_ply_count = 0
   
    h_ply_track = []
    c_ply_track = []
    
    board = [i for i in range(1,10)]
    board_print(board)
    
    while h_ply_count < 3 :
        move = input('make your move, input digit from 1-9\n>>> ')
        
        x = move.isnumeric()
        if x is True :
            
            move = int(move)
            
            for i in board :
                if move == i :
                    #player move
                    h_ply_count += 1
                    h_ply_track.append(move)
                    char_replace(board, move, h)
                    
                    ######START HERE#######
                    #computer move
                    c_move = computer_ply(board)
                    c_ply_count += 1
                    c_ply_track.append(c_move)
                    char_replace(board, (computer_ply(board)), c)
                    
                    continue
                
                elif move != i : continue    
                
                else :
                    print('invalid play')
                    continue   
             
        else:
            print('INCORRECT character input\n')
            continue        
        
        
#first 3 plays for player 1/2 plays for player 2        
play(human, comp)    
#checking for winner after player 1 makes 3 moves
win_chk(human,comp)
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