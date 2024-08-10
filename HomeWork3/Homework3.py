my_list = [0, 9, 0, 7, 31, 0, 45, 0, 45, 0]

for number in my_list:
    index_zero = my_list.index(0)
    delete_zero = my_list.pop(index_zero)
    my_list.append(delete_zero)
print(my_list)
