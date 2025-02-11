
import math as m
def cos_taylor(x):
    return 1 - x**2/m.factorial(2) + x**4/m.factorial(4) - x**6/m.factorial(6) + x**8/m.factorial(8)

# Перевод 60 градусов в радианы
x = m.radians(60)
# Вывод приближённого значения cos(60°)
print(cos_taylor(x))
def sin_taylor(x):
    return x - x**3/m.factorial(3) + x**5/m.factorial(5) - x**7/m.factorial(7) + x**9/m.factorial(9)
# Перевод 30 градусов в радианы
x = m.radians(30)
# Вывод приближённого значения sin(30°)
print(sin_taylor(x))