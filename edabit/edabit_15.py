def amplify(n) :
    amp_lst = []
    for i in range(0, n):
        if i % 4 == 0 :
            c = i * 10
            print(c)
            amp_lst.append(c)
        elif i % 4 != 0 :
            c = i
            print(c)
            amp_lst.append(c)
    return amp_lst


amplify(5)
amplify(10)
amplify(100)
