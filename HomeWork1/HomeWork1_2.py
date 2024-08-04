
user_input = int(input("Please write a 5 numbers: "))

first_number = user_input // 10000

second_number = (user_input % 10000) // 1000

third_number = (user_input % 1000) // 100

fourth_number = (user_input % 100) // 10

fifth_number = user_input % 10

print(str(fifth_number)+str(fourth_number)+str(third_number)+str(second_number)+str(first_number))