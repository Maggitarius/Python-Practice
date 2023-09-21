import random
print("Вам загадано число от 0 до 1000. Попробуйте угадать его за минимальное количество попыток.")
a = random.randint(0, 1000)
b = int(input("Введите число: "))
while b != a:
    if b > a:
        print("Меньше")
    else:
        print("Больше")
    b = int(input("Введите число: "))
print("Поздравляю, вы угадали!")