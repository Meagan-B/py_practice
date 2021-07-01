import numpy

board = [i for i in range(1,10)]
move = input('make your move, input digit from 1-9\n>>> ')
 
for i in board :
    if move == i : 
        arr = numpy.asarray(board)
        print(arr)
        arr[ arr == 'X' ] = move
        print(arr)

print(move)
print(board)

                