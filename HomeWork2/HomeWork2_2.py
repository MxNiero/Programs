my_list = [12,3,4,10,8]

if my_list == []:
    print(my_list)
else:
    my_list.insert(0,my_list[-1])
    my_list.pop()
    print(my_list)

