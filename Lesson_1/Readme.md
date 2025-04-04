# Перевод десятичных чисел в двоичную систему

Этот файл содержит процесс перевода десятичных чисел в двоичную систему и обратно.

## Числа для перевода:
- 15 → ?
- 27 → ?
- 73 → ?
- 105 → ?

## Метод перевода
Для перевода числа из десятичной системы в двоичную необходимо:
1. Последовательно делить число на 2, записывая остатки.
2. Записывать результаты деления до получения нуля в частном.
3. Прочитать остатки снизу вверх — это и будет двоичное представление числа.

## Результаты перевода
| Десятичное | Двоичное |
|------------|---------|
| 15         | 1111    |
| 27         | 11011   |
| 73         | 1001001 |
| 105        | 1101001 |

## Пример вычислений (для 15):
```
15 ÷ 2 = 7, остаток 1
 7 ÷ 2 = 3, остаток 1
 3 ÷ 2 = 1, остаток 1
 1 ÷ 2 = 0, остаток 1
```
**Ответ:** 1111 (читаем остатки снизу вверх).

Аналогично выполняются вычисления для остальных чисел.

## Перевод двоичных чисел в десятичную систему
| Двоичное   | Десятичное |
|------------|-----------|
| 111        | 7         |
| 10101      | 21        |
| 11011      | 27        |
| 110101011  | 427       |

Для перевода двоичного числа в десятичное необходимо:
1. Умножить каждую цифру двоичного числа на 2 в степени её позиции (считая справа налево, начиная с нуля).
2. Просуммировать полученные значения.

**Пример вычислений (для 11011):**
```
1 × 2^4 = 16
1 × 2^3 = 8
0 × 2^2 = 0
1 × 2^1 = 2
1 × 2^0 = 1
Сумма: 16 + 8 + 0 + 2 + 1 = 27

