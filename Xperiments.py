def win_chk(p) :
    wins = [(1,2,3),(1,5,9),(1,4,7),(2,5,8),(3,6,9),(3,5,7),(4,5,6),(7,8,9)]
    print(wins)
    wins = set(wins)
    print(wins)
    p = [int(m) for m in p]
    print(p)
    

ply_count = 0
ply_track = []

while ply_count < 3 :
    move = input('make your move, input digit from 1-9\n>>> ')
    ply_track += move
    print(ply_track)
    ply_count += 1


win_chk(ply_track)