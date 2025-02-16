import math

def easy_dig(n):
    # 1 не является простым числом
    if n <= 1:
        return False
    # 2 — простое число
    if n == 2:
        return True
    # Отсеиваем чётные числа, кроме 2
    if n % 2 == 0:
        return False
    # Проверяем делители от 3 до sqrt(n), только нечётные числа
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

num = 29
print(easy_dig(num))
