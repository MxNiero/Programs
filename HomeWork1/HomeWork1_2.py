print("Please write a 5 numbers")
user_input = int(input())

first_number = user_input // 10000

second_number = (user_input % 10000) // 1000

third_number = (user_input % 1000) // 100

fourth_number = (user_input % 100) // 10

fifth_number = user_input % 10

print(fifth_number,fourth_number,third_number,second_number,first_number)