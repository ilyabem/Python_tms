'''''
Дан список чисел. С помощью map() получить список, 
где каждое число из исходного списка переведено в строку. 
Пример: на входе – [1, 2, 3], на выходе – [‘1’, ‘2’, ‘3’]
'''''
'''''
num = [1, 2, 3, 4]
#Преобразуем значение в строку используя str
nums = list(map(str, num))
print(nums)
'''''


#а если я зохочу поставить любой другой символ
num = [1, 2, 3, 4]
# Так же преобразуем в строку
nums = list(map(str, num))
# Объединяем элементы списка разделяя их двоеточиями
result = ':'.join(nums)
print(result)

# а еще можно сделать так
#print('[' + ':'.join(nums) + ']')  # [1:2:3]
