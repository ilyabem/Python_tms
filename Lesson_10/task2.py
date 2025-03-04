from collections import Counter

def find_most_common_word(line):
    """Находит самое часто встречающееся слово в строке и количество его повторений."""
    words = line.strip().split()  # Разделяем строку на слова
    if not words:  # Если строка пустая, возвращаем None
        return None, 0
    # Используем Counter для подсчета частоты слов
    word_counts = Counter(words)
    # Находим самое часто встречающееся слово
    most_common_word, count = word_counts.most_common(1)[0]
    return most_common_word, count

def process_file(input_file, output_file):
    """Обрабатывает входной файл и записывает результат в выходной файл."""
    try:
        with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
            for line in infile:
                most_common_word, count = find_most_common_word(line)
                if most_common_word:  # Если строка не пустая
                    outfile.write(f"{most_common_word} {count}\n")
    except FileNotFoundError:
        print(f"Файл '{input_file}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Укажите пути к входному и выходному файлам
input_file = '/Lesson_10/txtFiles/input.txt'  # Замените на путь к вашему файлу
output_file = "/Lesson_10/txtFiles/output.txt"  # Замените на путь к выходному файлу

# Обработка файла
process_file(input_file, output_file)