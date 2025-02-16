def nod(a, b):
    while b != 0:
        a, b = b, a % b  # Применяем алгоритм Евклида
    return a
num1 = 12
num2 = 18
print(nod(num1, num2))
