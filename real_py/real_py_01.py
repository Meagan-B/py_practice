# Sum of Integers Up To n
#     Write a function, add_it_up, which returns the sum of the integers from 0
#     to the single integer input parameter.
#     The function should return 0 if a non-integer is passed in.

# >>>>>>>>>>>>>>>>>>>>>>>

def add_it_up(num) :
    sum_lst = []
    sum_num = 0

    print([i for i in range(0, num + 1)])
    for i in range(0, num + 1) :
        sum_lst.append(i)
        sum_num += i

    print(sum_lst, sum_num)

    return sum_lst
    return sum_num

# ----

usr_x = int(input('enter a number from 1-9\n>>> '))

# ----

print(add_it_up(usr_x))


# ...........................
