# Импортируем Counter из модуля collections
from collections import Counter

# Функция для проверки уникальности чисел в списке
def check_uniqueness(numbers):
    # Создаём словарь, который хранит количество вхождений каждого числа
    counter = Counter(numbers)

    # Создаём словарь дубликатов (числа, которые встречаются более 1 раза)
    duplicates = {num: count for num, count in counter.items() if count > 1}

    # Если дубликатов нет, выводим сообщение об уникальности списка
    if not duplicates:
        print("Все числа в списке уникальны.")
    else:
        # Если есть дубликаты, выводим их
        print("В списке есть дубликаты:")
        for num, count in duplicates.items():
            print(f"Число {num} встречается {count} раз(а).")

# Создаём список чисел
numbers = [1, 2, 3, 4, 5, 2, 6, 7, 8, 9, 1, 10, 3]

# Вызываем функцию для проверки списка
check_uniqueness(numbers)

