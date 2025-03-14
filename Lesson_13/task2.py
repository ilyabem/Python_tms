def cyclic_sequence(seq):
    """Генераторная функция для циклической последовательности"""
    while True:  # Бесконечный цикл
        for num in seq:  # Перебираем числа в списке
            yield num  # Отдаем текущее число

# Исходная последовательность
sequence = [1, 2, 3]

# Запрос количества чисел у пользователя
n = int(input("Сколько чисел вывести? "))

# Создаем генератор
gen = cyclic_sequence(sequence)

# Выводим n чисел
for _ in range(n):
    print(next(gen), end=" ")