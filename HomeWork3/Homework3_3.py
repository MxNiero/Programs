import random
my_list = []
final_list = []

for numbers in range(3, 10):
    my_list.append(random.randint(1, 10))
final_list.append(my_list[0])
final_list.append(my_list[2])
final_list.append(my_list[-2])

print(my_list, "=>", final_list)


