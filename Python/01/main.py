from math import sqrt


def check(n):
    try:
        n = int(n)
    except:
        return "Введено не целочисленное значение"
    if n < 0:
        return "Число меньше 0"
    if n == 0 or n == 1:
        return f"{n} не является простым числом"
    for i in range(2, int(sqrt(n))):
        if n % i == 0:
            return f"{n} не является простым числом"
    return f"{n} является простым числом"


x = input("Введите число: ")
print(check(x))
