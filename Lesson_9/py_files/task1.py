import os
import shutil

def main():
    # Выводим имя операционной системы
    print(f"Имя вашей ОС: {os.name}")

    # Выводим путь до текущей папки
    current_dir = os.getcwd()
    print(f"Путь до текущей папки: {current_dir}")

    # Создаем словарь для хранения информации о файлах по их расширениям
    files_by_extension = {}
    total_size_by_extension = {}

    # Читаем все файлы в текущей директории
    for file in os.listdir(current_dir):
        file_path = os.path.join(current_dir, file)
        if os.path.isfile(file_path):
            ext = os.path.splitext(file)[1]  # Получаем расширение файла
            if ext not in files_by_extension:
                files_by_extension[ext] = []
                total_size_by_extension[ext] = 0
            files_by_extension[ext].append(file)
            total_size_by_extension[ext] += os.path.getsize(file_path)

    # Перемещаем файлы в соответствующие папки
    for ext, files in files_by_extension.items():
        if ext:  # Игнорируем файлы без расширения
            dir_name = ext[1:] + "_files"  # Убираем точку из расширения
            dir_path = os.path.join(current_dir, dir_name)
            os.makedirs(dir_path, exist_ok=True)

            for file in files:
                src_path = os.path.join(current_dir, file)
                dst_path = os.path.join(dir_path, file)
                shutil.move(src_path, dst_path)

            total_size_mb = total_size_by_extension[ext] / (1024 * 1024)
            print(f"В папке с {ext} файлами перемещено {len(files)} файлов, их суммарный размер - {total_size_mb:.2f} мегабайт")

    # Переименовываем один файл в одной из поддиректорий
    if '.txt' in files_by_extension:
        txt_dir = os.path.join(current_dir, "txt_files")
        if os.path.exists(txt_dir):
            old_name = os.path.join(txt_dir, files_by_extension['.txt'][0])
            new_name = os.path.join(txt_dir, "some_data.txt")
            os.rename(old_name, new_name)
            print(f"Файл {old_name} был переименован в {new_name}")

if __name__ == "__main__":
    main()