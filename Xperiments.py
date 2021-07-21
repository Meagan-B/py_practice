#def win_chk(p) :
 #   wins = [(1,2,3),(1,5,9),(1,4,7),(2,5,8),(3,6,9),(3,5,7),(4,5,6),(7,8,9)]
  #  p = [int(m) for m in p]
   # print(p)
    
    #for l in wins :
     #   l = set(l)
      #  p = set(p)
       # if l == p :
        #    print('win')
            
#++++++++++++++++++++++++++++++
#ply_count = 0
#ply_track = []

#while ply_count < 3 :
 #   move = input('make your move, input digit from 1-9\n>>> ')
  #  ply_track += move
   # ply_count += 1


#win_chk(ply_track)
#++++++++++++++++++++++++++++++

def char_replace(arr, find, replace):
    print('ORIGINAL: {0}'.format(arr))
    
    for cnt in range(arr.count(find)):
        arr[find - 1] = replace
        print('MODIFIED array: {0}'.format(arr))
        #board_print(arr)
   
board = [1, 2, 3, 'X', 5, 6, 7, 'O', 9]
import random

def computer_ply(arr) :
    arr_clean = []
    
    for i in arr :
        #print(int(i))
        if i == 'X' or i == 'O' : continue
        else :
            arr_clean.append(i)

    computer_play = random.choice(arr_clean)
    
    return computer_play
    
computer_ply(board)

