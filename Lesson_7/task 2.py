"""
Дан список чисел. С помощью filter() получить список
тех элементов из исходного списка, значение которых
больше 0.
"""
num = [1,2,3,-1,-2,-3, 0]
def plus_or_minus(n):
    return n > 0
filter_num = list(filter(plus_or_minus,num))

print(filter_num)