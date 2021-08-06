            
#++++++++++++++++++++++++++++++

def win_chk(p) :
    wins = [(1,2,3),(1,5,9),(1,4,7),(2,5,8),(3,6,9),(3,5,7),(4,5,6),(7,8,9)]
    #ply = [int(m) for m in p]
    ply_set = set(p)
    w = None
   
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

#++++++++++++++++++++++++++++++
        
p1 = [1, 2, 3]
p2 = [4, 8, 9]
p3 = [1, 2]
p4 =[1, 2, 3, 4]

print(win_chk(p1))
print(win_chk(p2))
print(win_chk(p3))
print(win_chk(p4))