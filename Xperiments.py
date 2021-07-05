#import numpy

board = [i for i in range(1,10)]
print(board)

move = input('make your move, input digit from 1-9\n>>> ')
move = int(move) 

#for i in board :
   # if move == i :
  #      print(i)
 #       i = 'X'
#        print(i)
        #need to find way to replace the i in board, reverse the for i loop to put it back with new value

#print(move)
#print(board)


def f1(arr, find, replace):
    print('ORIGINAL array: {0}\nfind: {1}\nreplace: {2}'.format(arr, find, replace))
    for cnt in range(arr.count(find)):
        arr[find - 1] = replace
        print('MODIFIED array: {0}'.format(arr))

f1(board, move, 'X')


#arr = numpy.asarray([1, 6, 1, 9, 8])
#arr[ arr == 8 ] = 0 
#print(arr)