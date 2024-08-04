print("Please write a 4 numbers")
user_input = int(input())

first_number = user_input // 1000
print(first_number)

second_number = (user_input % 1000) // 100
print(second_number)

third_number = (user_input % 100) // 10
print(third_number)

fourth_number = user_input % 10
print(fourth_number)