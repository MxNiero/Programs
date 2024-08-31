def common_elements():
    list_multiple_three = list(range(0, 100, 3))
    list_multiple_five = list(range(0, 100, 5))
    return set(list_multiple_three).intersection(set(list_multiple_five))


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("OK")
