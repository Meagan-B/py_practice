import numpy

board = [i for i in range(1,10)]
print(board)

move = input('make your move, input digit from 1-9\n>>> ')
move = int(move) 

for i in board :
    if move == i :
        print(i)
        i = move
        print(i)

print(move)
print(board)

#arr = numpy.asarray([1, 6, 1, 9, 8])
#arr[ arr == 8 ] = 0 
#print(arr)