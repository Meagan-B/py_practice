#import numpy

board = [i for i in range(1,10)]
print(board)

move = input('make your move, input digit from 1-9\n>>> ')
move = int(move) 


def f1(arr, find, replace):
    print('ORIGINAL array: {0}\nfind: {1}\nreplacement: {2}'.format(arr, find, replace))
    for cnt in range(arr.count(find)):
        arr[find - 1] = replace
        print('MODIFIED array: {0}'.format(arr))

f1(board, move, 'X')
