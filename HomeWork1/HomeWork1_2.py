
user_input = int(input("Please write a 5 numbers: "))

first_number = user_input // 10000

second_number = (user_input % 10000) // 1000 * 10

third_number = (user_input % 1000) // 100 * 100

fourth_number = (user_input % 100) // 10 * 1000

fifth_number = user_input % 10 * 10000

print(fifth_number + fourth_number + third_number + second_number + first_number)