my_list = [6]
result = 0

if not my_list:
    my_list = [0]
else:
    for index, number in enumerate(my_list):

        if not index % 2:
            result += my_list[index]

print(result * my_list[-1])




