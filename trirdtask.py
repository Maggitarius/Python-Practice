a = int(input("Начало диапазона: "))
b = int(input("Конец диапазона:"))
for num in range(a, b + 1):
    if num <= 1:
        continue
    for i in range(2, num):
        if (num % i) == 0:
            break
    else:
        print(num, "Поздравляю! Это число является простым!")
input()