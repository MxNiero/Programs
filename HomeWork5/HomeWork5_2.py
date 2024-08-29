user_input = int(input("Вкажіть кількість секунд: "))

days = user_input // (24 * 60 * 60)
user_input %= 24 * 60 * 60

hours = user_input // (60 * 60)
user_input %= 60 * 60

minutes = user_input // 60
user_input %= 60

seconds = user_input

if 5 < days < 20 or days % 10 == 0 or days % 10 in range(5, 11):
    print(f"{days} Днів {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")

elif days % 10 in range(0, 9) and days != 0 and days % 10 != 1:
    print(f"{days} Дні {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")

elif days % 10 == 1:
    print(f"{days} День {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
