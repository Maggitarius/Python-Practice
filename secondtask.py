a = int(input("Введите число: "))
if a <= 1:
    print(a, "Это число не является простым")
else:
    for i in range(2, a):
        if (a % i) == 0:
            print(a, "Это число не является простым")
            break
    else:
        print(a, "Это число являестя простым! Поздравляю!")
input()