board = [i for i in range(1,10)]

move = input('make your move, input digit from 1-9\n>>> ')
 
arr = numpy.asarray(board)
print(arr)
arr[ arr == 'b' ] = move # change all occurrences of x by y
print(arr)
ply_count += 1
                