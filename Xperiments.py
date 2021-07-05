#import numpy

def board_print(b):
    #b = [[i] for i in b]
    print(b[:3])
    print(b[3:6])
    print(b[6:])
    
board = [i for i in range(1,10)]
board_print(board)

move = input('make your move, input digit from 1-9\n>>> ')
move = int(move) 

def char_replace(arr, find, replace):
    #print('ORIGINAL array: {0}\nfind: {1}\nreplacement: {2}'.format(arr, find, replace))
    for cnt in range(arr.count(find)):
        arr[find - 1] = replace
        #print('MODIFIED array: {0}'.format(arr))
        board_print(arr)
        
        
char_replace(board, move, 'x')