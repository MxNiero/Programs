my_list = [1, 2, 3, 4, 5, 6]

if not my_list:
    print(my_list)
else:
    my_list.insert(0, my_list[-1])
    my_list.pop()
    print(my_list)

