def calc():
    try:
        a = float(input('Введите число a: '))
        b = float(input('Введите число b: '))
        operation = input('Введите операцию (*, /, +, -): ')

        if operation == "*":
            result = a * b
        elif operation == "/":
            if b == 0:
                raise ZeroDivisionError('На 0 делить нельзя!')
            result = a / b
        elif operation == "+":
            result = a + b
        elif operation == "-":
            result = a - b
        else:
            raise ValueError('Неизвестная операция.')

        print(f'Результат: {result}')
    except ValueError as e:
        print(f'Ошибка ввода: {e}')
    except ZeroDivisionError as e:
        print(f'Ошибка: {e}')
    except Exception as e:
        print(f'Произошла непредвиденная ошибка: {e}')

calc()
