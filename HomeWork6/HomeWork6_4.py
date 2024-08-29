def common_elements():
    list_multiple_three = []
    list_multiple_five = []

    for number in range(0, 100):
        if not number % 3:
            list_multiple_three.append(number)

    for number in range(0, 100):
        if not number % 5:
            list_multiple_five.append(number)

    return set(list_multiple_three).intersection(set(list_multiple_five))


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("OK")
