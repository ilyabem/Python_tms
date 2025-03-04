import re

def load_stop_words(stop_words_file):
    """Загружает список запрещённых слов из файла."""
    try:
        with open(stop_words_file, 'r', encoding='utf-8') as file:
            stop_words = file.read().split()  # Читаем и разделяем слова по пробелам
        return stop_words
    except FileNotFoundError:
        print(f"Файл '{stop_words_file}' не найден.")
        return []

def censor_text(text, stop_words):
    """Заменяет запрещённые слова в тексте на звёздочки."""
    for word in stop_words:
        # Используем регулярное выражение для замены слова в любом регистре
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        text = pattern.sub('*' * len(word), text)
    return text

def main():
    # Загружаем список запрещённых слов
    stop_words_file = "stop_words.txt"
    stop_words = load_stop_words(stop_words_file)
    if not stop_words:
        return  # Если файл не найден или пуст, завершаем программу

    # Получаем имя файла от пользователя
    input_file = input("Введите имя файла для цензуры: ")

    try:
        # Читаем содержимое файла
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()

        # Применяем цензуру
        censored_text = censor_text(text, stop_words)

        # Выводим результат на экран
        print(censored_text)
    except FileNotFoundError:
        print(f"Файл '{input_file}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()