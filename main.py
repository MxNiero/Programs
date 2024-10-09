x = int(input("Введіть х: "))
y = int(input("Введіть y: "))

if x * x + y * y <= 9:
    if y + x > 0 and x - y > 0:
        print("Належить")
    else:
        if y + x < 0 and x - y > 0:
            print("Належить")
        else:
            print("Не належить")
else:
    print("Не належить\n")
