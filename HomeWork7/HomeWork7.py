def add_one(some_list: list) -> list:
    final_number = 0
    for number in some_list:
        final_number = final_number * 10 + number
    final_number += 1

    final_list = []
    while final_number > 0:
        final_list.append(final_number % 10)
        final_number //= 10
    final_list.reverse()
    return final_list


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
