def main():
    try:
        weight = float(input("Введите ваш вес (кг): "))
        height = float(input("Введите ваш рост (м): "))

        if weight <= 0 or height <= 0:
            raise ValueError("Вес и рост должны быть положительными числами.")

        bmi = weight / (height ** 2)

        if bmi < 16:
            category = "Выраженный дефицит массы тела"
        elif bmi < 18.5:
            category = "Недостаточная масса тела"
        elif bmi < 25:
            category = "Норма, красавчик)"
        elif bmi < 30:
            category = "Избыточная масса тела"
        elif bmi < 35:
            category = "Ожирение первой степени"
        elif bmi < 40:
            category = "Ожирение второй степени"
        else:
            category = "Ожирение третьей степени"

        print(f"Ваш ИМТ: {bmi:.2f}")
        print(f"Категория: {category}")

    except ValueError as e:
        print(f"Ошибка ввода: {e}")


if __name__ == "__main__":
    main()