def binary_search(arr, target, left, right):
    if left > right:
        return -1

    #Находим середину списка
    mid = (left + right) // 2
    #Если целевое чесло равно середине списка - возвращаем середину списка
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        #ищем в левой части списка
        return binary_search(arr, target, left, mid -1 )
    # ищем в правой части списка
    else:
        return binary_search(arr, target, mid, right +1)

arr = [1, 3, 5, 7, 9, 11, 13]
target = 11

result = binary_search(arr, target, 0, len(arr)- 1)
print(f"Индекс элемента {target}: {result}")