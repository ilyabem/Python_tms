#В текстовый файл построчно записаны фамилия и имя
#учащихся класса и оценка за контрольную. Вывести на экран
#всех учащихся, чья оценка меньше трёх баллов.
def print_students_with_low_grades(file_path):
    try:
        # Открываем файл для чтения
        with open(file_path, 'r', encoding='utf-8') as file:
            print("Учащиеся с оценкой меньше 3 баллов:")
            # Читаем файл построчно
            for line in file:
                # Разделяем строку на фамилию, имя и оценку
                parts = line.strip().split()
                if len(parts) >= 3:  # Проверяем, что строка содержит все три элемента
                    last_name, first_name, grade = parts[0], parts[1], int(parts[2])
                    # Проверяем оценку
                    if grade < 3:
                        print(f"{last_name} {first_name}: {grade} балла(ов)")
    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Путь к файлу с данными
file_path = "/Lesson_10/info_student.txt"

# Вызов функции для вывода учащихся с оценкой меньше 3
print_students_with_low_grades(file_path)